---
title: 'enumerateRanges(in:options:using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsindexset/enumerateranges(in:options:using:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsindexset/enumerateranges(in:options:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexset/enumerateranges%28in%3Aoptions%3Ausing%3A%29.json'
content_hash: 'sha256:d4b77861173d90c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSIndexSet](../nsindexset.md)

# enumerateRanges(in:options:using:)

<sub>Instance Method</sub>

Enumerates over the ranges in the range of objects using the block

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func enumerateRanges(in range: NSRange, options opts: NSEnumerationOptions = [], using block: (NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)
```

## Parameters

- `range` — The range of items to enumerate. If the range intersects a range of the receiver’s indexes, then that intersection will be passed to the block.

- `opts` — A bitmask that specifies the [NSEnumerationOptions](../nsenumerationoptions.md) for the enumeration.

- `block` — The block to apply to elements in the index set. The block takes two arguments: - **range** — The range of elements. - **stop** — A reference to a Boolean value. The block can set the value to [true](../../swift/true.md) to stop further processing of the array. The stop argument is an out-only argument. You should only ever set this Boolean to [true](../../swift/true.md) within the Block.

## Discussion

By default, the enumeration starts with the first object and continues serially through the indexed set range to the last object in the range. You can specify `NSEnumerationConcurrent` and/or `NSEnumerationReverse` as enumeration options to modify this behavior.

This method executes synchronously.

> [!important] Important
> If the Block parameter is `nil` this method will raise an exception.

## See Also

### Enumerating Index Set Content

- [- enumerateRangesUsingBlock:](<enumerateranges(__).md>) — Executes a given block using each object in the index set, in the specified ranges.
- [- enumerateRangesWithOptions:usingBlock:](<enumerateranges(options_using_).md>) — Executes a given block using each object in the index set, in the specified ranges.
