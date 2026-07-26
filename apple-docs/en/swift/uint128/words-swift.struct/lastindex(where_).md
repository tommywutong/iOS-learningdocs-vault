---
title: 'lastIndex(where:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/uint128/words-swift.struct/lastindex(where:)'
source_url: 'https://developer.apple.com/documentation/swift/uint128/words-swift.struct/lastindex(where:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint128/words-swift.struct/lastindex%28where%3A%29.json'
content_hash: 'sha256:1be773929b614ab3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [UInt128](../../uint128.md) · [Words](../words-swift.struct.md)

# lastIndex(where:)

<sub>Instance Method</sub>

Returns the index of the last element in the collection that matches the given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func lastIndex(where predicate: (Self.Element) throws -> Bool) rethrows -> Self.Index?
```

## Parameters

- `predicate` — A closure that takes an element as its argument and returns a Boolean value that indicates whether the passed element represents a match.

## Return Value

The index of the last element in the collection that matches `predicate`, or `nil` if no elements match.

## Discussion

You can use the predicate to find an element of a type that doesn’t conform to the `Equatable` protocol or to find an element that matches particular criteria. This example finds the index of the last name that begins with the letter _A:_

```swift
let students = ["Kofi", "Abena", "Peter", "Kweku", "Akosua"]
if let i = students.lastIndex(where: { $0.hasPrefix("A") }) {
    print("\(students[i]) starts with 'A'!")
}
// Prints "Akosua starts with 'A'!"
```

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the collection.
