---
title: 'increaseLength(by:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutabledata/increaselength(by:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutabledata/increaselength(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutabledata/increaselength%28by%3A%29.json'
content_hash: 'sha256:cb0d07faecbe6c01'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableData](../nsmutabledata.md)

# increaseLength(by:)

<sub>Instance Method</sub>

Increases the length of the receiver by a given number of bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func increaseLength(by extraLength: Int)
```

## Parameters

- `extraLength` — The number of bytes by which to increase the receiver’s length.

## Discussion

The additional bytes are all set to `0`.

> [!important] Important
> Changing the length of a mutable data object invalidates any existing data pointers returned by the [bytes](../nsdata/bytes.md) or [mutableBytes](mutablebytes.md) properties.

## See Also

### Related Documentation

- [length](length.md) — The number of bytes contained in the mutable data object.

### Adding Bytes

- [- appendBytes:length:](<append(__length_).md>) — Appends to the receiver a given number of bytes from a given buffer.
- [- appendData:](<append(__).md>) — Appends the content of another data object to the receiver.
