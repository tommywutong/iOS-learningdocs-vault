---
title: makeIterator()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsindexset/makeiterator()
source_url: 'https://developer.apple.com/documentation/foundation/nsindexset/makeiterator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexset/makeiterator%28%29.json'
content_hash: 'sha256:c6d93d3a229b9c36'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSIndexSet](../nsindexset.md)

# makeIterator()

<sub>Instance Method</sub>

Returns an _iterator_ over the elements of this _sequence_.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeIterator() -> NSIndexSetIterator
```

## Discussion

Complexity: O(1).

## See Also

### Enumerating Indexes

- [- enumerateIndexesUsingBlock:](<enumerate(__).md>) — Executes a given Block using each object in the index set.
- [- enumerateIndexesWithOptions:usingBlock:](<enumerate(options_using_).md>) — Executes a given Block over the index set’s indexes, using the specified enumeration options.
- [- enumerateIndexesInRange:options:usingBlock:](<enumerate(in_options_using_).md>) — Executes a given Block using the indexes in the specified range, using the specified enumeration options.
- [NSIndexSetIterator](../nsindexsetiterator.md) — An iterator suitable for enumerating the elements of an index set.
