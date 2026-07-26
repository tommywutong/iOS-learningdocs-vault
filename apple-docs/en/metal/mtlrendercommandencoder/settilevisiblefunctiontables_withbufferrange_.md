---
title: 'setTileVisibleFunctionTables:withBufferRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/settilevisiblefunctiontables:withbufferrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settilevisiblefunctiontables:withbufferrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/settilevisiblefunctiontables%3Awithbufferrange%3A.json'
content_hash: 'sha256:fc7c0f0fd6d87732'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setTileVisibleFunctionTables:withBufferRange:

<sub>Instance Method</sub>

Assigns multiple visible function tables to a range of entries in the tile shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setTileVisibleFunctionTables:(id<MTLVisibleFunctionTable> const[]) functionTables withBufferRange:(NSRange) range;
```

## Parameters

- `functionTables` — A pointer to a C array of [MTLVisibleFunctionTable](../mtlvisiblefunctiontable.md) instances the command assigns to entries in the tile shader argument table for visible function tables.

- `range` — A span of integers that represent the entries in the tile shader argument table for visible function tables. Each entry stores a record of the corresponding element in `functionTables`.

## Discussion

By default, the visible function table at each index is `nil`.

> [!note] Note
> The Swift version of this method is [setTileVisibleFunctionTables(_:bufferRange:)](<settilevisiblefunctiontables(__bufferrange_).md>).

## See Also

### Assigning visible function tables

- [- setTileVisibleFunctionTable:atBufferIndex:](<settilevisiblefunctiontable(__bufferindex_).md>) — Assigns a visible function table to an entry in the tile shader argument table.
