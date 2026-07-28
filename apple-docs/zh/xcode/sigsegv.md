---
title: EXC_BAD_ACCESS (SIGSEGV)
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/sigsegv
source_url: 'https://developer.apple.com/documentation/xcode/sigsegv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/sigsegv.json'
content_hash: 'sha256:910581911da60a09'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Diagnosing issues using crash reports and device logs](diagnosing-issues-using-crash-reports-and-device-logs.md) · [Understanding the exception types in a crash report](understanding-the-exception-types-in-a-crash-report.md)

# EXC_BAD_ACCESS (SIGSEGV)

<sub>文章</sub>

内存段错误终止了该进程，通常是因为该进程试图访问内存中无效或越界的地址。

## 概述

常见的问题包括访问数组中的无效索引、解引用指向无效内存位置的指针，或写入只读内存。

更多信息，请参阅[排查内存访问崩溃](investigating-memory-access-crashes.md)。

## 另请参阅

### 异常

- [EXC_ARITHMETIC](exc_arithmetic.md) — 算术问题终止了该进程，通常是因为除以零或浮点数错误。
- [EXC_BAD_ACCESS](exc_bad_access.md) — 错误的内存访问终止了该进程。
- [EXC_BAD_ACCESS (SIGBUS)](sigbus.md) — 总线错误终止了该进程，通常是因为该进程试图访问内存中未对齐或无效的地址，或是由于指针验证失败。
- [EXC_BREAKPOINT (SIGTRAP) and EXC_BAD_INSTRUCTION (SIGILL)](sigtrap_sigill.md) — 跟踪陷阱或无效的 CPU 指令中断了该进程，通常是因为该进程违反了某项要求或超时。
- [EXC_CRASH](exc_crash.md) — 该进程发生了崩溃。
- [EXC_CRASH (SIGABRT)](sigabrt.md) — 该进程因收到中止信号而终止。
- [EXC_CRASH (SIGKILL)](sigkill.md) — 操作系统终止了该进程，通常是因为后台任务违反了某项要求、设备资源有限，或用户强制退出了 App。
- [EXC_CRASH (SIGQUIT)](sigquit.md) — 另一个进程终止了该进程，通常是因为该进程违反了某项要求或超时。
- [EXC_CRASH (SIGSYS)](sigsys.md) — 系统调用的错误参数终止了该进程。
- [EXC_CRASH (SIGTERM)](sigterm.md) — 软件终止信号终止了该进程。
- [EXC_GUARD](exc_guard.md) — 该进程违反了受保护资源的保护机制，通常与文件描述符有关。
- [EXC_RESOURCE](exc_resource.md) — 操作系统因该进程超出了资源消耗限制（如 CPU 时间或内存）而停止了该进程。
