from pathlib import Path
import sys

# tests
cwd = Path(__file__).parent.resolve()
repo_root = cwd.parent
src_folder = repo_root / 'src'

sys.path.append(str(src_folder))
