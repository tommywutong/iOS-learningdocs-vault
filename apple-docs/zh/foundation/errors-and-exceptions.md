---
title: 错误与异常
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/errors-and-exceptions
source_url: 'https://developer.apple.com/documentation/foundation/errors-and-exceptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/errors-and-exceptions.json'
content_hash: 'sha256:1808293eda5fac18'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md)

# 错误与异常

<sub>API 集合</sub>

响应与 API 交互时出现的问题状况，并微调你的 App 以改善调试体验。

## 主题

### 与用户相关的错误

- [Error](../swift/error.md) — 表示可抛出错误值的类型。
- [NSError](nserror.md) — 有关错误状况的信息，包括域、特定于域的错误码和特定于 App 的信息。
- [LocalizedError](localizederror.md) — 一种特殊错误，可提供描述错误及其发生原因的本地化信息。
- [RecoverableError](recoverableerror.md) — 一种可能恢复的特殊错误，可通过向用户呈现多个潜在恢复选项来恢复。
- [CustomNSError](customnserror.md) — 一种特殊错误，可提供域、错误码和用户信息字典。

### 断言

- [NSAssertionHandler](nsassertionhandler.md) — 将断言记录到控制台的对象。

### 异常

- [NSException](nsexception.md) — 表示中断程序正常执行流程的特殊状况的对象。

### 诊断与调试

- [NSLogv](<nslogv(____).md>) — 将错误信息记录到 Apple System Log 工具。
- [NSLog(_:_:)](<nslog(____).md>) — 将错误信息记录到 Apple System Log 工具。

## 另请参阅

### App 支持

- [任务管理](task-management.md) — 管理 App 的工作，以及它与 Handoff 和快捷指令等系统服务的交互方式。
- [资源](resources.md) — 访问与 App 捆绑在一起的资源和其他数据。
- [通知](notifications.md) — 用于广播信息和订阅广播的设计模式。
- [App 扩展支持](app-extension-support.md) — 管理 App 扩展与托管它的 App 之间的交互。
- [脚本支持](scripting-support.md) — 允许用户通过 AppleScript 和其他自动化技术控制你的 App，或从 App 内运行脚本。
