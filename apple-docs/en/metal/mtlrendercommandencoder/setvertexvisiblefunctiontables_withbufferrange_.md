---
title: 'setVertexVisibleFunctionTables:withBufferRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setvertexvisiblefunctiontables:withbufferrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertexvisiblefunctiontables:withbufferrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setvertexvisiblefunctiontables%3Awithbufferrange%3A.json'
content_hash: 'sha256:5ec9f727d5b0703d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setVertexVisibleFunctionTables:withBufferRange:

<sub>Instance Method</sub>

Assigns multiple visible function tables to a range of entries in the vertex shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setVertexVisibleFunctionTables:(id<MTLVisibleFunctionTable> const[]) functionTables withBufferRange:(NSRange) range;
```

## Parameters

- `functionTables` — A pointer to a C array of [MTLVisibleFunctionTable](../mtlvisiblefunctiontable.md) instances the command assigns to entries in the vertex shader argument table for visible function tables.

- `range` — A span of integers that represent the entries in the vertex shader argument table for visible function tables. Each entry stores a record of the corresponding element in `functionTables`.

## Discussion

By default, the visible function table at each index is `nil`.

> [!note] Note
> The Swift version of this method is [setVertexVisibleFunctionTables(_:bufferRange:)](<setvertexvisiblefunctiontables(__bufferrange_).md>).

## See Also

### Assigning visible function tables

- [- setVertexVisibleFunctionTable:atBufferIndex:](<setvertexvisiblefunctiontable(__bufferindex_).md>) — Assigns a visible function table to an entry in the vertex shader argument table.
