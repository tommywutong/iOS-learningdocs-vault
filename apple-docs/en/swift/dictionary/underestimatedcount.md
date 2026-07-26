---
title: underestimatedCount
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/dictionary/underestimatedcount
source_url: 'https://developer.apple.com/documentation/swift/dictionary/underestimatedcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/underestimatedcount.json'
content_hash: 'sha256:07be1c9b9818d3ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# underestimatedCount

<sub>Instance Property</sub>

A value less than or equal to the number of elements in the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var underestimatedCount: Int { get }
```

## Discussion

> [!abstract] Complexity
> O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(_n_), where _n_ is the length of the collection.

## See Also

### Iterating over Keys and Values

- [forEach(_:)](<foreach(__).md>) — Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [enumerated()](<enumerated().md>) — Returns a sequence of pairs (_n_, _x_), where _n_ represents a consecutive integer starting at zero and _x_ represents an element of the sequence.
- [lazy](lazy.md) — A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
- [makeIterator()](<makeiterator().md>) — Returns an iterator over the dictionary’s key-value pairs.
