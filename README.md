```
======================================== beginning repro.py in Dockerfile.inner container run by docker-dind in GCB
Traceback (most recent call last):
  File "/workspace/repro.py", line 31, in <module>
    main()
  File "/workspace/repro.py", line 23, in main
    with losetup_ctxmgr() as device:
  File "/usr/lib/python3.7/contextlib.py", line 112, in __enter__
    return next(self.gen)
  File "/workspace/repro.py", line 18, in losetup_ctxmgr
    device = losetup(*args).stdout.decode("utf8").strip()
  File "/usr/lib/python3.7/site-packages/sh.py", line 1427, in __call__
    return RunningCommand(cmd, call_args, stdin, stdout, stderr)
  File "/usr/lib/python3.7/site-packages/sh.py", line 774, in __init__
    self.wait()
  File "/usr/lib/python3.7/site-packages/sh.py", line 792, in wait
    self.handle_command_exit_code(exit_code)
  File "/usr/lib/python3.7/site-packages/sh.py", line 815, in handle_command_exit_code
    raise exc
sh.ErrorReturnCode_1: 

  RAN: /sbin/losetup -f --show --offset 0 --sizelimit 50000000000 /workspace/disk.img

  STDOUT:


  STDERR:
losetup: /workspace/disk.img: failed to set up loop device: Resource temporarily unavailable
ERROR
ERROR: build step 0 "gcr.io/cloud-builders/docker" failed: exit status 1
```
