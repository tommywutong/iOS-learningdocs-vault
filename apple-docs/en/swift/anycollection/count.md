---
title: count
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/anycollection/count
source_url: 'https://developer.apple.com/documentation/swift/anycollection/count'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anycollection/count.json'
content_hash: 'sha256:56490ec2f07459d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AnyCollection](../anycollection.md)

# count

<sub>Instance Property</sub>

The number of elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var count: Int { get }
```

## Discussion

To check whether a collection is empty, use its `isEmpty` property instead of comparing `count` to zero. Calculating `count` can be an O(_n_) operation.

> [!abstract] Complexity
> O(_n_)
