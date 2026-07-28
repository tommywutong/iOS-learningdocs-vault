---
title: EXC_GUARD
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/exc_guard
source_url: 'https://developer.apple.com/documentation/xcode/exc_guard'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/exc_guard.json'
content_hash: 'sha256:b971fcbb4b4a18c3'
translated: true
---

> 导航： [技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [使用崩溃报告和设备日志诊断问题](diagnosing-issues-using-crash-reports-and-device-logs.md) · [理解崩溃报告中的异常类型](understanding-the-exception-types-in-a-crash-report.md)

# EXC_GUARD

<sub>文章</sub>

进程违反了一项受防护的资源保护，通常与文件描述符有关。

## 概述

受防护的系统资源有多种类型，但大多数受防护资源崩溃都由受防护的文件描述符引起，这类崩溃在 `Exception Subtype` 字段中具有 `GUARD_TYPE_FD` 值。操作系统将文件描述符标记为受防护状态，以确保常规文件描述符 API 无法修改它们。例如，如果某个 App 关闭了用于访问支撑 [Core Data](../coredata.md) 存储的 SQLite 文件的文件描述符，[Core Data](../coredata.md) 可能会在很久之后莫名其妙地崩溃。防护文件描述会在这些问题发生时识别出它们，从而更容易识别和解决。

`Exception Message` 字段包含具体的违规信息：

- **`CLOSE`** — 进程尝试对受防护的文件描述符调用 `close()`。
- **`DUP`** — 进程尝试对受防护的文件描述符调用 `dup()`、`dup2()` 或带有 `F_DUPFD` 或 `F_DUPFD_CLOEXEC` 命令的 `fcntl()`。
- **`NOCLOEXEC`** — 进程尝试从受防护的文件描述符中移除 `FD_CLOEXEC` 标志。
- **`SOCKET_IPC`** — 进程尝试通过套接字发送受防护的文件描述符。
- **`FILEPORT`** — 进程尝试为受防护的文件描述符获取 Mach 发送权限（Mach send right）。
- **`WRITE`** — 进程尝试向受防护的文件描述符执行写入操作。

`Exception Message` 字段还会标识进程尝试修改的特定受防护文件描述符。要了解触发此异常的上下文，请查阅崩溃线程的回溯信息。

## 另请参阅

### 异常

- [EXC_ARITHMETIC](exc_arithmetic.md) — 算术问题导致进程终止，通常是由于除零或浮点错误。
- [EXC_BAD_ACCESS](exc_bad_access.md) — 对内存的错误访问导致进程终止。
- [EXC_BAD_ACCESS (SIGBUS)](sigbus.md) — 总线错误导致进程终止，通常是由于进程尝试访问内存中未对齐或无效的地址，或者由于指针认证（Pointer Authentication）失败。
- [EXC_BAD_ACCESS (SIGSEGV)](sigsegv.md) — 内存分段错误导致进程终止，通常是由于进程尝试访问内存中无效或越界的地址。
- [EXC_BREAKPOINT (SIGTRAP) 和 EXC_BAD_INSTRUCTION (SIGILL)](sigtrap_sigill.md) — 跟踪陷阱或无效的 CPU 指令导致进程中断，通常是由于进程违反了一项要求或超时。
- [EXC_CRASH](exc_crash.md) — 进程崩溃。
- [EXC_CRASH (SIGABRT)](sigabrt.md) — 进程由于收到中止信号而终止。
- [EXC_CRASH (SIGKILL)](sigkill.md) — 操作系统终止了进程，通常是由于某个后台任务（background task）违反了要求、设备资源受限或用户强制退出了 App。
- [EXC_CRASH (SIGQUIT)](sigquit.md) — 另一个进程终止了该进程，通常是由于该进程违反了一项要求或超时。
- [EXC_CRASH (SIGSYS)](sigsys.md) — 对系统调用传入的错误参数导致进程终止。
- [EXC_CRASH (SIGTERM)](sigterm.md) — 软件终止信号导致进程终止。
- [EXC_RESOURCE](exc_resource.md) — 操作系统由于进程超出了资源消耗限制（如 CPU 时间或内存）而停止了该进程。
