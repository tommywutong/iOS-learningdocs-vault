---
title: underestimatedCount
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/sequence/underestimatedcount
source_url: 'https://developer.apple.com/documentation/swift/sequence/underestimatedcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/sequence/underestimatedcount.json'
content_hash: 'sha256:9f82f0aedfb12ffd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Sequence](../sequence.md)

# underestimatedCount

<sub>Instance Property</sub>

A value less than or equal to the number of elements in the sequence, calculated nondestructively.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var underestimatedCount: Int { get }
```

## Discussion

The default implementation returns 0. If you provide your own implementation, make sure to compute the value nondestructively.

> [!abstract] Complexity
> O(1), except if the sequence also conforms to `Collection`. In this case, see the documentation of `Collection.underestimatedCount`.

## Default Implementations

### Sequence Implementations

- [underestimatedCount](underestimatedcount-1uzd0.md) _(beta)_
- [underestimatedCount](underestimatedcount-3n9ne.md) — A value less than or equal to the number of elements in the collection.
- [underestimatedCount](underestimatedcount-8gzwv.md) _(beta)_
- [underestimatedCount](underestimatedcount-9oyup.md) — A value less than or equal to the number of elements in the sequence, calculated nondestructively.

## See Also

### Iterating Over a Sequence’s Elements

- [forEach(_:)](<foreach(__).md>) — Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [enumerated()](<enumerated().md>) — Returns a sequence of pairs (_n_, _x_), where _n_ represents a consecutive integer starting at zero and _x_ represents an element of the sequence.
