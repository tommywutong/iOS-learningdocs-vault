---
title: 'index(passingTest:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsindexset/index(passingtest:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsindexset/index(passingtest:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexset/index%28passingtest%3A%29.json'
content_hash: 'sha256:03fa0b7c04ba3bd3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSIndexSet](../nsindexset.md)

# index(passingTest:)

<sub>Instance Method</sub>

Returns the index of the first object that passes the predicate Block test.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func index(passingTest predicate: (Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int
```

## Parameters

- `predicate` — The Block to apply to elements in the set. The Block takes two arguments: - **idx** — The index of the object. - **stop** — A reference to a Boolean value. The block can set the value to [true](../../swift/true.md) to stop further processing of the set. The `stop` argument is an out-only argument. You should only ever set this Boolean to YES within the Block. The Block returns a Boolean value that indicates whether `obj` passed the test.

## Return Value

The index of the first object that passes the predicate test.

## See Also

### Querying Index Sets

- [- containsIndex:](<contains(__)-bb19.md>) — Indicates whether the index set contains a specific index.
- [- containsIndexes:](<contains(__)-5j2kh.md>) — Indicates whether the receiving index set contains a superset of the indexes in another index set.
- [- containsIndexesInRange:](<contains(in_).md>) — Indicates whether the index set contains the indexes represented by an index range.
- [- intersectsIndexesInRange:](<intersects(in_).md>) — Indicates whether the index set contains any of the indexes in a range.
- [count](count.md) — The number of indexes in the index set.
- [- countOfIndexesInRange:](<countofindexes(in_).md>) — Returns the number of indexes in the index set that are members of a given range.
- [- indexesPassingTest:](<indexes(passingtest_).md>) — Returns an `NSIndexSet` containing the receiving index set’s objects that pass the Block test.
- [- indexWithOptions:passingTest:](<index(options_passingtest_).md>) — Returns the index of the first object that passes the predicate Block test using the specified enumeration options.
- [- indexesWithOptions:passingTest:](<indexes(options_passingtest_).md>) — Returns an `NSIndexSet` containing the receiving index set’s objects that pass the Block test using the specified enumeration options.
- [- indexInRange:options:passingTest:](<index(in_options_passingtest_).md>) — Returns the index of the first object in the specified range that passes the predicate Block test.
- [- indexesInRange:options:passingTest:](<indexes(in_options_passingtest_).md>) — Returns an `NSIndexSet` containing the receiving index set’s objects in the specified range that pass the Block test.
