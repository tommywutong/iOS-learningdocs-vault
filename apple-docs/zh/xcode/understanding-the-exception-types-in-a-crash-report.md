---
title: 了解崩溃报告中的异常类型
framework: xcode
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/understanding-the-exception-types-in-a-crash-report
source_url: 'https://developer.apple.com/documentation/xcode/understanding-the-exception-types-in-a-crash-report'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/understanding-the-exception-types-in-a-crash-report.json'
content_hash: 'sha256:acad27cc23dce14e'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [使用崩溃报告和设备日志诊断问题](diagnosing-issues-using-crash-reports-and-device-logs.md)

# 了解崩溃报告中的异常类型

了解异常类型能告诉你哪些有关 App 崩溃原因的信息。

## 概述

崩溃报告中的异常类型描述了 App 的终止方式。它是一项关键信息，可以指导你调查问题的根源。

```other
Exception Type: EXC_BAD_ACCESS (SIGSEGV)
```

崩溃报告会单独记录语言异常信息，其中包括 API 或 Objective-C/C++ 语言功能抛出的异常。

## 主题

### 异常

- [EXC_ARITHMETIC](exc_arithmetic.md) — 算术问题终止了进程，通常是因为除以零或浮点错误。
- [EXC_BAD_ACCESS](exc_bad_access.md) — 错误的内存访问终止了进程。
- [EXC_BAD_ACCESS (SIGBUS)](sigbus.md) — 总线错误终止了进程，通常是因为进程尝试访问内存中未对齐或无效的地址，或者发生了指针认证失败。
- [EXC_BAD_ACCESS (SIGSEGV)](sigsegv.md) — 内存段错误终止了进程，通常是因为进程尝试访问内存中无效或越界的地址。
- [EXC_BREAKPOINT (SIGTRAP) 和 EXC_BAD_INSTRUCTION (SIGILL)](sigtrap_sigill.md) — 跟踪陷阱或无效 CPU 指令中断了进程，通常是因为进程违反了某项要求或发生超时。
- [EXC_CRASH](exc_crash.md) — 进程发生崩溃。
- [EXC_CRASH (SIGABRT)](sigabrt.md) — 进程因收到中止信号而终止。
- [EXC_CRASH (SIGKILL)](sigkill.md) — 操作系统终止了进程，通常是因为后台任务违反了某项要求、设备资源受限，或者用户强制退出了 App。
- [EXC_CRASH (SIGQUIT)](sigquit.md) — 另一个进程终止了该进程，通常是因为该进程违反了某项要求或发生超时。
- [EXC_CRASH (SIGSYS)](sigsys.md) — 向系统调用传入错误参数导致进程终止。
- [EXC_CRASH (SIGTERM)](sigterm.md) — 软件终止信号终止了进程。
- [EXC_GUARD](exc_guard.md) — 进程违反了受保护资源的防护机制，通常与文件描述符有关。
- [EXC_RESOURCE](exc_resource.md) — 操作系统停止了进程，因为进程超过了 CPU 时间或内存等资源的消耗限制。

## 另请参阅

### 崩溃报告

- [为崩溃报告添加可识别的符号名称](adding-identifiable-symbol-names-to-a-crash-report.md) — 用与你 App 代码相对应的函数名和行号替换崩溃报告中的十六进制地址。
- [识别常见崩溃的原因](identifying-the-cause-of-common-crashes.md) — 在崩溃报告中找出能识别常见问题的模式，并根据该模式调查问题。
- [分析崩溃报告](analyzing-a-crash-report.md) — 在崩溃报告中找出有助于你诊断问题的线索。
- [检查崩溃报告中的字段](examining-the-fields-in-a-crash-report.md) — 了解崩溃报告的结构以及每个字段包含的信息。
- [解读崩溃报告的 JSON 格式](interpreting-the-json-format-of-a-crash-report.md) — 了解系统在崩溃报告 JSON 中包含的各个对象的结构和属性。
