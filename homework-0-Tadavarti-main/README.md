# CSE 598 Introduction to Deep Learning

## Homework 0

### Instructions

You are expected to be familiar with Python, Git and GitHub. Check the course materials for pointers if you are not familiar.

Follow these instructions:

1. Clone the repository to your local machine:

   ```
   $ git clone LINK
   ```

1. Create a virtual environment with the required packages:

   ```
   $ cd FOLDER
   $ python3 -m venv venv
   $ source venv/bin/activate
   $ python -m pip install -r requirements.txt
   ```

1. Implement the `add(a, b)` and `sort(a)` methods in `operators.py`. You only need to write one line for each. It is fine if you need to use more than one line, but you only need one line for each method.

1. Test that your implementation works:
   
   ```
   $ python run_tests.py
   ```

   Your implementation works if you see the following output:

   ```
   =================
   Running test 0
   =================

   =================
   Running test 1
   =================
   ================================================================================ test session starts ================================================================================
   platform darwin -- Python 3.7.7, pytest-6.0.1, py-1.10.0, pluggy-0.13.1
   hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase('/Users/eduardo/work/cse598.github/homework0.sol/.hypothesis/examples')
   rootdir: /Users/eduardo/work/cse598.github/homework0.sol
   plugins: hypothesis-4.38.0
   collected 2 items

   tests/test_operators.py ..                                                                                                                                                    [100%]

   ================================================================================= 2 passed in 0.27s =================================================================================
   ```

   The trace will make it clear if you fail any test case. There are two test cases:
   * `test 0` tests for style. Read about [`flake8`](https://flake8.pycqa.org/en/latest/) and how to fix most style issues automatically with [`black`](https://github.com/psf/black).
   * `test 1` tests that your `add(a, b)` and `sort(a)` work properly.

1. After you pass the tests cases locally, push your changes to the repository. Check the intro materials for references about how to use GitHub if you are not used to it. You have to `commit` and `push` the changes to your repository. After you push, the test cases are run automatically on GitHub after a brief delay. While the test are running, you will see the following:

   <img width="964" alt="test_running" src="https://user-images.githubusercontent.com/9103274/130525784-67563652-22ac-4539-84d1-92ed930646bb.png">


   You have completed the assignment successfully (i.e., passed all the test cases) if you see a screen like the following:

   <img width="700" alt="tests_passed" src="https://user-images.githubusercontent.com/9103274/130526013-6c46b66d-6773-4272-bdb8-ffa4b6279647.png">
   
   If you have not completed the assignment successfully (i.e., at least one test case fails), you will see a screen like the following:

   <img width="605" alt="test_failed" src="https://user-images.githubusercontent.com/9103274/130526020-c36dcdb5-8991-40ed-b7c2-5f3f38abe882.png">

   Clicking on `Feedback` will give you details about what test cases pass and fail. **If you pass the test cases locally, you will pass them on GitHUb. Please help us minimize the GitHub resources we need and do not push every other minute.**

1. Read the preliminaries to get started with MiniTorch:
   * [Workspace Setup](https://minitorch.github.io/setup.html)
   * [Contributing](https://minitorch.github.io/contributing.html)


 
