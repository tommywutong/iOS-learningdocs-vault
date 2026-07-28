---
title: EXC_RESOURCE
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/exc_resource
source_url: 'https://developer.apple.com/documentation/xcode/exc_resource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/exc_resource.json'
content_hash: 'sha256:dba7d8af3a0f11f2'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [使用崩溃报告和设备日志诊断问题](diagnosing-issues-using-crash-reports-and-device-logs.md) · [了解崩溃报告中的异常类型](understanding-the-exception-types-in-a-crash-report.md)

# EXC_RESOURCE

<sub>文章</sub>

操作系统停止了进程，原因是该进程超出了资源消耗限制，例如 CPU 时间或内存。

## 概述

如果 `Exception Note` 字段包含 `NON-FATAL CONDITION`，则表示操作系统生成了崩溃报告，但并未实际终止进程。`Exception Message` 字段描述了在特定时间间隔内消耗的资源量。

崩溃报告在 `Exception Subtype` 字段中列出了具体的资源：

- **`CPU` 和 `CPU_FATAL`**——进程中的某个线程在短时间内使用了过多的 CPU 资源。
- **`MEMORY`**——进程超出了系统施加的内存限制。这可能是因内存使用过多而导致终止的先兆。
- **`IO`**——进程在短时间内导致了过多的磁盘写入。
- **`WAKEUPS`**——进程中的线程每秒唤醒次数过多，这会导致电池续航下降。

过度唤醒可能来自于调用线程间通信 API 的频率过高；这些 API 包括 [perform(_:on:with:waitUntilDone:)](<../objectivec/nsobject-swift.class/perform(__on_with_waituntildone_).md>)、[async(execute:)](<../dispatch/dispatchqueue/async(execute_).md>) 和 [dispatch_async](../dispatch/dispatch_async.md)。由于触发此异常的通信发生得过于频繁，崩溃报告中通常会包含多个具有非常相似回溯（backtrace）的后台线程，这些回溯指示了线程通信的根源。请参阅 [Modernizing Grand Central Dispatch Usage](https://developer.apple.com/videos/play/wwdc2017/706/) 了解如何更高效地管理并发工作负载。

## 另请参阅

### 异常

- [EXC_ARITHMETIC](exc_arithmetic.md)——算术问题导致进程终止，通常由除零或浮点数错误引起。
- [EXC_BAD_ACCESS](exc_bad_access.md)——对内存的错误访问导致进程终止。
- [EXC_BAD_ACCESS (SIGBUS)](sigbus.md)——总线错误导致进程终止，通常是因为进程试图访问内存中未对齐或无效的地址，或由于指针认证（pointer authentication）失败。
- [EXC_BAD_ACCESS (SIGSEGV)](sigsegv.md)——内存段错误导致进程终止，通常是因为进程试图访问内存中无效或越界的地址。
- [EXC_BREAKPOINT (SIGTRAP) 和 EXC_BAD_INSTRUCTION (SIGILL)](sigtrap_sigill.md)——跟踪陷阱或无效 CPU 指令中断了进程，通常是因为进程违反了要求或超时。
- [EXC_CRASH](exc_crash.md)——进程崩溃。
- [EXC_CRASH (SIGABRT)](sigabrt.md)——进程因收到中止信号而终止。
- [EXC_CRASH (SIGKILL)](sigkill.md)——操作系统终止了进程，通常是因为后台任务（background task）违反了要求、设备资源受限或用户强制退出了 App。
- [EXC_CRASH (SIGQUIT)](sigquit.md)——其他进程终止了该进程，通常是因为此进程违反了要求或超时。
- [EXC_CRASH (SIGSYS)](sigsys.md)——系统调用的参数错误导致进程终止。
- [EXC_CRASH (SIGTERM)](sigterm.md)——软件终止信号导致进程终止。
- [EXC_GUARD](exc_guard.md)——进程违反了受保护的资源保护机制，通常与文件描述符（file descriptor）相关。
