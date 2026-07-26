---
title: lazy
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/dictionary/lazy
source_url: 'https://developer.apple.com/documentation/swift/dictionary/lazy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/lazy.json'
content_hash: 'sha256:3dd0bc1a906afc27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# lazy

<sub>Instance Property</sub>

A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var lazy: LazySequence<Self> { get }
```

## See Also

### Iterating over Keys and Values

- [forEach(_:)](<foreach(__).md>) — Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [enumerated()](<enumerated().md>) — Returns a sequence of pairs (_n_, _x_), where _n_ represents a consecutive integer starting at zero and _x_ represents an element of the sequence.
- [makeIterator()](<makeiterator().md>) — Returns an iterator over the dictionary’s key-value pairs.
- [underestimatedCount](underestimatedcount.md) — A value less than or equal to the number of elements in the collection.
