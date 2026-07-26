---
title: 'removeSubranges(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/removesubranges(_:)'
source_url: 'https://developer.apple.com/documentation/swift/string/removesubranges(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/removesubranges%28_%3A%29.json'
content_hash: 'sha256:d6f83961d700e9da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# removeSubranges(_:)

<sub>Instance Method</sub>

Removes the elements at the given indices.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func removeSubranges(_ subranges: RangeSet<Self.Index>)
```

## Parameters

- `subranges` — The indices of the elements to remove.

## Discussion

For example, this code sample finds the indices of all the vowel characters in the string, and then removes those characters.

```swift
var str = "The rain in Spain stays mainly in the plain."
let vowels: Set<Character> = ["a", "e", "i", "o", "u"]
let vowelIndices = str.indices(where: { vowels.contains($0) })

str.removeSubranges(vowelIndices)
// str == "Th rn n Spn stys mnly n th pln."
```

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the collection.
