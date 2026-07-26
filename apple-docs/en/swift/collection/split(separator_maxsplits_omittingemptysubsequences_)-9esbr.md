---
title: 'split(separator:maxSplits:omittingEmptySubsequences:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/collection/split(separator:maxsplits:omittingemptysubsequences:)-9esbr'
source_url: 'https://developer.apple.com/documentation/swift/collection/split(separator:maxsplits:omittingemptysubsequences:)-9esbr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collection/split%28separator%3Amaxsplits%3Aomittingemptysubsequences%3A%29-9esbr.json'
content_hash: 'sha256:8a71a81e7ae2e3ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Collection](../collection.md)

# split(separator:maxSplits:omittingEmptySubsequences:)

<sub>Instance Method</sub>

Returns the longest possible subsequences of the collection, in order, around elements equal to the given separator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func split<C>(separator: C, maxSplits: Int = .max, omittingEmptySubsequences: Bool = true) -> [Self.SubSequence] where C : Collection, Self.Element == C.Element
```

## Parameters

- `separator` — The element to be split upon.

## Return Value

A collection of subsequences, split from this collection’s elements.

## See Also

### Splitting and Joining Elements

- [split(separator:maxSplits:omittingEmptySubsequences:)](<split(separator_maxsplits_omittingemptysubsequences_)-6c22.md>) — Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [split(maxSplits:omittingEmptySubsequences:whereSeparator:)](<split(maxsplits_omittingemptysubsequences_whereseparator_).md>) — Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
