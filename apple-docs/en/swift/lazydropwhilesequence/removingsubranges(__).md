---
title: 'removingSubranges(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/lazydropwhilesequence/removingsubranges(_:)'
source_url: 'https://developer.apple.com/documentation/swift/lazydropwhilesequence/removingsubranges(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazydropwhilesequence/removingsubranges%28_%3A%29.json'
content_hash: 'sha256:997ca0b0712d315c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazyDropWhileSequence](../lazydropwhilesequence.md)

# removingSubranges(_:)

<sub>Instance Method</sub>

Returns a collection of the elements in this collection that are not represented by the given range set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removingSubranges(_ subranges: RangeSet<Self.Index>) -> DiscontiguousSlice<Self>
```

## Parameters

- `subranges` — A range set representing the indices of the elements to remove.

## Return Value

A collection of the elements that are not in `subranges`.

## Discussion

For example, this code sample finds the indices of all the vowel characters in the string, and then retrieves a collection that omits those characters.

```swift
let str = "The rain in Spain stays mainly in the plain."
let vowels: Set<Character> = ["a", "e", "i", "o", "u"]
let vowelIndices = str.indices(where: { vowels.contains($0) })

let disemvoweled = str.removingSubranges(vowelIndices)
print(String(disemvoweled))
// Prints "Th rn n Spn stys mnly n th pln."
```

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the collection.
