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
doc_path: /documentation/swift/slice/startindex
source_url: 'https://developer.apple.com/documentation/swift/slice/startindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/slice/startindex.json'
content_hash: 'sha256:59fc6190f38ae2e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Slice](../slice.md)

# startIndex

<sub>Instance Property</sub>

The position of the first element in a nonempty collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var startIndex: Slice<Base>.Index { get }
```

## Discussion

If the collection is empty, `startIndex` is equal to `endIndex`.
