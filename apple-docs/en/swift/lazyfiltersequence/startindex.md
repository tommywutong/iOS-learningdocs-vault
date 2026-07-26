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
doc_path: /documentation/swift/lazyfiltersequence/startindex
source_url: 'https://developer.apple.com/documentation/swift/lazyfiltersequence/startindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazyfiltersequence/startindex.json'
content_hash: 'sha256:78ed0c7bbb2e825f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazyFilterSequence](../lazyfiltersequence.md)

# startIndex

<sub>Instance Property</sub>

The position of the first element in a non-empty collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var startIndex: LazyFilterSequence<Base>.Index { get }
```

## Discussion

In an empty collection, `startIndex == endIndex`.

> [!abstract] Complexity
> O(_n_), where _n_ is the ratio between unfiltered and filtered collection counts.
