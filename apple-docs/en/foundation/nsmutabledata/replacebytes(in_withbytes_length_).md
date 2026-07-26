---
title: 'replaceBytes(in:withBytes:length:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutabledata/replacebytes(in:withbytes:length:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutabledata/replacebytes(in:withbytes:length:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutabledata/replacebytes%28in%3Awithbytes%3Alength%3A%29.json'
content_hash: 'sha256:85c6397c81bc2c92'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableData](../nsmutabledata.md)

# replaceBytes(in:withBytes:length:)

<sub>Instance Method</sub>

Replaces with a given set of bytes a given range within the contents of the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replaceBytes(in range: NSRange, withBytes replacementBytes: UnsafeRawPointer?, length replacementLength: Int)
```

## Parameters

- `range` — The range within the receiver’s contents to replace with `bytes`. The range must not exceed the bounds of the receiver.

- `replacementBytes` — The data to insert into the receiver’s contents.

- `replacementLength` — The number of bytes to take from `replacementBytes`.

## Discussion

If the length of `range` is not equal to `replacementLength`, the receiver is resized to accommodate the new bytes. Any bytes past `range` in the receiver are shifted to accommodate the new bytes. You can therefore pass `NULL` for `replacementBytes` and `0` for `replacementLength` to delete bytes in the receiver in the range `range`. You can also replace a range (which might be zero-length) with more bytes than the length of the range, which has the effect of insertion (or “replace some and insert more”).

## See Also

### Modifying Bytes

- [- replaceBytesInRange:withBytes:](<replacebytes(in_withbytes_).md>) — Replaces with a given set of bytes a given range within the contents of the receiver.
- [- resetBytesInRange:](<resetbytes(in_).md>) — Replaces with zeroes the contents of the receiver in a given range.
- [- setData:](<setdata(__).md>) — Replaces the entire contents of the receiver with the contents of another data object.
