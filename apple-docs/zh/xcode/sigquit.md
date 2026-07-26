---
title: EXC_CRASH (SIGQUIT)
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/sigquit
source_url: 'https://developer.apple.com/documentation/xcode/sigquit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/sigquit.json'
content_hash: 'sha256:a42e9ad15cd101da'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Diagnosing issues using crash reports and device logs](diagnosing-issues-using-crash-reports-and-device-logs.md) · [Understanding the exception types in a crash report](understanding-the-exception-types-in-a-crash-report.md)

# EXC_CRASH (SIGQUIT)

<sub>文章</sub>

另一个进程终止了该进程，通常是因为该进程违反了某项要求或超时。

## 概述

该信号表示该进程是应另一个具备管理其生命周期权限的进程的请求而终止的。这并不一定意味着该进程发生了崩溃，但该进程很可能以某种可检测的方式出现了异常行为。对于命令行进程，用户按下 control-\\ 也可能发送这个信号，不过按键绑定可能因 shell 和配置而异。

对于 iOS 和 iPadOS 键盘扩展，如果加载耗时过长，宿主 App 会终止该键盘扩展。虽然看门狗终止时的异常信息有所不同，但排查 `EXC_CRASH (SIGQUIT)` 可以采用[处理看门狗终止](addressing-watchdog-terminations.md)中讨论的相同方法。

## 另请参阅

### Exceptions

- [EXC_ARITHMETIC](exc_arithmetic.md) — 算术问题终止了该进程，通常是因为除以零或浮点数错误。
- [EXC_BAD_ACCESS](exc_bad_access.md) — 错误的内存访问终止了该进程。
- [EXC_BAD_ACCESS (SIGBUS)](sigbus.md) — 总线错误终止了该进程，通常是因为该进程试图访问内存中未对齐或无效的地址，或是由于指针验证失败。
- [EXC_BAD_ACCESS (SIGSEGV)](sigsegv.md) — 内存段错误终止了该进程，通常是因为该进程试图访问内存中无效或越界的地址。
- [EXC_BREAKPOINT (SIGTRAP) and EXC_BAD_INSTRUCTION (SIGILL)](sigtrap_sigill.md) — 跟踪陷阱或无效的 CPU 指令中断了该进程，通常是因为该进程违反了某项要求或超时。
- [EXC_CRASH](exc_crash.md) — 该进程发生了崩溃。
- [EXC_CRASH (SIGABRT)](sigabrt.md) — 该进程因收到中止信号而终止。
- [EXC_CRASH (SIGKILL)](sigkill.md) — 操作系统终止了该进程，通常是因为后台任务违反了某项要求、设备资源有限，或用户强制退出了 App。
- [EXC_CRASH (SIGSYS)](sigsys.md) — 系统调用的错误参数终止了该进程。
- [EXC_CRASH (SIGTERM)](sigterm.md) — 软件终止信号终止了该进程。
- [EXC_GUARD](exc_guard.md) — 该进程违反了受保护资源的保护机制，通常与文件描述符有关。
- [EXC_RESOURCE](exc_resource.md) — 操作系统因该进程超出了资源消耗限制（如 CPU 时间或内存）而停止了该进程。
