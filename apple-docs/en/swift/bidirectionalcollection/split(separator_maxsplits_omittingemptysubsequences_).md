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
doc_path: '/documentation/swift/bidirectionalcollection/split(separator:maxsplits:omittingemptysubsequences:)'
source_url: 'https://developer.apple.com/documentation/swift/bidirectionalcollection/split(separator:maxsplits:omittingemptysubsequences:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/bidirectionalcollection/split%28separator%3Amaxsplits%3Aomittingemptysubsequences%3A%29.json'
content_hash: 'sha256:e32596a436371e52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BidirectionalCollection](../bidirectionalcollection.md)

# split(separator:maxSplits:omittingEmptySubsequences:)

<sub>Instance Method</sub>

Returns the longest possible subsequences of the collection, in order, around elements equal to the given separator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func split(separator: some RegexComponent, maxSplits: Int = .max, omittingEmptySubsequences: Bool = true) -> [Self.SubSequence]
```

## Parameters

- `separator` — A regex describing elements to be split upon.

## Return Value

A collection of substrings, split from this collection’s elements.
