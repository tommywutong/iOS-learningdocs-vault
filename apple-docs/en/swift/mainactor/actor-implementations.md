---
title: Actor Implementations
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
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Concurrency](../concurrency.md) · [MainActor](../mainactor.md)

# Actor Implementations

<sub>API Collection</sub>

## Topics

### Instance Methods

- [assertIsolated(_:file:line:)](<assertisolated(__file_line_).md>) — Stops program execution if the current task is not executing on this actor’s serial executor.
- [assumeIsolated(_:file:line:)](<assumeisolated(__file_line_)-swift.method.md>) — Assume that the current task is executing on this actor’s serial executor, or stop program execution otherwise.
- [preconditionIsolated(_:file:line:)](<preconditionisolated(__file_line_).md>) — Stops program execution if the current task is not executing on this actor’s serial executor.
- [withSerialExecutor(_:)](<withserialexecutor(__)-79jll.md>) — Perform an operation with the actor’s [SerialExecutor](../serialexecutor.md).
- [withSerialExecutor(_:)](<withserialexecutor(__)-epjy.md>) — Perform an operation with the actor’s [SerialExecutor](../serialexecutor.md).
