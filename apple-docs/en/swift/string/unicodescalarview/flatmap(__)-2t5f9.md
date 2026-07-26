---
title: 'flatMap(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+, Swift（4.1 起废弃）]
languages: [swift, swift, swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/swift/string/unicodescalarview/flatmap(_:)-2t5f9'
source_url: 'https://developer.apple.com/documentation/swift/string/unicodescalarview/flatmap(_:)-2t5f9'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/unicodescalarview/flatmap%28_%3A%29-2t5f9.json'
content_hash: 'sha256:fe9ebca1f9715af3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [UnicodeScalarView](../unicodescalarview.md)

# flatMap(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func flatMap<ElementOfResult>(_ transform: (Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]
```
