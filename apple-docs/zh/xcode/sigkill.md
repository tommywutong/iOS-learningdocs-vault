---
title: EXC_CRASH (SIGKILL)
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/sigkill
source_url: 'https://developer.apple.com/documentation/xcode/sigkill'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/sigkill.json'
content_hash: 'sha256:e634d046374b98d2'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Diagnosing issues using crash reports and device logs](diagnosing-issues-using-crash-reports-and-device-logs.md) · [Understanding the exception types in a crash report](understanding-the-exception-types-in-a-crash-report.md)

# EXC_CRASH (SIGKILL)

<sub>文章</sub>

操作系统终止了该进程，通常是因为后台任务违反了某项要求、设备资源有限，或用户强制退出了 App。

## 概述

崩溃报告里包含一个 `Termination Reason` 字段，其中的代码说明了崩溃的原因。在下面的示例中，该代码为 `0xdead10cc`：

```other
Exception Type:  EXC_CRASH (SIGKILL)
Exception Codes: 0x0000000000000000, 0x0000000000000000
Exception Note:  EXC_CORPSE_NOTIFY
Termination Reason: Namespace RUNNINGBOARD, Code 0xdead10cc
```

`Termination Reason` 代码是以下值之一：

- **`0x2182bad2`（`562215634`）**——操作系统因某个后台任务未能及时完成而终止了该 App。
- **`0x2182bad3`（`562215635`）**——操作系统因后台 URL 会话未能及时完成而终止了该 App。
- **`0x2182bad4`（`562215636`）**——操作系统因后台获取未能及时完成而终止了该 App。
- **`0x8badf00d`（`2343432205`）——读作 "ate bad food"**——操作系统的看门狗终止了该 App。参阅[处理看门狗终止](addressing-watchdog-terminations.md)。
- **`0xc00010ff`（`3221229823`）——读作 "cool off"**——操作系统因发生热事件而终止了该 App。这可能是发生崩溃的具体设备的问题，也可能是其运行环境的问题。若想了解让 App 运行更高效的技巧，请观看 WWDC 场次 [iOS Performance and Power Optimization with Instruments](https://developer.apple.com/videos/play/wwdc2011/312/)。若想测试你的 App 对热事件的响应，请按照[在不利的设备条件下测试 (iOS)](https://help.apple.com/xcode/mac/current/#/dev308429d42) 中的说明启用某个设备热状态条件。
- **`0xdead10cc`（`3735883980`）——读作 "dead lock"**——操作系统终止了该 App，因为它在挂起期间持有着文件锁或 SQLite 数据库锁。请使用 [beginBackgroundTask(withName:expirationHandler:)](<../uikit/uiapplication/beginbackgroundtask(withname_expirationhandler_).md>) 在主线程上请求额外的后台执行时间。请务必在开始写入文件之前很早就发出这个请求，以便在 App 挂起之前完成这些操作并释放锁。在 App 扩展中，请使用 [beginActivity(options:reason:)](<../foundation/processinfo/beginactivity(options_reason_).md>) 来管理这项工作。
- **`0xbaadca11`（`3131951633`）——读作 "bad call"**——操作系统因该 App 未能响应 [PushKit](../pushkit.md) 通知报告 [CallKit](../callkit.md) 来电而将其终止。
- **`0xbad22222`（`3134333474`）**——操作系统因某个 VoIP 应用恢复运行过于频繁而将其终止。
- **`0xbaddd15c`（`3135099228`）——读作 "bad disc"**——操作系统为删除缓存、试图回收磁盘空间而终止了该 App。造成磁盘空间不足的因素有很多。你可以通过尽量减少写入磁盘的内容、管理好文件的整个生命周期来提供帮助。
- **`0xc51bad01`（`3306925313`）**——watchOS 因该 App 在执行后台任务时占用了过多 CPU 时间而将其终止。请优化执行该后台任务的代码，使其更节省 CPU，或减少 App 在后台运行期间执行的工作量，以解决此崩溃。
- **`0xc51bad02`（`3306925314`）**——watchOS 因该 App 未能在分配的时间内完成后台任务而将其终止。请减少 App 在后台运行期间执行的工作量，以解决此崩溃。
- **`0xc51bad03`（`3306925315`）**——watchOS 因该 App 未能在分配的时间内完成后台任务而将其终止，但当时系统整体相当繁忙，该 App 可能并未获得多少 CPU 时间来执行后台任务。尽管你或许可以通过减少 App 在后台任务中执行的工作量来避免这个问题，但 `0xc51bad03` 并不表示该 App 做错了什么。更可能的情况是，由于系统整体负载过高，该 App 未能完成其工作。
- **`0xd00d2bad`（`3490524077`）——读作 "dude, too bad"**——操作系统因关键系统资源被过度使用而终止了该 App。你或许可以通过减少并行化、并确保 App 在开始新任务之前完成前序任务的操作来避免这个问题。

## 另请参阅

### Exceptions

- [EXC_ARITHMETIC](exc_arithmetic.md) — 算术问题终止了该进程，通常是因为除以零或浮点数错误。
- [EXC_BAD_ACCESS](exc_bad_access.md) — 错误的内存访问终止了该进程。
- [EXC_BAD_ACCESS (SIGBUS)](sigbus.md) — 总线错误终止了该进程，通常是因为该进程试图访问内存中未对齐或无效的地址，或是由于指针验证失败。
- [EXC_BAD_ACCESS (SIGSEGV)](sigsegv.md) — 内存段错误终止了该进程，通常是因为该进程试图访问内存中无效或越界的地址。
- [EXC_BREAKPOINT (SIGTRAP) and EXC_BAD_INSTRUCTION (SIGILL)](sigtrap_sigill.md) — 跟踪陷阱或无效的 CPU 指令中断了该进程，通常是因为该进程违反了某项要求或超时。
- [EXC_CRASH](exc_crash.md) — 该进程发生了崩溃。
- [EXC_CRASH (SIGABRT)](sigabrt.md) — 该进程因收到中止信号而终止。
- [EXC_CRASH (SIGQUIT)](sigquit.md) — 另一个进程终止了该进程，通常是因为该进程违反了某项要求或超时。
- [EXC_CRASH (SIGSYS)](sigsys.md) — 系统调用的错误参数终止了该进程。
- [EXC_CRASH (SIGTERM)](sigterm.md) — 软件终止信号终止了该进程。
- [EXC_GUARD](exc_guard.md) — 该进程违反了受保护资源的保护机制，通常与文件描述符有关。
- [EXC_RESOURCE](exc_resource.md) — 操作系统因该进程超出了资源消耗限制（如 CPU 时间或内存）而停止了该进程。
