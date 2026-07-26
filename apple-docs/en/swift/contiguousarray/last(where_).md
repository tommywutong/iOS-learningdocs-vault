---
title: 'last(where:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/contiguousarray/last(where:)'
source_url: 'https://developer.apple.com/documentation/swift/contiguousarray/last(where:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/contiguousarray/last%28where%3A%29.json'
content_hash: 'sha256:ef21cafd9e0c8c58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ContiguousArray](../contiguousarray.md)

# last(where:)

<sub>Instance Method</sub>

Returns the last element of the sequence that satisfies the given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func last(where predicate: (Self.Element) throws -> Bool) rethrows -> Self.Element?
```

## Parameters

- `predicate` — A closure that takes an element of the sequence as its argument and returns a Boolean value indicating whether the element is a match.

## Return Value

The last element of the sequence that satisfies `predicate`, or `nil` if there is no element that satisfies `predicate`.

## Discussion

This example uses the `last(where:)` method to find the last negative number in an array of integers:

```swift
let numbers = [3, 7, 4, -2, 9, -6, 10, 1]
if let lastNegative = numbers.last(where: { $0 < 0 }) {
    print("The last negative number is \(lastNegative).")
}
// Prints "The last negative number is -6."
```

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the collection.
