import os
import sys

if len(sys.argv) == 1 or int(sys.argv[1]) == 0:
    print('')
    print('=================')
    print('Running test 0')
    print('=================')
    os.system('flake8 --ignore "N801, E203, E266, E501, W503, F812, E741, N803, N802, N806" tests/')

if len(sys.argv) == 1 or int(sys.argv[1]) == 1:
    print('')
    print('=================')
    print('Running test 1')
    print('=================')
    os.system('python -m pytest tests/')
