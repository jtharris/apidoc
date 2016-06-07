import os
import os.path
import sys

APP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app'))
sys.path.append(APP_DIR)

os.environ['ENV_CONFIG'] = 'test'
