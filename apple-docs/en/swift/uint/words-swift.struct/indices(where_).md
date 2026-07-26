---
title: 'indices(where:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/uint/words-swift.struct/indices(where:)'
source_url: 'https://developer.apple.com/documentation/swift/uint/words-swift.struct/indices(where:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint/words-swift.struct/indices%28where%3A%29.json'
content_hash: 'sha256:f8f1c22baf5f559e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [UInt](../../uint.md) · [Words](../words-swift.struct.md)

# indices(where:)

<sub>Instance Method</sub>

Returns the indices of all the elements that match the given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func indices(where predicate: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>
```

## Parameters

- `predicate` — A closure that takes an element as its argument and returns a Boolean value that indicates whether the passed element represents a match.

## Return Value

A set of the indices of the elements for which `predicate` returns `true`.

## Discussion

For example, you can use this method to find all the places that a vowel occurs in a string.

```swift
let str = "Fresh cheese in a breeze"
let vowels: Set<Character> = ["a", "e", "i", "o", "u"]
let allTheVowels = str.indices(where: { vowels.contains($0) })
// str[allTheVowels].count == 9
```

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the collection.
