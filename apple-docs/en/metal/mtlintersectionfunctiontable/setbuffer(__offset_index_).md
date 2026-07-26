---
title: 'setBuffer(_:offset:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlintersectionfunctiontable/setbuffer(_:offset:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlintersectionfunctiontable/setbuffer(_:offset:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlintersectionfunctiontable/setbuffer%28_%3Aoffset%3Aindex%3A%29.json'
content_hash: 'sha256:92569dcef2ac0328'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIntersectionFunctionTable](../mtlintersectionfunctiontable.md)

# setBuffer(_:offset:index:)

<sub>Instance Method</sub>

Sets a buffer for the intersection functions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setBuffer(_ buffer: (any MTLBuffer)?, offset: Int, index: Int)
```

## Parameters

- `buffer` — The [MTLBuffer](../mtlbuffer.md) object to set in the argument table.

- `offset` — Where the data begins, in bytes, from the start of the buffer.

- `index` — An index in the function table’s buffer argument table.

## See Also

### Specifying arguments for intersection functions

- [setBuffers(_:offsets:range:)](<setbuffers(__offsets_range_).md>) — Sets a range of buffers for the intersection functions.
- [- setVisibleFunctionTable:atBufferIndex:](<setvisiblefunctiontable(__bufferindex_).md>) — Sets a visible function table for the intersection functions.
- [setVisibleFunctionTables(_:bufferRange:)](<setvisiblefunctiontables(__bufferrange_).md>) — Sets a range of visible function tables for the intersection functions.
