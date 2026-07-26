---
title: UnsafeBufferPointer.Index
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unsafebufferpointer/index
source_url: 'https://developer.apple.com/documentation/swift/unsafebufferpointer/index'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafebufferpointer/index.json'
content_hash: 'sha256:22927bfcad8d614f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeBufferPointer](../unsafebufferpointer.md)

# UnsafeBufferPointer.Index

<sub>Type Alias</sub>

A type that represents a position in the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Index = Int
```

## Discussion

Valid indices consist of the position of every element and a “past the end” position that’s not valid for use as a subscript argument.
