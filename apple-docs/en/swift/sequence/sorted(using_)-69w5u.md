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
doc_path: '/documentation/swift/sequence/sorted(using:)-69w5u'
source_url: 'https://developer.apple.com/documentation/swift/sequence/sorted(using:)-69w5u'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/sequence/sorted%28using%3A%29-69w5u.json'
content_hash: 'sha256:33c258c0ffe6a45b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Sequence](../sequence.md)

# sorted(using:)

<sub>Instance Method</sub>

Returns the elements of the sequence, sorted using the given array of `SortComparator`s to compare elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sorted<S, Comparator>(using comparators: S) -> [Self.Element] where S : Sequence, Comparator : SortComparator, Comparator == S.Element, Self.Element == Comparator.Compared
```

## Parameters

- `comparators` — An array of comparators used to compare elements. The first comparator specifies the primary comparator to be used in sorting the sequence’s elements. Any subsequent comparators are used to further refine the order of elements with equal values.

## Return Value

An array of the elements sorted using `comparators`.
