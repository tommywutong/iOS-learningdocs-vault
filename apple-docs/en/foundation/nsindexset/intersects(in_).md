---
title: 'intersects(in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsindexset/intersects(in:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsindexset/intersects(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexset/intersects%28in%3A%29.json'
content_hash: 'sha256:edd868b30ca6cf7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSIndexSet](../nsindexset.md)

# intersects(in:)

<sub>Instance Method</sub>

Indicates whether the index set contains any of the indexes in a range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func intersects(in range: NSRange) -> Bool
```

## Parameters

- `range` — Index range being inquired about.

## Return Value

[true](../../swift/true.md) when the index set contains one or more of the indexes in `indexRange`, [false](../../swift/false.md) otherwise.

## See Also

### Querying Index Sets

- [- containsIndex:](<contains(__)-bb19.md>) — Indicates whether the index set contains a specific index.
- [- containsIndexes:](<contains(__)-5j2kh.md>) — Indicates whether the receiving index set contains a superset of the indexes in another index set.
- [- containsIndexesInRange:](<contains(in_).md>) — Indicates whether the index set contains the indexes represented by an index range.
- [count](count.md) — The number of indexes in the index set.
- [- countOfIndexesInRange:](<countofindexes(in_).md>) — Returns the number of indexes in the index set that are members of a given range.
- [- indexPassingTest:](<index(passingtest_).md>) — Returns the index of the first object that passes the predicate Block test.
- [- indexesPassingTest:](<indexes(passingtest_).md>) — Returns an `NSIndexSet` containing the receiving index set’s objects that pass the Block test.
- [- indexWithOptions:passingTest:](<index(options_passingtest_).md>) — Returns the index of the first object that passes the predicate Block test using the specified enumeration options.
- [- indexesWithOptions:passingTest:](<indexes(options_passingtest_).md>) — Returns an `NSIndexSet` containing the receiving index set’s objects that pass the Block test using the specified enumeration options.
- [- indexInRange:options:passingTest:](<index(in_options_passingtest_).md>) — Returns the index of the first object in the specified range that passes the predicate Block test.
- [- indexesInRange:options:passingTest:](<indexes(in_options_passingtest_).md>) — Returns an `NSIndexSet` containing the receiving index set’s objects in the specified range that pass the Block test.
