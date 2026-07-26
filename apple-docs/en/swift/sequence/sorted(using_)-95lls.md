---
title: 'sorted(using:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/sequence/sorted(using:)-95lls'
source_url: 'https://developer.apple.com/documentation/swift/sequence/sorted(using:)-95lls'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/sequence/sorted%28using%3A%29-95lls.json'
content_hash: 'sha256:ae430571e7015257'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Sequence](../sequence.md)

# sorted(using:)

<sub>Instance Method</sub>

Returns the elements of the sequence, sorted using the given comparator to compare elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sorted<Comparator>(using comparator: Comparator) -> [Self.Element] where Comparator : SortComparator, Self.Element == Comparator.Compared
```

## Parameters

- `comparator` — The comparator to use in ordering elements

## Return Value

An array of the elements sorted using `comparator`.
