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
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Diagnosing issues using crash reports and device logs](diagnosing-issues-using-crash-reports-and-device-logs.md) · [Understanding the exception types in a crash report](understanding-the-exception-types-in-a-crash-report.md)

# EXC_CRASH (SIGTERM)

<sub>文章</sub>

软件终止信号终止了该进程。

## 概述

该信号通常在 `SIGKILL` 之前不久发出，以便让该进程有机会正常终止。如果未指定具体信号，用户也可以在终端中使用 `kill` 命令发送该信号。

有关系统如何停止 App 和服务的更多信息，请参阅《_Daemons and Services Programming Guide_》中的 [The Life Cycle of a Daemon](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/Lifecycle.html)。

## 另请参阅

### 异常

- [EXC_ARITHMETIC](exc_arithmetic.md) — 算术问题终止了该进程，通常是因为除以零或浮点数错误。
- [EXC_BAD_ACCESS](exc_bad_access.md) — 错误的内存访问终止了该进程。
- [EXC_BAD_ACCESS (SIGBUS)](sigbus.md) — 总线错误终止了该进程，通常是因为该进程试图访问内存中未对齐或无效的地址，或是由于指针验证失败。
- [EXC_BAD_ACCESS (SIGSEGV)](sigsegv.md) — 内存段错误终止了该进程，通常是因为该进程试图访问内存中无效或越界的地址。
- [EXC_BREAKPOINT (SIGTRAP) and EXC_BAD_INSTRUCTION (SIGILL)](sigtrap_sigill.md) — 跟踪陷阱或无效的 CPU 指令中断了该进程，通常是因为该进程违反了某项要求或超时。
- [EXC_CRASH](exc_crash.md) — 该进程发生了崩溃。
- [EXC_CRASH (SIGABRT)](sigabrt.md) — 该进程因收到中止信号而终止。
- [EXC_CRASH (SIGKILL)](sigkill.md) — 操作系统终止了该进程，通常是因为后台任务违反了某项要求、设备资源有限，或用户强制退出了 App。
- [EXC_CRASH (SIGQUIT)](sigquit.md) — 另一个进程终止了该进程，通常是因为该进程违反了某项要求或超时。
- [EXC_CRASH (SIGSYS)](sigsys.md) — 系统调用的错误参数终止了该进程。
- [EXC_GUARD](exc_guard.md) — 该进程违反了受保护资源的保护机制，通常与文件描述符有关。
- [EXC_RESOURCE](exc_resource.md) — 操作系统因该进程超出了资源消耗限制（如 CPU 时间或内存）而停止了该进程。
