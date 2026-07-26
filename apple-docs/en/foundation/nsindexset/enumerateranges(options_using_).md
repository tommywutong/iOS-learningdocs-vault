---
title: 'enumerateRanges(options:using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsindexset/enumerateranges(options:using:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsindexset/enumerateranges(options:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexset/enumerateranges%28options%3Ausing%3A%29.json'
content_hash: 'sha256:9f37611259296e00'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSIndexSet](../nsindexset.md)

# enumerateRanges(options:using:)

<sub>Instance Method</sub>

Executes a given block using each object in the index set, in the specified ranges.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func enumerateRanges(options opts: NSEnumerationOptions = [], using block: (NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)
```

## Parameters

- `opts` — A bitmask that specifies the [NSEnumerationOptions](../nsenumerationoptions.md) for the enumeration (whether it should be performed concurrently and whether it should be performed in reverse order).

- `block` — The block to apply to elements in the index set. The block takes two arguments: - **range** — The range of objects of the elements in the index set. - **stop** — A reference to a Boolean value. The block can set the value to [true](../../swift/true.md) to stop further processing of the array. The stop argument is an out-only argument. You should only ever set this Boolean to [true](../../swift/true.md) within the Block.

## Discussion

By default, the enumeration starts with the first object and continues serially through the indexed set range to the last object in the range. You can specify `NSEnumerationConcurrent` and/or `NSEnumerationReverse` as enumeration options to modify this behavior.

This method executes synchronously.

> [!important] Important
> If the Block parameter is `nil` this method will raise an exception.

## See Also

### Enumerating Index Set Content

- [- enumerateRangesInRange:options:usingBlock:](<enumerateranges(in_options_using_).md>) — Enumerates over the ranges in the range of objects using the block
- [- enumerateRangesUsingBlock:](<enumerateranges(__).md>) — Executes a given block using each object in the index set, in the specified ranges.
