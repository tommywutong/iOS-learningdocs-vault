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
doc_path: '/documentation/swift/ref/init(_:)'
source_url: 'https://developer.apple.com/documentation/swift/ref/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/ref/init%28_%3A%29.json'
content_hash: 'sha256:6e57a68501a21d52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Ref](../ref.md)

# init(_:)

<sub>Initializer</sub>

Initializes an instance of `Ref` with the given borrowed value. This creates a constant reference to that value preventing writes on the original value while this reference is still active.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ value: borrowing Value)
```
