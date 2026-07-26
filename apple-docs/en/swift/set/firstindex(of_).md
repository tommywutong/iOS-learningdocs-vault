---
title: 'firstIndex(of:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/set/firstindex(of:)'
source_url: 'https://developer.apple.com/documentation/swift/set/firstindex(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/firstindex%28of%3A%29.json'
content_hash: 'sha256:b60f5573b0dcad34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

# firstIndex(of:)

<sub>Instance Method</sub>

Returns the index of the given element in the set, or `nil` if the element is not a member of the set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func firstIndex(of member: Element) -> Set<Element>.Index?
```

## Parameters

- `member` — An element to search for in the set.

## Return Value

The index of `member` if it exists in the set; otherwise, `nil`.

## Discussion

> [!abstract] Complexity
> O(1)

## See Also

### Finding Elements

- [subscript(_:)](<subscript(__).md>) — Accesses the member at the given position.
- [contains(where:)](<contains(where_).md>) — Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [allSatisfy(_:)](<allsatisfy(__).md>) — Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [first(where:)](<first(where_).md>) — Returns the first element of the sequence that satisfies the given predicate.
- [firstIndex(where:)](<firstindex(where_).md>) — Returns the first index in which an element of the collection satisfies the given predicate.
- [index(of:)](<index(of_).md>) — Returns the first index where the specified value appears in the collection.
- [min()](<min().md>) — Returns the minimum element in the sequence.
- [min(by:)](<min(by_).md>) — Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [max()](<max().md>) — Returns the maximum element in the sequence.
- [max(by:)](<max(by_).md>) — Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
