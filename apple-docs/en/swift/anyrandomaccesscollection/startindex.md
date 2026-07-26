---
title: startIndex
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/anyrandomaccesscollection/startindex
source_url: 'https://developer.apple.com/documentation/swift/anyrandomaccesscollection/startindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anyrandomaccesscollection/startindex.json'
content_hash: 'sha256:3072978c7747d5fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AnyRandomAccessCollection](../anyrandomaccesscollection.md)

# startIndex

<sub>Instance Property</sub>

The position of the first element in a non-empty collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var startIndex: AnyRandomAccessCollection<Element>.Index { get }
```

## Discussion

In an empty collection, `startIndex == endIndex`.
