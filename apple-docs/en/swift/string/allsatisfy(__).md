---
title: 'allSatisfy(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/allsatisfy(_:)'
source_url: 'https://developer.apple.com/documentation/swift/string/allsatisfy(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/allsatisfy%28_%3A%29.json'
content_hash: 'sha256:d054ee9d3264101f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# allSatisfy(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func allSatisfy(_ predicate: (Self.Element) throws -> Bool) rethrows -> Bool
```

## Parameters

- `predicate` — A closure that takes an element of the sequence as its argument and returns a Boolean value that indicates whether the passed element satisfies a condition.

## Return Value

`true` if the sequence contains only elements that satisfy `predicate`; otherwise, `false`.

## Discussion

The following code uses this method to test whether all the names in an array have at least five characters:

```swift
let names = ["Sofia", "Camilla", "Martina", "Mateo", "Nicolás"]
let allHaveAtLeastFive = names.allSatisfy({ $0.count >= 5 })
// allHaveAtLeastFive == true
```

If the sequence is empty, this method returns `true`.

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the sequence.

## See Also

### Finding Characters

- [contains(_:)](<contains(__).md>) — Returns a Boolean value indicating whether the sequence contains the given element.
- [contains(where:)](<contains(where_).md>) — Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [first(where:)](<first(where_).md>) — Returns the first element of the sequence that satisfies the given predicate.
- [firstIndex(of:)](<firstindex(of_).md>) — Returns the first index where the specified value appears in the collection.
- [firstIndex(where:)](<firstindex(where_).md>) — Returns the first index in which an element of the collection satisfies the given predicate.
- [last(where:)](<last(where_).md>) — Returns the last element of the sequence that satisfies the given predicate.
- [lastIndex(of:)](<lastindex(of_).md>) — Returns the last index where the specified value appears in the collection.
- [lastIndex(where:)](<lastindex(where_).md>) — Returns the index of the last element in the collection that matches the given predicate.
- [max()](<max().md>) — Returns the maximum element in the sequence.
- [max(_:_:)](<max(____).md>)
- [max(by:)](<max(by_).md>) — Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [min()](<min().md>) — Returns the minimum element in the sequence.
- [min(_:_:)](<min(____).md>)
- [min(by:)](<min(by_).md>) — Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
