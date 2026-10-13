"""Registro de hashes sem obter dados nem expor conteúdos individuais."""
from pathlib import Path
import hashlib
import platform
import importlib.metadata

def sha256_file(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()

def environment():
    return {'python': platform.python_version(), 'packages': {
        name: importlib.metadata.version(name)
        for name in ('numpy', 'pandas', 'scikit-learn')
    }}
