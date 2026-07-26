---
title: 'withUnsafeBytes(for:_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+, Swift 6.2+, Xcode 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/array/withunsafebytes(for:_:)'
source_url: 'https://developer.apple.com/documentation/swift/array/withunsafebytes(for:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/withunsafebytes%28for%3A_%3A%29.json'
content_hash: 'sha256:33cca73000376b8c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# withUnsafeBytes(for:_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withUnsafeBytes<R>(for attachment: borrowing Attachment<Array<Element>>, _ body: (UnsafeRawBufferPointer) throws -> R) throws -> R
```
