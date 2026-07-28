---
title: EXC_ARITHMETIC
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/exc_arithmetic
source_url: 'https://developer.apple.com/documentation/xcode/exc_arithmetic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/exc_arithmetic.json'
content_hash: 'sha256:f7b52e6c27456c2b'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [使用崩溃报告和设备日志诊断问题](diagnosing-issues-using-crash-reports-and-device-logs.md) · [了解崩溃报告中的异常类型](understanding-the-exception-types-in-a-crash-report.md)

# EXC_ARITHMETIC

<sub>文章</sub>

某个算术问题终止了进程，通常是因为除以零或浮点错误。

## 概述

根据语言和 CPU 架构的不同，除以零和浮点错误也可能产生其他异常。例如，Swift 标准库中的数值类型会检测除以零的情况并产生致命错误（`SIGTRAP` 或 `SIGILL`）。由于在 C 语言中除以零属于未定义行为，它可能产生错误结果而非错误。

## 另请参阅

### 异常

- [EXC_BAD_ACCESS](exc_bad_access.md) — 内存的错误访问终止了进程。
- [EXC_BAD_ACCESS (SIGBUS)](sigbus.md) — 总线错误终止了进程，通常是因为进程尝试访问内存中未对齐或无效的地址，或由于指针认证失败。
- [EXC_BAD_ACCESS (SIGSEGV)](sigsegv.md) — 内存段错误终止了进程，通常是因为进程尝试访问内存中无效或越界的地址。
- [EXC_BREAKPOINT (SIGTRAP) 和 EXC_BAD_INSTRUCTION (SIGILL)](sigtrap_sigill.md) — 跟踪陷阱或无效的 CPU 指令中断了进程，通常是因为进程违反了某个要求或超时。
- [EXC_CRASH](exc_crash.md) — 进程崩溃了。
- [EXC_CRASH (SIGABRT)](sigabrt.md) — 进程因为收到中止信号而终止。
- [EXC_CRASH (SIGKILL)](sigkill.md) — 操作系统终止了进程，通常是因为后台任务（background task）违反了某个要求、设备资源有限或用户强制退出了 App。
- [EXC_CRASH (SIGQUIT)](sigquit.md) — 另一个进程终止了该进程，通常是因为该进程违反了某个要求或超时。
- [EXC_CRASH (SIGSYS)](sigsys.md) — 系统调用的错误参数终止了进程。
- [EXC_CRASH (SIGTERM)](sigterm.md) — 软件终止信号终止了进程。
- [EXC_GUARD](exc_guard.md) — 进程违反了受防护的资源保护，通常与文件描述符相关。
- [EXC_RESOURCE](exc_resource.md) — 操作系统停止了该进程，因为进程超出了资源消耗的限制，如 CPU 时间或内存。
