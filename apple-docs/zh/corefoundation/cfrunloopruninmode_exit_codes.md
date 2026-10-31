---
title: CFRunLoopRunInMode 退出码
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunloopruninmode_exit_codes
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopruninmode_exit_codes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopruninmode_exit_codes.json'
content_hash: 'sha256:230ddb1f9a41bac4'
translated: true
---

> 导航： [技术](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFRunLoop](cfrunloop.md)

# CFRunLoopRunInMode 退出码

<sub>API 集合</sub>

`CFRunLoopRunInMode` 的返回码，用于标识运行循环退出的原因。

## 主题

### 常量

- [kCFRunLoopRunFinished](cfrunlooprunresult/finished.md) — 正在运行的运行循环模式没有需要处理的源或定时器。
- [kCFRunLoopRunStopped](cfrunlooprunresult/stopped.md) — 已对运行循环调用了 [CFRunLoopStop](<cfrunloopstop(__).md>)。
- [kCFRunLoopRunTimedOut](cfrunlooprunresult/timedout.md) — 为运行该运行循环指定的时间间隔已过。
- [kCFRunLoopRunHandledSource](cfrunlooprunresult/handledsource.md) — 已处理完一个源。仅当被告知运行循环只运行到处理完一个源为止时，才会返回此值。

## 另请参阅

### 常量

- [通用模式标志](common-mode-flag.md) — 一个运行循环伪模式，用于管理在“通用”模式下监视的对象。
- [默认运行循环模式](default-run-loop-mode.md) — 默认运行循环模式。
