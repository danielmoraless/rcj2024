import os
import hashlib
from glob import glob

def cach_all() -> list:
	cached = []
	w = os.walk(".")

	for (dirpath, dirnames, filenames) in w:
		pyfiles = glob(os.path.join(dirpath, "*.py"))
		for pyfile in pyfiles:
			with open(pyfile, "rb") as f:
				cached += pyfile, hashlib.md5(f.read()).hexdigest()


	return cached

def watch() -> tuple:
	old_cache = cach_all()
	loc = len(old_cache)

	while True:
		new_cache = cach_all()
		lnc = len(new_cache)

		if lnc > loc:
			for i in range(0, loc, 2):
				if old_cache[i] != new_cache[i]: return (new_cache[i], "NEW")
		if lnc < loc:
			for i in range(0, lnc, 2):
				if old_cache[i] not in new_cache: return (old_cache[i], "REM")
		if lnc == loc:
			for i in range(1, lnc, 2):
				if old_cache[i] != new_cache[i]: return (new_cache[i-1], "MOD")