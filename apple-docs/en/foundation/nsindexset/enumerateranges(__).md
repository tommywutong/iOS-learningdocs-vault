---
title: 'enumerateRanges(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsindexset/enumerateranges(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsindexset/enumerateranges(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexset/enumerateranges%28_%3A%29.json'
content_hash: 'sha256:a7b78d62c397bf56'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSIndexSet](../nsindexset.md)

# enumerateRanges(_:)

<sub>Instance Method</sub>

Executes a given block using each object in the index set, in the specified ranges.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func enumerateRanges(_ block: (NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)
```

## Parameters

- `block` — The block to apply to elements in the index set. The block takes two arguments: - **range** — The range of objects of the elements in the index set. - **stop** — A reference to a Boolean value. The block can set the value to [true](../../swift/true.md) to stop further processing of the array. The stop argument is an out-only argument. You should only ever set this Boolean to [true](../../swift/true.md) within the Block.

## Discussion

If the Block parameter is `nil` this method will raise an exception.

This method executes synchronously.

## See Also

### Enumerating Index Set Content

- [- enumerateRangesInRange:options:usingBlock:](<enumerateranges(in_options_using_).md>) — Enumerates over the ranges in the range of objects using the block
- [- enumerateRangesWithOptions:usingBlock:](<enumerateranges(options_using_).md>) — Executes a given block using each object in the index set, in the specified ranges.
