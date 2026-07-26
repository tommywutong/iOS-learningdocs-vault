---
title: 'index(of:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+, Swift（5.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/swift/set/index(of:)'
source_url: 'https://developer.apple.com/documentation/swift/set/index(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/index%28of%3A%29.json'
content_hash: 'sha256:3c159c0ccb32084a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

# index(of:)

<sub>Instance Method</sub>

Returns the first index where the specified value appears in the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func index(of element: Self.Element) -> Self.Index?
```

## See Also

### Finding Elements

- [subscript(_:)](<subscript(__).md>) — Accesses the member at the given position.
- [contains(where:)](<contains(where_).md>) — Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [allSatisfy(_:)](<allsatisfy(__).md>) — Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [first(where:)](<first(where_).md>) — Returns the first element of the sequence that satisfies the given predicate.
- [firstIndex(of:)](<firstindex(of_).md>) — Returns the index of the given element in the set, or `nil` if the element is not a member of the set.
- [firstIndex(where:)](<firstindex(where_).md>) — Returns the first index in which an element of the collection satisfies the given predicate.
- [min()](<min().md>) — Returns the minimum element in the sequence.
- [min(by:)](<min(by_).md>) — Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [max()](<max().md>) — Returns the maximum element in the sequence.
- [max(by:)](<max(by_).md>) — Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
