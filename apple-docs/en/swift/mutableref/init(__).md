---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/mutableref/init(_:)'
source_url: 'https://developer.apple.com/documentation/swift/mutableref/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutableref/init%28_%3A%29.json'
content_hash: 'sha256:03d0906a63afaa41'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MutableRef](../mutableref.md)

# init(_:)

<sub>Initializer</sub>

Initializes an instance of `MutableRef` with the given mutable value. This creates a mutable reference to that value preventing writes to the original value while this mutable reference is still active.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ value: inout Value)
```
