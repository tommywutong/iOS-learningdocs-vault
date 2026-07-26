---
title: endIndex
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unsafemutablerawbufferpointer/endindex
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablerawbufferpointer/endindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablerawbufferpointer/endindex.json'
content_hash: 'sha256:8ef27d6c3a4bc04f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableRawBufferPointer](../unsafemutablerawbufferpointer.md)

# endIndex

<sub>Instance Property</sub>

The “past the end” position—that is, the position one greater than the last valid subscript argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var endIndex: UnsafeMutableRawBufferPointer.Index { get }
```

## Discussion

The `endIndex` property of an `UnsafeMutableRawBufferPointer` instance is always identical to `count`.
