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
doc_path: '/documentation/swift/rangeset/ranges-swift.struct/flatmap(_:)-4laa6'
source_url: 'https://developer.apple.com/documentation/swift/rangeset/ranges-swift.struct/flatmap(_:)-4laa6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangeset/ranges-swift.struct/flatmap%28_%3A%29-4laa6.json'
content_hash: 'sha256:0e2ece3ab6feb290'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [RangeSet](../../rangeset.md) · [Ranges](../ranges-swift.struct.md)

# flatMap(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func flatMap<ElementOfResult>(_ transform: (Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]
```
