---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/collectionofone/subscript(_:)-7b34k'
source_url: 'https://developer.apple.com/documentation/swift/collectionofone/subscript(_:)-7b34k'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collectionofone/subscript%28_%3A%29-7b34k.json'
content_hash: 'sha256:b4bee70a8249b083'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [CollectionOfOne](../collectionofone.md)

# subscript(_:)

<sub>Instance Subscript</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript<R>(r: R) -> Self.SubSequence where R : RangeExpression, Self.Index == R.Bound { get set }
```
