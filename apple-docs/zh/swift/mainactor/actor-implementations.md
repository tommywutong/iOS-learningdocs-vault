---
title: Actor 实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/mainactor/actor-implementations
source_url: 'https://developer.apple.com/documentation/swift/mainactor/actor-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mainactor/actor-implementations.json'
content_hash: 'sha256:efcd058388d7ccf0'
translated: true
---

> 导航：[Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Concurrency](../concurrency.md) · [MainActor](../mainactor.md)

# Actor 实现

<sub>API 集合</sub>

## 主题

### 实例方法

- [assertIsolated(_:file:line:)](<assertisolated(__file_line_).md>) — 如果当前任务没有在此 Actor 的串行执行器上执行，则停止程序执行。
- [assumeIsolated(_:file:line:)](<assumeisolated(__file_line_)-swift.method.md>) — 假定当前任务正在此 Actor 的串行执行器上执行，否则停止程序执行。
- [preconditionIsolated(_:file:line:)](<preconditionisolated(__file_line_).md>) — 如果当前任务没有在此 Actor 的串行执行器上执行，则停止程序执行。
- [withSerialExecutor(_:)](<withserialexecutor(__)-79jll.md>) — 使用 Actor 的 [SerialExecutor](../serialexecutor.md) 执行一项操作。
- [withSerialExecutor(_:)](<withserialexecutor(__)-epjy.md>) — 使用 Actor 的 [SerialExecutor](../serialexecutor.md) 执行一项操作。
