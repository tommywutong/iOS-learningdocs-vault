---
title: 'flatMap(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+, Swift（4.1 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swift/stridethrough/flatmap(_:)-1er06'
source_url: 'https://developer.apple.com/documentation/swift/stridethrough/flatmap(_:)-1er06'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stridethrough/flatmap%28_%3A%29-1er06.json'
content_hash: 'sha256:bc2735ad5df500dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StrideThrough](../stridethrough.md)

# flatMap(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func flatMap<ElementOfResult>(_ transform: (Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]
```
