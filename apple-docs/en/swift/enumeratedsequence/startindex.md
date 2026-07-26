---
title: startIndex
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/enumeratedsequence/startindex
source_url: 'https://developer.apple.com/documentation/swift/enumeratedsequence/startindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/enumeratedsequence/startindex.json'
content_hash: 'sha256:a95f7360f399592d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [EnumeratedSequence](../enumeratedsequence.md)

# startIndex

<sub>Instance Property</sub>

The position of the first element in a nonempty collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var startIndex: EnumeratedSequence<Base>.Index { get }
```

## Discussion

If the collection is empty, `startIndex` is equal to `endIndex`.
