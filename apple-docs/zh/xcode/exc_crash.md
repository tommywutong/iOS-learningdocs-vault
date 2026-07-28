---
title: EXC_CRASH
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/exc_crash
source_url: 'https://developer.apple.com/documentation/xcode/exc_crash'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/exc_crash.json'
content_hash: 'sha256:02004b448d1365ae'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [使用崩溃报告和设备日志诊断问题](diagnosing-issues-using-crash-reports-and-device-logs.md) · [了解崩溃报告中的异常类型](understanding-the-exception-types-in-a-crash-report.md)

# EXC_CRASH

<sub>文章</sub>

进程崩溃。

## 概述

有关更具体的信息，请参见与对应信号相关的文章：

- [EXC_CRASH (SIGABRT)](sigabrt.md)
- [EXC_CRASH (SIGKILL)](sigkill.md)
- [EXC_CRASH (SIGQUIT)](sigquit.md)
- [EXC_CRASH (SIGSYS)](sigsys.md)
- [EXC_CRASH (SIGTERM)](sigterm.md)

## 另请参阅

### 异常

- [EXC_ARITHMETIC](exc_arithmetic.md) — 算术问题导致进程终止，通常是因为除以零或浮点错误。
- [EXC_BAD_ACCESS](exc_bad_access.md) — 对内存的错误访问导致进程终止。
- [EXC_BAD_ACCESS (SIGBUS)](sigbus.md) — 总线错误导致进程终止，通常是因为进程尝试访问内存中对齐不正确或无效的地址，或由于指针认证失败。
- [EXC_BAD_ACCESS (SIGSEGV)](sigsegv.md) — 内存分段错误导致进程终止，通常是因为进程尝试访问内存中无效或越界的地址。
- [EXC_BREAKPOINT (SIGTRAP) 与 EXC_BAD_INSTRUCTION (SIGILL)](sigtrap_sigill.md) — 跟踪陷阱或无效的 CPU 指令中断了进程，通常是因为进程违反了某项要求或超时。
- [EXC_CRASH (SIGABRT)](sigabrt.md) — 进程因收到中止信号而终止。
- [EXC_CRASH (SIGKILL)](sigkill.md) — 操作系统终止了进程，通常是因为后台任务违反了要求、设备资源有限或用户强制退出了 App。
- [EXC_CRASH (SIGQUIT)](sigquit.md) — 其他进程终止了该进程，通常是因为进程违反了要求或超时。
- [EXC_CRASH (SIGSYS)](sigsys.md) — 系统调用的错误参数导致进程终止。
- [EXC_CRASH (SIGTERM)](sigterm.md) — 软件终止信号导致进程终止。
- [EXC_GUARD](exc_guard.md) — 进程违反了受保护资源的保护规则，通常与文件描述符相关。
- [EXC_RESOURCE](exc_resource.md) — 操作系统因进程超出了资源消耗限制（如 CPU 时间或内存）而停止了该进程。
