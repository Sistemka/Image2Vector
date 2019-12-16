from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
FILES_DIR = Path(BASE_DIR, 'files')
FILES_DIR.mkdir(parents=True, exist_ok=True)
