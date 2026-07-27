---
title: EXC_CRASH (SIGABRT)
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/sigabrt
source_url: 'https://developer.apple.com/documentation/xcode/sigabrt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/sigabrt.json'
content_hash: 'sha256:f126fe41aaa81544'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [使用崩溃报告和设备日志诊断问题](diagnosing-issues-using-crash-reports-and-device-logs.md) · [了解崩溃报告中的异常类型](understanding-the-exception-types-in-a-crash-report.md)

# EXC_CRASH (SIGABRT)

<sub>文章</sub>

进程因收到中止信号而终止。

## 概述

通常，发送 `SIGABRT` 信号是因为进程调用了 `abort()` 函数，例如 App 遇到未捕获的 Objective-C 或 C++ 语言异常时。[处理语言异常崩溃](addressing-language-exception-crashes.md)更详细地说明了如何处理未捕获的语言异常。此信号也可能来自另一个有权管理该进程生命周期的进程；当该进程以可检测的方式出现异常行为时，另一个进程会发送 `SIGABRT`。

如果信号并非因语言异常而发送，请查看崩溃线程的回溯，以确定进程中的代码是否调用了 `abort()`。有关 C 标准库 `abort()` 函数的更多信息，请在“终端”中输入 `man 3 abort` 查看 `abort(3)` 手册页。

如果 App 扩展初始化耗时过长，操作系统会向 App 扩展进程发送 `SIGABRT`。这类崩溃包含值为 `LAUNCH_HANG` 的 `Exception Subtype` 字段。由于扩展没有 `main` 函数，所有初始化耗时都发生在扩展及其依赖库中的静态构造函数和 [load()](<../objectivec/nsobject-swift.class/load().md>) 方法内。虽然看门狗终止的异常信息有所不同，但调查 `LAUNCH_HANG` 时可使用[处理看门狗终止](addressing-watchdog-terminations.md)中讨论的相同技术。

## 另请参阅

### Exceptions

- [EXC_ARITHMETIC](exc_arithmetic.md) — 算术问题终止了进程，通常是因为除以零或浮点错误。
- [EXC_BAD_ACCESS](exc_bad_access.md) — 对内存的错误访问终止了进程。
- [EXC_BAD_ACCESS (SIGBUS)](sigbus.md) — 总线错误终止了进程，通常是因为进程尝试访问内存中未对齐或无效的地址，或因为指针认证失败。
- [EXC_BAD_ACCESS (SIGSEGV)](sigsegv.md) — 内存分段错误终止了进程，通常是因为进程尝试访问内存中无效或越界的地址。
- [EXC_BREAKPOINT (SIGTRAP) and EXC_BAD_INSTRUCTION (SIGILL)](sigtrap_sigill.md) — 跟踪陷阱或无效的 CPU 指令中断了进程，通常是因为进程违反了要求或超时。
- [EXC_CRASH](exc_crash.md) — 进程发生崩溃。
- [EXC_CRASH (SIGKILL)](sigkill.md) — 操作系统终止了进程，通常是因为后台任务违反要求、设备资源受限，或用户强制退出 App。
- [EXC_CRASH (SIGQUIT)](sigquit.md) — 另一个进程终止了该进程，通常是因为该进程违反要求或超时。
- [EXC_CRASH (SIGSYS)](sigsys.md) — 系统调用的错误参数终止了进程。
- [EXC_CRASH (SIGTERM)](sigterm.md) — 软件终止信号终止了进程。
- [EXC_GUARD](exc_guard.md) — 进程违反了受保护资源的防护，通常与文件描述符有关。
- [EXC_RESOURCE](exc_resource.md) — 操作系统停止了进程，因为进程超出了 CPU 时间或内存等资源的消耗限制。
