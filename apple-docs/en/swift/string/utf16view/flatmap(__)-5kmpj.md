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
doc_path: '/documentation/swift/string/utf16view/flatmap(_:)-5kmpj'
source_url: 'https://developer.apple.com/documentation/swift/string/utf16view/flatmap(_:)-5kmpj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/utf16view/flatmap%28_%3A%29-5kmpj.json'
content_hash: 'sha256:e3bc4db83626cfad'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [UTF16View](../utf16view.md)

# flatMap(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func flatMap<ElementOfResult>(_ transform: (Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]
```
