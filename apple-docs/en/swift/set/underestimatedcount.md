---
title: underestimatedCount
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/set/underestimatedcount
source_url: 'https://developer.apple.com/documentation/swift/set/underestimatedcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/underestimatedcount.json'
content_hash: 'sha256:b15fe8048c21d183'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

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

### Iterating over a Set

- [enumerated()](<enumerated().md>) — Returns a sequence of pairs (_n_, _x_), where _n_ represents a consecutive integer starting at zero and _x_ represents an element of the sequence.
- [forEach(_:)](<foreach(__).md>) — Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [makeIterator()](<makeiterator().md>) — Returns an iterator over the members of the set.
