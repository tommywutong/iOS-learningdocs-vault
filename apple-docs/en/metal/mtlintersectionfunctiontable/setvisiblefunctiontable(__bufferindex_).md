---
title: 'setVisibleFunctionTable(_:bufferIndex:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlintersectionfunctiontable/setvisiblefunctiontable(_:bufferindex:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlintersectionfunctiontable/setvisiblefunctiontable(_:bufferindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlintersectionfunctiontable/setvisiblefunctiontable%28_%3Abufferindex%3A%29.json'
content_hash: 'sha256:f1945f8e0a38de27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIntersectionFunctionTable](../mtlintersectionfunctiontable.md)

# setVisibleFunctionTable(_:bufferIndex:)

<sub>Instance Method</sub>

Sets a visible function table for the intersection functions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setVisibleFunctionTable(_ functionTable: (any MTLVisibleFunctionTable)?, bufferIndex: Int)
```

## Parameters

- `functionTable` — A visible function table.

- `bufferIndex` — An index in the function table’s buffer argument table.

## See Also

### Specifying arguments for intersection functions

- [- setBuffer:offset:atIndex:](<setbuffer(__offset_index_).md>) — Sets a buffer for the intersection functions.
- [setBuffers(_:offsets:range:)](<setbuffers(__offsets_range_).md>) — Sets a range of buffers for the intersection functions.
- [setVisibleFunctionTables(_:bufferRange:)](<setvisiblefunctiontables(__bufferrange_).md>) — Sets a range of visible function tables for the intersection functions.
