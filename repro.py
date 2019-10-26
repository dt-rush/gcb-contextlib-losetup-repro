#!/usr/bin/python3 -u

from contextlib import contextmanager
from sh import (
        file,
        losetup
)
from time import sleep

IMAGE = "/workspace/disk.img"

print("======================================== beginning repro.py in Dockerfile.inner container run by docker-dind in GCB")

@contextmanager
def losetup_ctxmgr():
    args = ["-f", "--show", "--offset", "0", "--sizelimit", "50000000000"]
    args.append(IMAGE)
    device = losetup(*args).stdout.decode("utf8").strip()
    yield device
    losetup("-d", device)

def main():
    with losetup_ctxmgr() as device:
        out = file("-s", device).stdout.decode("utf8").strip()
        print(out)
    with losetup_ctxmgr() as device:
        out = file("-s", device).stdout.decode("utf8").strip()
        print(out)

if __name__ == "__main__":
    main()
