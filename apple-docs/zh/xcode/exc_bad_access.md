---
title: EXC_BAD_ACCESS
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/exc_bad_access
source_url: 'https://developer.apple.com/documentation/xcode/exc_bad_access'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/exc_bad_access.json'
content_hash: 'sha256:d2403fb5551b73b2'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [使用崩溃报告和设备日志诊断问题](diagnosing-issues-using-crash-reports-and-device-logs.md) · [了解崩溃报告中的异常类型](understanding-the-exception-types-in-a-crash-report.md)

# EXC_BAD_ACCESS

<sub>文章</sub>

对内存的错误访问终止了进程。

## 概述

此异常通常伴随 `SIGBUS` 或 `SIGSEGV` 信号；更多信息，请参阅 [EXC_BAD_ACCESS (SIGBUS)](sigbus.md) 或 [EXC_BAD_ACCESS (SIGSEGV)](sigsegv.md)。

## 另请参阅

### 异常

- [EXC_ARITHMETIC](exc_arithmetic.md) — 算术问题终止了进程，通常是因为除零或浮点错误。
- [EXC_BAD_ACCESS (SIGBUS)](sigbus.md) — 总线错误终止了进程，通常是因为进程尝试访问内存中未对齐或无效的地址，或者由于指针认证失败。
- [EXC_BAD_ACCESS (SIGSEGV)](sigsegv.md) — 内存分段错误终止了进程，通常是因为进程尝试访问内存中无效或越界的地址。
- [EXC_BREAKPOINT (SIGTRAP) 和 EXC_BAD_INSTRUCTION (SIGILL)](sigtrap_sigill.md) — 跟踪陷阱或无效的 CPU 指令中断了进程，通常是因为进程违反了某个要求或超时。
- [EXC_CRASH](exc_crash.md) — 进程崩溃。
- [EXC_CRASH (SIGABRT)](sigabrt.md) — 进程因收到中止信号而终止。
- [EXC_CRASH (SIGKILL)](sigkill.md) — 操作系统终止了进程，通常是因为后台任务（background task）违反了某个要求、设备资源受限，或用户强制退出了 App。
- [EXC_CRASH (SIGQUIT)](sigquit.md) — 另一个进程终止了该进程，通常是因为该进程违反了某个要求或超时。
- [EXC_CRASH (SIGSYS)](sigsys.md) — 系统调用的参数错误终止了进程。
- [EXC_CRASH (SIGTERM)](sigterm.md) — 软件终止信号终止了进程。
- [EXC_GUARD](exc_guard.md) — 进程违反了受保护资源的保护，通常与文件描述符相关。
- [EXC_RESOURCE](exc_resource.md) — 操作系统停止了进程，因为进程超过了资源消耗的限制，如 CPU 时间或内存。
