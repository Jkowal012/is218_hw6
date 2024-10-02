# Was getting an error trying to locate calculator folder, this fixed it
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
