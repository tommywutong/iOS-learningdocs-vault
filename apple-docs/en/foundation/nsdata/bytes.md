---
title: bytes
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdata/bytes
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/bytes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/bytes.json'
content_hash: 'sha256:589cd2d82740da03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# bytes

<sub>Instance Property</sub>

A pointer to the data object’s contents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var bytes: UnsafeRawPointer { get }
```

## Discussion

If the [length](length.md) of the [NSData](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/OldStylePlists/OldStylePLists.html#//apple_ref/doc/uid/20001012-47169) object is 0, this property returns `nil`.

For an immutable data object, the returned pointer is valid until the data object is deallocated. For a mutable data object, the returned pointer is valid until the data object is deallocated or the data is mutated.

## See Also

### Related Documentation

- [description](description.md) — A string that contains a hexadecimal representation of the data object’s contents in a property list format.

### Accessing Underlying Bytes

- [- enumerateByteRangesUsingBlock:](<enumeratebytes(__).md>) — Enumerates each range of bytes in the data object using a block.
- [- getBytes:](<getbytes(__).md>) — Copies a data object’s contents into a given buffer. _(deprecated)_
- [- getBytes:length:](<getbytes(__length_).md>) — Copies a number of bytes from the start of the data object into a given buffer.
- [- getBytes:range:](<getbytes(__range_).md>) — Copies a range of bytes from the data object into a given buffer.
