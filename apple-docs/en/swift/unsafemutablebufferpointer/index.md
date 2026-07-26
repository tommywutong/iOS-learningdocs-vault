---
title: UnsafeMutableBufferPointer.Index
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unsafemutablebufferpointer/index
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/index'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablebufferpointer/index.json'
content_hash: 'sha256:d8bf37b195c0670b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableBufferPointer](../unsafemutablebufferpointer.md)

# UnsafeMutableBufferPointer.Index

<sub>Type Alias</sub>

A type that represents a position in the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Index = Int
```

## Discussion

Valid indices consist of the position of every element and a “past the end” position that’s not valid for use as a subscript argument.
