---
title: 'getBytes(_:length:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdata/getbytes(_:length:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/getbytes(_:length:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/getbytes%28_%3Alength%3A%29.json'
content_hash: 'sha256:55b48550586fb454'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# getBytes(_:length:)

<sub>Instance Method</sub>

Copies a number of bytes from the start of the data object into a given buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getBytes(_ buffer: UnsafeMutableRawPointer, length: Int)
```

## Parameters

- `buffer` — A buffer into which to copy data.

- `length` — The number of bytes from the start of the receiver’s data to copy to `buffer`.

## Discussion

The number of bytes copied is the smaller of the `length` parameter and the [length](length.md) of the data encapsulated in the object.

## See Also

### Related Documentation

- [description](description.md) — A string that contains a hexadecimal representation of the data object’s contents in a property list format.

### Accessing Underlying Bytes

- [bytes](bytes.md) — A pointer to the data object’s contents.
- [- enumerateByteRangesUsingBlock:](<enumeratebytes(__).md>) — Enumerates each range of bytes in the data object using a block.
- [- getBytes:](<getbytes(__).md>) — Copies a data object’s contents into a given buffer. _(deprecated)_
- [- getBytes:range:](<getbytes(__range_).md>) — Copies a range of bytes from the data object into a given buffer.
