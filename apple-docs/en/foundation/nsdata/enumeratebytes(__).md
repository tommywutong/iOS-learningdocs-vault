---
title: 'enumerateBytes(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdata/enumeratebytes(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/enumeratebytes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/enumeratebytes%28_%3A%29.json'
content_hash: 'sha256:6bd6bc7ee203c334'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# enumerateBytes(_:)

<sub>Instance Method</sub>

Enumerates each range of bytes in the data object using a block.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func enumerateBytes(_ block: (UnsafeRawPointer, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)
```

## Parameters

- `block` — The block to apply to byte ranges in the array. The block takes three arguments: - **bytes** — The bytes for the current range. This pointer is valid until the data object is deallocated. - **byteRange** — The range of the current data bytes. - **stop** — A reference to a Boolean value. The block can set the value to [true](../../swift/true.md) to stop further processing of the data. The stop argument is an out-only argument. You should only ever set this Boolean to [true](../../swift/true.md) within the Block.

## Discussion

The enumeration block is called once for each contiguous region of memory in the receiver (once total for a contiguous [NSData](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/OldStylePlists/OldStylePLists.html#//apple_ref/doc/uid/20001012-47169) object), until either all bytes have been enumerated, or the `stop` parameter is set to [true](../../swift/true.md).

## See Also

### Accessing Underlying Bytes

- [bytes](bytes.md) — A pointer to the data object’s contents.
- [- getBytes:](<getbytes(__).md>) — Copies a data object’s contents into a given buffer. _(deprecated)_
- [- getBytes:length:](<getbytes(__length_).md>) — Copies a number of bytes from the start of the data object into a given buffer.
- [- getBytes:range:](<getbytes(__range_).md>) — Copies a range of bytes from the data object into a given buffer.
