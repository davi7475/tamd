#!/home/davi/YAMD/.venv/bin/python
import sys
from jsonpath_rw.bin.jsonpath import entry_point
if __name__ == '__main__':
    sys.argv[0] = sys.argv[0].removesuffix('.exe')
    sys.exit(entry_point())
