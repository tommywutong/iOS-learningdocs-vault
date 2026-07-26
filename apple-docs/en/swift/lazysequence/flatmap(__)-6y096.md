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
doc_path: '/documentation/swift/lazysequence/flatmap(_:)-6y096'
source_url: 'https://developer.apple.com/documentation/swift/lazysequence/flatmap(_:)-6y096'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazysequence/flatmap%28_%3A%29-6y096.json'
content_hash: 'sha256:0098a186dbe3c281'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazySequence](../lazysequence.md)

# flatMap(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func flatMap<ElementOfResult>(_ transform: (Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]
```
