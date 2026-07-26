---
title: EXC_CRASH (SIGTERM)
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/sigterm
source_url: 'https://developer.apple.com/documentation/xcode/sigterm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/sigterm.json'
content_hash: 'sha256:30656ae866a19b18'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Diagnosing issues using crash reports and device logs](diagnosing-issues-using-crash-reports-and-device-logs.md) · [Understanding the exception types in a crash report](understanding-the-exception-types-in-a-crash-report.md)

# EXC_CRASH (SIGTERM)

<sub>Article</sub>

A software termination signal terminated the process.

## Overview

This signal is often sent shortly before `SIGKILL`, to give the process an opportunity to terminate cleanly. The user can also send this signal using the `kill` command in Terminal, if no specific signal is specified.

For more information about how the system stops apps and services, see [The Life Cycle of a Daemon](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/Lifecycle.html) in _Daemons and Services Programming Guide_.

## See Also

### Exceptions

- [EXC_ARITHMETIC](exc_arithmetic.md) — An arithmetic problem terminated the process, often because of division by zero or a floating-point error.
- [EXC_BAD_ACCESS](exc_bad_access.md) — A bad access to memory terminated the process.
- [EXC_BAD_ACCESS (SIGBUS)](sigbus.md) — A bus error terminated the process, often because the process tried to access a misaligned or invalid address in memory, or due to a pointer authentication failure.
- [EXC_BAD_ACCESS (SIGSEGV)](sigsegv.md) — A memory segmentation fault terminated the process, often because the process tried to access an invalid or out-of-bounds address in memory.
- [EXC_BREAKPOINT (SIGTRAP) and EXC_BAD_INSTRUCTION (SIGILL)](sigtrap_sigill.md) — A trace trap or invalid CPU instruction interrupted the process, often because the process violated a requirement or timeout.
- [EXC_CRASH](exc_crash.md) — The process crashed.
- [EXC_CRASH (SIGABRT)](sigabrt.md) — The process terminated because it received an abort signal.
- [EXC_CRASH (SIGKILL)](sigkill.md) — The operating system terminated the process, often because a background task violated a requirement, device resources were limited, or the user force quit the app.
- [EXC_CRASH (SIGQUIT)](sigquit.md) — Another processes terminated the process, often because the process violated a requirement or timeout.
- [EXC_CRASH (SIGSYS)](sigsys.md) — A bad argument to a system call terminated the process.
- [EXC_GUARD](exc_guard.md) — The process violated a guarded resource protection, often related to file descriptors.
- [EXC_RESOURCE](exc_resource.md) — The operating system stopped the process because the process exceeded a limit on resource consumption, like CPU time or memory.
