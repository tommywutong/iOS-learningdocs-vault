---
title: makeIterator()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/set/makeiterator()
source_url: 'https://developer.apple.com/documentation/swift/set/makeiterator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/makeiterator%28%29.json'
content_hash: 'sha256:b1137d1276c15a77'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

# makeIterator()

<sub>Instance Method</sub>

Returns an iterator over the members of the set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeIterator() -> Set<Element>.Iterator
```

## See Also

### Iterating over a Set

- [enumerated()](<enumerated().md>) — Returns a sequence of pairs (_n_, _x_), where _n_ represents a consecutive integer starting at zero and _x_ represents an element of the sequence.
- [forEach(_:)](<foreach(__).md>) — Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [underestimatedCount](underestimatedcount.md) — A value less than or equal to the number of elements in the collection.
