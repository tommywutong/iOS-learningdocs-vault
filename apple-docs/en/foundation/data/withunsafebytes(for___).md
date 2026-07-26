---
title: 'withUnsafeBytes(for:_:)'
framework: Testing
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+, Swift 6.2+, Xcode 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/data/withunsafebytes(for:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/data/withunsafebytes(for:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/withunsafebytes%28for%3A_%3A%29.json'
content_hash: 'sha256:348a912027991d72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# withUnsafeBytes(for:_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withUnsafeBytes<R>(for attachment: borrowing Attachment<Data>, _ body: (UnsafeRawBufferPointer) throws -> R) throws -> R
```
