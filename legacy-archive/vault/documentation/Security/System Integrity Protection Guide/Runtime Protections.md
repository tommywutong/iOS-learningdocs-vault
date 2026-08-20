---
title: System Integrity Protection Guide
apple_id: TP40016462
resource_type: Guide
platform: Xcode Developer Tools|macOS
topic: Security
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/System_Integrity_Protection_Guide/RuntimeProtections/RuntimeProtections.html
archived_at: '2026-07-18T02:06:31.797135Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [System Integrity Protection Guide](Introduction.md)


[Next](Kernel%20Extensions.md)[Previous](File%20System%20Protections.md)

# Runtime Protections

When a process is started, the kernel checks to see whether the main executable is protected on disk or is signed with an special system entitlement. If either is true, then a flag is set to denote that it is protected against modification. Any attempt to attach to a protected process is denied by the kernel.

Attempting to get the Mach task for a process using the `task_for_pid` function or attempting to get the permissions of a set of tasks using the `processor_set_tasks` function fails, returning `EPERM`.

Spawning children processes of processes restricted by System Integrity Protection, such as by launching a helper process in a bundle with `NSTask` or calling the `exec(2)` command, resets the Mach special ports of that child process. Any dynamic linker (`dyld`) environment variables, such as `DYLD_LIBRARY_PATH`, are purged when launching protected processes.

DTrace cannot be used to inspect system processes, whether from the Instruments application or the `dtrace(1)` command-line tool.

Attempting to attach to a system process, such as with LLDB, fails—even when running as root with sudo:

```
$> sudo lldb -n Finder
(lldb) process attach —name "Finder"
error: attach failed: attach failed: lost connection
```

[Next](Kernel%20Extensions.md)[Previous](File%20System%20Protections.md)

