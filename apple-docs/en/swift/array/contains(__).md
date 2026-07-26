---
title: 'contains(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/array/contains(_:)'
source_url: 'https://developer.apple.com/documentation/swift/array/contains(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/contains%28_%3A%29.json'
content_hash: 'sha256:c33c5567e39026b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# contains(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the sequence contains the given element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains(_ element: Self.Element) -> Bool
```

## Parameters

- `element` — The element to find in the sequence.

## Return Value

`true` if the element was found in the sequence; otherwise, `false`.

## Discussion

This example checks to see whether a favorite actor is in an array storing a movie’s cast.

```swift
let cast = ["Vivien", "Marlon", "Kim", "Karl"]
print(cast.contains("Marlon"))
// Prints "true"
print(cast.contains("James"))
// Prints "false"
```

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the sequence.

## See Also

### Finding Elements

- [contains(where:)](<contains(where_).md>) — Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [allSatisfy(_:)](<allsatisfy(__).md>) — Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [first(where:)](<first(where_).md>) — Returns the first element of the sequence that satisfies the given predicate.
- [firstIndex(of:)](<firstindex(of_).md>) — Returns the first index where the specified value appears in the collection.
- [index(of:)](<index(of_).md>) — Returns the first index where the specified value appears in the collection.
- [firstIndex(where:)](<firstindex(where_).md>) — Returns the first index in which an element of the collection satisfies the given predicate.
- [last(where:)](<last(where_).md>) — Returns the last element of the sequence that satisfies the given predicate.
- [lastIndex(of:)](<lastindex(of_).md>) — Returns the last index where the specified value appears in the collection.
- [lastIndex(where:)](<lastindex(where_).md>) — Returns the index of the last element in the collection that matches the given predicate.
- [min()](<min().md>) — Returns the minimum element in the sequence.
- [min(by:)](<min(by_).md>) — Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [max()](<max().md>) — Returns the maximum element in the sequence.
- [max(by:)](<max(by_).md>) — Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
