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
doc_path: '/documentation/swift/indexingiterator/flatmap(_:)-6ahgc'
source_url: 'https://developer.apple.com/documentation/swift/indexingiterator/flatmap(_:)-6ahgc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/indexingiterator/flatmap%28_%3A%29-6ahgc.json'
content_hash: 'sha256:8ed3c76d21871ab1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [IndexingIterator](../indexingiterator.md)

# flatMap(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func flatMap<ElementOfResult>(_ transform: (Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]
```
