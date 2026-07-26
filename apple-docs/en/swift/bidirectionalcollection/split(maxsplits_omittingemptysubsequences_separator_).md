---
title: 'split(maxSplits:omittingEmptySubsequences:separator:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/bidirectionalcollection/split(maxsplits:omittingemptysubsequences:separator:)'
source_url: 'https://developer.apple.com/documentation/swift/bidirectionalcollection/split(maxsplits:omittingemptysubsequences:separator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/bidirectionalcollection/split%28maxsplits%3Aomittingemptysubsequences%3Aseparator%3A%29.json'
content_hash: 'sha256:fb8313d808fedc1d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BidirectionalCollection](../bidirectionalcollection.md)

# split(maxSplits:omittingEmptySubsequences:separator:)

<sub>Instance Method</sub>

Returns the longest possible subsequences of the collection, in order, around subsequence that match the regex created by the given closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func split(maxSplits: Int = Int.max, omittingEmptySubsequences: Bool = true, @RegexComponentBuilder separator: () -> some RegexComponent) -> [Self.SubSequence]
```

## Parameters

- `maxSplits` — The maximum number of times to split the collection, or one less than the number of subsequences to return.

- `omittingEmptySubsequences` — If `false`, an empty subsequence is returned in the result for each consecutive pair of matches and for each match at the start or end of the collection. If `true`, only nonempty subsequences are returned.

- `separator` — A closure that returns a regex to be split upon.

## Return Value

A collection of substrings, split from this collection’s elements.
