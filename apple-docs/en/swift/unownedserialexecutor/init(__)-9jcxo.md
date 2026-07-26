---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, tvOS 26.4+, visionOS 26.4+, watchOS 26.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unownedserialexecutor/init(_:)-9jcxo'
source_url: 'https://developer.apple.com/documentation/swift/unownedserialexecutor/init(_:)-9jcxo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unownedserialexecutor/init%28_%3A%29-9jcxo.json'
content_hash: 'sha256:513eb9037c784351'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnownedSerialExecutor](../unownedserialexecutor.md)

# init(_:)

<sub>Initializer</sub>

Automatically opt-in to complex equality semantics if the Executor implements `Equatable`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<E>(_ executor: E) where E : SerialExecutor
```
