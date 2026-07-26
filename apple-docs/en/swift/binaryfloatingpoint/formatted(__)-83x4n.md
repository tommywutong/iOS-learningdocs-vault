---
title: 'formatted(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/binaryfloatingpoint/formatted(_:)-83x4n'
source_url: 'https://developer.apple.com/documentation/swift/binaryfloatingpoint/formatted(_:)-83x4n'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/binaryfloatingpoint/formatted%28_%3A%29-83x4n.json'
content_hash: 'sha256:74b056b885c84ec0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BinaryFloatingPoint](../binaryfloatingpoint.md)

# formatted(_:)

<sub>Instance Method</sub>

Format `self` with the given format. `self` is first converted to `S.FormatInput` type, then format with the given format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formatted<S>(_ format: S) -> S.FormatOutput where S : FormatStyle, S.FormatInput : BinaryFloatingPoint
```
