---
title: 'getBytes(_:range:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdata/getbytes(_:range:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/getbytes(_:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/getbytes%28_%3Arange%3A%29.json'
content_hash: 'sha256:e2b4c8b606c0e90b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# getBytes(_:range:)

<sub>Instance Method</sub>

Copies a range of bytes from the data object into a given buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getBytes(_ buffer: UnsafeMutableRawPointer, range: NSRange)
```

## Parameters

- `buffer` — A buffer into which to copy data.

- `range` — The range of bytes in the receiver’s data to copy to `buffer`. The range must lie within the range of bytes of the receiver’s data.

## Discussion

If `range` isn’t within the receiver’s range of bytes, an [NSRangeException](../nsexceptionname/rangeexception.md) is raised.

## See Also

### Related Documentation

- [description](description.md) — A string that contains a hexadecimal representation of the data object’s contents in a property list format.

### Accessing Underlying Bytes

- [bytes](bytes.md) — A pointer to the data object’s contents.
- [- enumerateByteRangesUsingBlock:](<enumeratebytes(__).md>) — Enumerates each range of bytes in the data object using a block.
- [- getBytes:](<getbytes(__).md>) — Copies a data object’s contents into a given buffer. _(deprecated)_
- [- getBytes:length:](<getbytes(__length_).md>) — Copies a number of bytes from the start of the data object into a given buffer.
