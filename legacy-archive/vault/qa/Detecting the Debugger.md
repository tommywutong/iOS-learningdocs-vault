---
title: Detecting the Debugger
apple_id: DTS10003368
resource_type: QA
platform: Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2004-10-27'
source_url: https://developer.apple.com/library/archive/qa/qa1361/_index.html
archived_at: '2026-07-18T02:30:26.201416Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1361

# Detecting the Debugger

## Q:  How do I determine if I'm being run under the debugger?

A: How do I determine if I'm being run under the debugger?

The code in Listing 1 shows the best way to do this.

__Listing 1__  Are you being debugged?

```c
#include <assert.h> #include <stdbool.h> #include <sys/types.h> #include <unistd.h> #include <sys/sysctl.h>  static bool AmIBeingDebugged(void)     // Returns true if the current process is being debugged (either      // running under the debugger or has a debugger attached post facto). {     int                 junk;     int                 mib[4];     struct kinfo_proc   info;     size_t              size;      // Initialize the flags so that, if sysctl fails for some bizarre      // reason, we get a predictable result.      info.kp_proc.p_flag = 0;      // Initialize mib, which tells sysctl the info we want, in this case     // we're looking for information about a specific process ID.      mib[0] = CTL_KERN;     mib[1] = KERN_PROC;     mib[2] = KERN_PROC_PID;     mib[3] = getpid();      // Call sysctl.      size = sizeof(info);     junk = sysctl(mib, sizeof(mib) / sizeof(*mib), &info, &size, NULL, 0);     assert(junk == 0);      // We're being debugged if the P_TRACED flag is set.      return ( (info.kp_proc.p_flag & P_TRACED) != 0 ); }
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-10-27 | New document that shows how to determine whether you're being run under the debugger. |

