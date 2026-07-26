---
title: 'getBytes(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（8.0 起废弃）, iPadOS 2.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.10 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsdata/getbytes(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/getbytes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/getbytes%28_%3A%29.json'
content_hash: 'sha256:4a3aab667d162017'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# getBytes(_:)

<sub>Instance Method</sub>

Copies a data object’s contents into a given buffer.

> [!warning] Deprecated
> This method is unsafe because it could potentially cause buffer overruns. Use [- getBytes:length:](<getbytes(__length_).md>) or [- getBytes:range:](<getbytes(__range_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getBytes(_ buffer: UnsafeMutableRawPointer)
```

## Parameters

- `buffer` — A buffer into which to copy the receiver’s data. The buffer must be at least [length](length.md) bytes.

## Discussion

You can see a sample using this method in [Working With Binary Data](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/BinaryData/Tasks/WorkingBinaryData.html#//apple_ref/doc/uid/20000717).

## See Also

### Related Documentation

- [description](description.md) — A string that contains a hexadecimal representation of the data object’s contents in a property list format.

### Accessing Underlying Bytes

- [bytes](bytes.md) — A pointer to the data object’s contents.
- [- enumerateByteRangesUsingBlock:](<enumeratebytes(__).md>) — Enumerates each range of bytes in the data object using a block.
- [- getBytes:length:](<getbytes(__length_).md>) — Copies a number of bytes from the start of the data object into a given buffer.
- [- getBytes:range:](<getbytes(__range_).md>) — Copies a range of bytes from the data object into a given buffer.
