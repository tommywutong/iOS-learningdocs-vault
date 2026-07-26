---
title: 'setVisibleFunctionTables(_:bufferRange:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlintersectionfunctiontable/setvisiblefunctiontables(_:bufferrange:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlintersectionfunctiontable/setvisiblefunctiontables(_:bufferrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlintersectionfunctiontable/setvisiblefunctiontables%28_%3Abufferrange%3A%29.json'
content_hash: 'sha256:6876f4633f4b6353'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIntersectionFunctionTable](../mtlintersectionfunctiontable.md)

# setVisibleFunctionTables(_:bufferRange:)

<sub>Instance Method</sub>

Sets a range of visible function tables for the intersection functions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setVisibleFunctionTables(_ functionTables: [(any MTLVisibleFunctionTable)?], bufferRange: Range<Int>)
```

## Parameters

- `functionTables` — The function tables to insert.

- `bufferRange` — A range of indices in the function table’s buffer argument table.

## See Also

### Specifying arguments for intersection functions

- [- setBuffer:offset:atIndex:](<setbuffer(__offset_index_).md>) — Sets a buffer for the intersection functions.
- [setBuffers(_:offsets:range:)](<setbuffers(__offsets_range_).md>) — Sets a range of buffers for the intersection functions.
- [- setVisibleFunctionTable:atBufferIndex:](<setvisiblefunctiontable(__bufferindex_).md>) — Sets a visible function table for the intersection functions.
