---
title: 'enumerate(options:using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsindexset/enumerate(options:using:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsindexset/enumerate(options:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexset/enumerate%28options%3Ausing%3A%29.json'
content_hash: 'sha256:44b86646b006f6eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSIndexSet](../nsindexset.md)

# enumerate(options:using:)

<sub>Instance Method</sub>

Executes a given Block over the index set’s indexes, using the specified enumeration options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func enumerate(options opts: NSEnumerationOptions = [], using block: (Int, UnsafeMutablePointer<ObjCBool>) -> Void)
```

## Parameters

- `opts` — A bitmask that specifies the options for the enumeration (whether it should be performed concurrently and whether it should be performed in reverse order). See [NSEnumerationOptions](../nsenumerationoptions.md) for the supported values.

- `block` — The Block to apply to elements in the set. The Block takes two arguments: - **idx** — The index of the object. - **stop** — A reference to a Boolean value. The block can set the value to [true](../../swift/true.md) to stop further processing of the set. The `stop` argument is an out-only argument. You should only ever set this Boolean to YES within the Block.

## Discussion

This method executes synchronously.

## See Also

### Enumerating Indexes

- [- enumerateIndexesUsingBlock:](<enumerate(__).md>) — Executes a given Block using each object in the index set.
- [- enumerateIndexesInRange:options:usingBlock:](<enumerate(in_options_using_).md>) — Executes a given Block using the indexes in the specified range, using the specified enumeration options.
- [makeIterator()](<makeiterator().md>) — Returns an _iterator_ over the elements of this _sequence_.
- [NSIndexSetIterator](../nsindexsetiterator.md) — An iterator suitable for enumerating the elements of an index set.
