---
title: 'setTileIntersectionFunctionTables:withBufferRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/settileintersectionfunctiontables:withbufferrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settileintersectionfunctiontables:withbufferrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/settileintersectionfunctiontables%3Awithbufferrange%3A.json'
content_hash: 'sha256:11cd329aeb464aa1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setTileIntersectionFunctionTables:withBufferRange:

<sub>Instance Method</sub>

Assigns multiple intersection function tables to a range of entries in the tile shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setTileIntersectionFunctionTables:(id<MTLIntersectionFunctionTable> const[]) intersectionFunctionTables withBufferRange:(NSRange) range;
```

## Parameters

- `intersectionFunctionTables` — A pointer to a C array of [MTLIntersectionFunctionTable](../mtlintersectionfunctiontable.md) instances the command assigns to entries in the tile shader argument table for intersection function tables.

- `range` — A span of integers that represent the entries in the tile shader argument table for intersection function tables. Each entry stores a record of the corresponding element in `intersectionFunctionTables`.

## Discussion

By default, the intersection function table at each index is `nil`.

> [!note] Note
> The Swift version of this method is [setTileIntersectionFunctionTables(_:bufferRange:)](<settileintersectionfunctiontables(__bufferrange_).md>).

## See Also

### Assigning intersection function tables

- [- setTileIntersectionFunctionTable:atBufferIndex:](<settileintersectionfunctiontable(__bufferindex_).md>) — Assigns an intersection function table to an entry in the tile shader argument table.
