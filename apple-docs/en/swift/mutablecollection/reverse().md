---
title: reverse()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/mutablecollection/reverse()
source_url: 'https://developer.apple.com/documentation/swift/mutablecollection/reverse()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablecollection/reverse%28%29.json'
content_hash: 'sha256:1bac3dc8b9b49877'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MutableCollection](../mutablecollection.md)

# reverse()

<sub>Instance Method</sub>

Reverses the elements of the collection in place.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func reverse()
```

## Discussion

The following example reverses the elements of an array of characters:

```swift
var characters: [Character] = ["C", "a", "f", "é"]
characters.reverse()
print(characters)
// Prints "["é", "f", "a", "C"]"
```

> [!abstract] Complexity
> O(_n_), where _n_ is the number of elements in the collection.
