---
title: 'filter(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/lazymapsequence/iterator/filter(_:)'
source_url: 'https://developer.apple.com/documentation/swift/lazymapsequence/iterator/filter(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazymapsequence/iterator/filter%28_%3A%29.json'
content_hash: 'sha256:fb51c1731ecfe3ef'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [LazyMapSequence](../../lazymapsequence.md) · [Iterator](../iterator.md)

# filter(_:)

<sub>Instance Method</sub>

Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func filter<E>(_ isIncluded: (Self.Element) throws(E) -> Bool) throws(E) -> [Self.Element] where E : Error
```

## Parameters

- `isIncluded` — A closure that takes an element of the sequence as its argument and returns a Boolean value indicating whether the element should be included in the returned array.

## Return Value

An array of the elements that `isIncluded` allowed.

## Discussion

In this example, `filter(_:)` is used to include only names shorter than five characters.

```swift
let cast = ["Vivien", "Marlon", "Kim", "Karl"]
let shortNames = cast.filter { $0.count < 5 }
print(shortNames)
// Prints "["Kim", "Karl"]"
```

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the sequence.
