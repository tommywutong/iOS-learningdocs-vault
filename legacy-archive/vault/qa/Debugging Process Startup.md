---
title: Debugging Process Startup
apple_id: DTS10004557
resource_type: QA
platform: macOS
topic: Xcode
technology: null
published: '2007-12-21'
source_url: https://developer.apple.com/library/archive/qa/qa1573/_index.html
archived_at: '2026-07-18T02:32:19.616282Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1573

# Debugging Process Startup

## Q:  How do I debug a process's startup code?

A: This depends on how the process is launched. For a typical application-level process, you can debug the startup code by launching it from within the debugger in Xcode. However, there may be circumstances where that's not an option. For example:

- if the problem is masked by starting the application in the debugger
- if the program isn't a typical application (for example it might be a CUPS filter)

The following sections describe various ways to debug a process's startup code.

If you can build the program from source, it's trivial to add code to stop the program at the first line of main. Listing 1 shows an example of this.

__Listing 1__  Code to stop at startup

```c
#include <signal.h> #include <unistd.h> int main(int argc, char **argv) {     (void) raise(SIGSTOP);     /// rest of your code here }
```

This sends a `SIGSTOP` to the process, which stops its execution so that you can attach using GDB. Alternatively, you can resume execution by sending the process a `SIGCONT` using kill.

If it's not convenient to build the program from source, you can use a variety of other techniques. If your program is managed by `launchd`, you can add the `WaitForDebugger` property to your property list file to have `launchd` stop your program before it it executes a single instruction. See the man page for details.

If your program is not managed by `launchd`, you can use GDB's `--waitfor` option. GDB will poll the process list waiting for a matching process to be launched. You can supply the option either on the command line or as an argument to GDB's `attach` command.

The fact that GDB polls the process list has two drawbacks. Firstly, it consumes a lot of CPU while waiting for the process to be launched. Secondly, the program stops in an indeterminate state. If you're running on Mac OS X 10.5 or later, it's probably better to use [DTrace](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinjvg4wugsbrfvjukq2ekrjecq2f) instead.

Listing 2 shows an example DTrace script that sets a probe on a commonly used system call (`getpid`) and, when that probe is hit, stops the process and invokes GDB on it. Listing 3 shows an example of its use.

__Listing 2__  WaitAttach.d

```
#! /usr/sbin/dtrace -w -q -s  syscall::getpid:entry / execname == $$1 / {     stop();     system(         "echo attach %d > /tmp/WaitAttach.gdb ; gdb -x /tmp/WaitAttach.gdb",          pid     );     exit(0); }
```


__Listing 3__  Using WaitAttach.d

```
$ # Make the script executable $ chmod ugo+x WaitAttach.d $ # Run it $ sudo ./WaitAttach.d TextEdit GNU gdb 6.3.50-20050815 [...] [... now launch TextEdit ...] Attaching to process 3723. Reading symbols for shared libraries . done 0x8fe21a25 in __dyld_getpid () (gdb) bt #0  0x8fe21a25 in __dyld_getpid () #1  0x8fe07139 in __dyld__ZN4dyld5_mainEPK11mach_headermiPPKcS5_S5_ () #2  0x8fe01872 in __dyld__ZN13dyldbootstrap5startEPK11mach_headeriPPKcl () #3  0x8fe01037 in __dyld__dyld_start ()
```

You can modify this script to meet your particular needs. For example:

- The script sets the probe on `getpid`, which is currently the first system call made by a process. You can change this to any other system call (by changing "getpid" to something else), or to match all system calls (by deleting "getpid" entirely).
- The script currently matches the process by its executable name. This is an exact string match. You can use a fuzzy match by invoking DTrace functions like `strstr`.
- You can also extend the match to look for other criteria. For example, you can use the DTrace built in variable `ppid` to filter on the parent process ID.
- As it stands the script runs GDB as root. If that's a problem, you can change the script to invoke the chroot command to set the user and group ID of GDB to whatever you desire.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-12-21 | New document that describes techniques for debugging a process's startup code. |

