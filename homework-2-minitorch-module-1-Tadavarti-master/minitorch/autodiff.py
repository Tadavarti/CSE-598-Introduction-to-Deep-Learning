variable_count = 1


class Variable:
    """
    Attributes:
        history (:class:`History` or None) : the Function calls that created this variable or None if constant
        derivative (variable type): the derivative with respect to this variable
        grad (variable type) : alias for derivative (PyTorch name)
        name (string) : an optional name for debugging
    """

    def __init__(self, history, name=None):
        global variable_count
        assert history is None or isinstance(history, History), history

        self.history = history
        self._derivative = None

        # This isFinal a bit simplistic, but make things easier.
        variable_count += 1
        self.unique_id = "Variable" + str(variable_count)

        # For debugging can have a name.
        if name is not None:
            self.name = name
        else:
            self.name = self.unique_id

        self.used = 0

    def requires_grad_(self, val):
        """
        Set the requires_grad flag to `val` on variable.

        Ensures that operations on this variable will trigger
        backpropagation.

        Args:
            val (bool): whether to require grad
        """
        self.history = History()

    def backward(self, d_output=None):
        """
        Calls autodiff to fill in the derivatives for the history of this object.

        Args:
            d_output (number, opt): starting derivative to backpropagate through the model
                                   (typically left out, and assumed to be 1.0).
        """
        if d_output is None:
            d_output = 1.0
        backpropagate(self, d_output)

    @property
    def derivative(self):
        return self._derivative

    def is_leaf(self):
        "True if this variable created by the user (no `last_fn`)"
        return self.history.last_fn is None

    ## IGNORE
    def accumulate_derivative(self, val):
        """
        Add `val` to the the derivative accumulated on this variable.
        Should only be called during autodifferentiation on leaf variables.

        Args:
            val (number): value to be accumulated
        """
        assert self.is_leaf(), "Only leaf variables can have derivatives."
        if self._derivative is None:
            self._derivative = self.zeros()
        self._derivative += val

    def zero_derivative_(self):  # pragma: no cover
        """
        Reset the derivative on this variable.
        """
        self._derivative = self.zeros()

    def zero_grad_(self):  # pragma: no cover
        """
        Reset the derivative on this variable.
        """
        self.zero_derivative_()

    def expand(self, x):
        "Placeholder for tensor variables"
        return x

    # Helper functions for children classes.

    def __radd__(self, b):
        return self + b

    def __rmul__(self, b):
        return self * b

    def zeros(self):
        return 0.0


def wrap_tuple(x):
    "Turn a possible value into a tuple"
    if isinstance(x, tuple):
        return x
    return (x,)


def unwrap_tuple(x):
    "Turn a singleton tuple into a value"
    if len(x) == 1:
        return x[0]
    return x


class Context:
    """
    Context class is used by `Function` to store information during the forward pass.

    Attributes:
        no_grad (bool) : do not save gradient information
        saved_values (tuple) : tuple of values saved for backward pass
        saved_tensors (tuple) : alias for saved_values (PyTorch name)

    """

    def __init__(self, no_grad=False):
        self._saved_values = None
        self.no_grad = no_grad

    def save_for_backward(self, *values):
        """
        Store the given `values` if they need to be used during backpropagation.

        Args:
            values (list of values) : values to save for backward
        """
        if self.no_grad:
            return
        self._saved_values = values

    @property
    def saved_values(self):
        assert not self.no_grad, "Doesn't require grad"
        assert self._saved_values is not None, "Did you forget to save values?"
        return unwrap_tuple(self._saved_values)

    @property
    def saved_tensors(self):  # pragma: no cover
        return self.saved_values


class History:
    """
    `History` stores the history of `Function` operations that was
    used to construct the current Variable.

    Attributes:
        last_fn (:class:`FunctionBase`) : The last Function that was called.
        ctx (:class:`Context`): The context for that Function.
        inputs (list of inputs) : The inputs that were given when `last_fn.forward` was called.

    """

    def __init__(self, last_fn=None, ctx=None, inputs=None):
        self.last_fn = last_fn
        self.ctx = ctx
        self.inputs = inputs

    def backprop_step(self, d_output):
        """
        Run one step of backpropagation by calling chain rule.

        Args:
            d_output : a derivative with respect to this variable

        Returns:
            list of numbers : a derivative with respect to `inputs`
        """
        return self.last_fn.chain_rule(self.ctx, self.inputs, d_output)


class FunctionBase:
    """
    A function that can act on :class:`Variable` arguments to
    produce a :class:`Variable` output, while tracking the internal history.

    Call by :func:`FunctionBase.apply`.

    """

    @staticmethod
    def variable(raw, history):
        raise NotImplementedError()

    @classmethod
    def apply(cls, *vals):
        raw_vals = []
        need_grad = False
        for v in vals:
            if isinstance(v, Variable):
                if v.history is not None:
                    need_grad = True
                v.used += 1
                raw_vals.append(v.get_data())
            else:
                raw_vals.append(v)
        ctx = Context(not need_grad)
        c = cls.forward(ctx, *raw_vals)
        assert isinstance(c, cls.data_type), "Expected return typ %s got %s" % (
            cls.data_type,
            type(c),
        )
        back = None
        if need_grad:
            back = History(cls, ctx, vals)
        return cls.variable(cls.data(c), back)

    @classmethod
    def chain_rule(cls, ctx, inputs, d_output):
        out = cls.backward(ctx , d_output)
        output = []
        if type(out) == float :
            out = out

        else:
            out = list(out)
            for i in range(len(inputs)):
                if(not is_constant(inputs[i])):
                    output.append((inputs[i], out[i]))
        return(output)
        raise NotImplementedError('Need to implement for Task 1.3')


def is_constant(val):
    return not isinstance(val, Variable) or val.history is None


def topological_sort(variable):
    "Returns nodes in topological order"
    order = []
    seen = set()

    def visit(var):
        if var.unique_id in seen:
            return
        if not var.is_leaf():
            for m in var.history.inputs:
                if not is_constant(m):
                    visit(m)
        seen.add(var.unique_id)
        order.insert(0, var)

    visit(variable)
    return order


def backpropagate(variable, deriv):
    # TODO: Implement for Task 1.4.
    order = topological_sort(variable)
    accumulate_derivative = {order[0].unique_id: deriv}
    print("order" , order)
    for i in order:
        if (i.is_leaf()):
            i.accumulate_derivative(accumulate_derivative[i.unique_id])
        else:
            node_history = i.history.last_fn.chain_rule(ctx=i.history.ctx, inputs=i.history.inputs, d_output=accumulate_derivative[i.unique_id])
            for vari, deri in node_history:
                if vari.unique_id in accumulate_derivative.keys():
                    accumulate_derivative[vari.unique_id] += deri
                else:
                    accumulate_derivative[vari.unique_id] = deri
    # raise NotImplementedError('Need to implement for Task 1.4')