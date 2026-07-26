---
title: 'setVisibleFunctionTables:withBufferRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlintersectionfunctiontable/setvisiblefunctiontables:withbufferrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlintersectionfunctiontable/setvisiblefunctiontables:withbufferrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlintersectionfunctiontable/setvisiblefunctiontables%3Awithbufferrange%3A.json'
content_hash: 'sha256:83b19fde2c57f963'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIntersectionFunctionTable](../mtlintersectionfunctiontable.md)

# setVisibleFunctionTables:withBufferRange:

<sub>Instance Method</sub>

Sets a range of visible function tables for the intersection functions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setVisibleFunctionTables:(id<MTLVisibleFunctionTable> const[]) functionTables withBufferRange:(NSRange) bufferRange;
```

## Parameters

- `functionTables` — The function tables to insert.

- `bufferRange` — A range of indices in the function table’s buffer argument table.

## See Also

### Specifying arguments for intersection functions

- [- setBuffer:offset:atIndex:](<setbuffer(__offset_index_).md>) — Sets a buffer for the intersection functions.
- [setBuffers:offsets:withRange:](setbuffers_offsets_withrange_.md) — Sets a range of buffers for the intersection functions.
- [- setVisibleFunctionTable:atBufferIndex:](<setvisiblefunctiontable(__bufferindex_).md>) — Sets a visible function table for the intersection functions.
