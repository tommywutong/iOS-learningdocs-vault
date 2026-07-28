---
title: EXC_BAD_ACCESS (SIGBUS)
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/sigbus
source_url: 'https://developer.apple.com/documentation/xcode/sigbus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/sigbus.json'
content_hash: 'sha256:49cea33409715cc4'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [使用崩溃报告和设备日志诊断问题](diagnosing-issues-using-crash-reports-and-device-logs.md) · [了解崩溃报告中的异常类型](understanding-the-exception-types-in-a-crash-report.md)

# EXC_BAD_ACCESS (SIGBUS)

<sub>文章</sub>

总线错误终止了进程，通常是因为进程尝试访问内存中未对齐或无效的地址，或因为指针认证失败。

## 概述

常见问题包括访问数组中的无效索引、解引用指向无效内存位置的指针，或写入只读内存。在许多情况下，这些问题会产生 `SIGSEGV` 而不是 `SIGBUS`。

有关更多信息，请参阅[调查内存访问崩溃](investigating-memory-access-crashes.md)。

## 另请参阅

### 异常

- [EXC_ARITHMETIC](exc_arithmetic.md) — 算术问题终止了进程，通常是因为除以零或浮点错误。
- [EXC_BAD_ACCESS](exc_bad_access.md) — 对内存的错误访问终止了进程。
- [EXC_BAD_ACCESS (SIGSEGV)](sigsegv.md) — 内存分段错误终止了进程，通常是因为进程尝试访问内存中无效或越界的地址。
- [EXC_BREAKPOINT (SIGTRAP) and EXC_BAD_INSTRUCTION (SIGILL)](sigtrap_sigill.md) — 跟踪陷阱或无效的 CPU 指令中断了进程，通常是因为进程违反了要求或超时。
- [EXC_CRASH](exc_crash.md) — 进程发生崩溃。
- [EXC_CRASH (SIGABRT)](sigabrt.md) — 进程因收到中止信号而终止。
- [EXC_CRASH (SIGKILL)](sigkill.md) — 操作系统终止了进程，通常是因为后台任务违反要求、设备资源受限，或用户强制退出 App。
- [EXC_CRASH (SIGQUIT)](sigquit.md) — 另一个进程终止了该进程，通常是因为该进程违反要求或超时。
- [EXC_CRASH (SIGSYS)](sigsys.md) — 系统调用的错误参数终止了进程。
- [EXC_CRASH (SIGTERM)](sigterm.md) — 软件终止信号终止了进程。
- [EXC_GUARD](exc_guard.md) — 进程违反了受保护资源的防护，通常与文件描述符有关。
- [EXC_RESOURCE](exc_resource.md) — 操作系统停止了进程，因为进程超出了 CPU 时间或内存等资源的消耗限制。
