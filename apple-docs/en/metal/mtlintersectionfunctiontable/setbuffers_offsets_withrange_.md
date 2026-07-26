---
title: 'setBuffers:offsets:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlintersectionfunctiontable/setbuffers:offsets:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlintersectionfunctiontable/setbuffers:offsets:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlintersectionfunctiontable/setbuffers%3Aoffsets%3Awithrange%3A.json'
content_hash: 'sha256:188d7257ad069caa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIntersectionFunctionTable](../mtlintersectionfunctiontable.md)

# setBuffers:offsets:withRange:

<sub>Instance Method</sub>

Sets a range of buffers for the intersection functions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setBuffers:(id<MTLBuffer> const[]) buffers offsets:(const NSUInteger[]) offsets withRange:(NSRange) range;
```

## Parameters

- `buffers` — A pointer to an array of buffers.

- `offsets` — A pointer to an array of offsets, measured in bytes, from the start of each buffer.

- `range` — A range of indices in the function table’s buffer argument table.

## See Also

### Specifying arguments for intersection functions

- [- setBuffer:offset:atIndex:](<setbuffer(__offset_index_).md>) — Sets a buffer for the intersection functions.
- [- setVisibleFunctionTable:atBufferIndex:](<setvisiblefunctiontable(__bufferindex_).md>) — Sets a visible function table for the intersection functions.
- [setVisibleFunctionTables:withBufferRange:](setvisiblefunctiontables_withbufferrange_.md) — Sets a range of visible function tables for the intersection functions.
