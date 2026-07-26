---
title: 'removeAll(where:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/arrayslice/removeall(where:)-10tcx'
source_url: 'https://developer.apple.com/documentation/swift/arrayslice/removeall(where:)-10tcx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/arrayslice/removeall%28where%3A%29-10tcx.json'
content_hash: 'sha256:ba1037c0b53fec59'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ArraySlice](../arrayslice.md)

# removeAll(where:)

<sub>Instance Method</sub>

Removes all the elements that satisfy the given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func removeAll(where shouldBeRemoved: (Self.Element) throws -> Bool) rethrows
```

## Parameters

- `shouldBeRemoved` — A closure that takes an element of the sequence as its argument and returns a Boolean value indicating whether the element should be removed from the collection.

## Discussion

Use this method to remove every element in a collection that meets particular criteria. The order of the remaining elements is preserved. This example removes all the vowels from a string:

```swift
var phrase = "The rain in Spain stays mainly in the plain."

let vowels: Set<Character> = ["a", "e", "i", "o", "u"]
phrase.removeAll(where: { vowels.contains($0) })
// phrase == "Th rn n Spn stys mnly n th pln."
```

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the collection.
