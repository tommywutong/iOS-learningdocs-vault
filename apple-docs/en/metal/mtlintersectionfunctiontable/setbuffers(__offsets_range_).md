---
title: 'setBuffers(_:offsets:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlintersectionfunctiontable/setbuffers(_:offsets:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlintersectionfunctiontable/setbuffers(_:offsets:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlintersectionfunctiontable/setbuffers%28_%3Aoffsets%3Arange%3A%29.json'
content_hash: 'sha256:99c008ae04929a9e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIntersectionFunctionTable](../mtlintersectionfunctiontable.md)

# setBuffers(_:offsets:range:)

<sub>Instance Method</sub>

Sets a range of buffers for the intersection functions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setBuffers(_ buffers: [(any MTLBuffer)?], offsets: [Int], range: Range<Int>)
```

## Parameters

- `buffers` — An array of buffers to insert into the table.

- `offsets` — An array of offsets to insert into the table.

- `range` — A range of indices in the function table’s buffer argument table.

## See Also

### Specifying arguments for intersection functions

- [- setBuffer:offset:atIndex:](<setbuffer(__offset_index_).md>) — Sets a buffer for the intersection functions.
- [- setVisibleFunctionTable:atBufferIndex:](<setvisiblefunctiontable(__bufferindex_).md>) — Sets a visible function table for the intersection functions.
- [setVisibleFunctionTables(_:bufferRange:)](<setvisiblefunctiontables(__bufferrange_).md>) — Sets a range of visible function tables for the intersection functions.
