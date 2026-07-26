---
title: 'replaceBytes(in:withBytes:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutabledata/replacebytes(in:withbytes:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutabledata/replacebytes(in:withbytes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutabledata/replacebytes%28in%3Awithbytes%3A%29.json'
content_hash: 'sha256:75953f0b22ce1c47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableData](../nsmutabledata.md)

# replaceBytes(in:withBytes:)

<sub>Instance Method</sub>

Replaces with a given set of bytes a given range within the contents of the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replaceBytes(in range: NSRange, withBytes bytes: UnsafeRawPointer)
```

## Parameters

- `range` — The range within the receiver’s contents to replace with `bytes`. The range must not exceed the bounds of the receiver.

- `bytes` — The data to insert into the receiver’s contents.

## Discussion

If the location of `range` isn’t within the receiver’s range of bytes, an `NSRangeException` is raised. The receiver is resized to accommodate the new bytes, if necessary.

A sample using this method is given in [Working With Mutable Binary Data](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/BinaryData/Tasks/WorkingMutableData.html#//apple_ref/doc/uid/20002150).

## See Also

### Modifying Bytes

- [- replaceBytesInRange:withBytes:length:](<replacebytes(in_withbytes_length_).md>) — Replaces with a given set of bytes a given range within the contents of the receiver.
- [- resetBytesInRange:](<resetbytes(in_).md>) — Replaces with zeroes the contents of the receiver in a given range.
- [- setData:](<setdata(__).md>) — Replaces the entire contents of the receiver with the contents of another data object.
