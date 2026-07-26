---
title: 'setTileIntersectionFunctionTables(_:bufferRange:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/settileintersectionfunctiontables(_:bufferrange:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settileintersectionfunctiontables(_:bufferrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/settileintersectionfunctiontables%28_%3Abufferrange%3A%29.json'
content_hash: 'sha256:258f1618494a715a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setTileIntersectionFunctionTables(_:bufferRange:)

<sub>Instance Method</sub>

Assigns multiple intersection function tables to a range of entries in the tile shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setTileIntersectionFunctionTables(_ functionTables: [(any MTLIntersectionFunctionTable)?], bufferRange: Range<Int>)
```

## Parameters

- `functionTables` — An array of [MTLIntersectionFunctionTable](../mtlintersectionfunctiontable.md) instances the command assigns to entries in the tile shader argument table for intersection function tables.

- `bufferRange` — A span of integers that represent the entries in the tile shader argument table for intersection function tables. Each entry stores a record of the corresponding element in `functionTables`.

## Discussion

By default, the intersection function table at each index is `nil`.

> [!note] Note
> The Objective-C version of this method is [setTileIntersectionFunctionTables:withBufferRange:](settileintersectionfunctiontables_withbufferrange_.md).

## See Also

### Assigning intersection function tables

- [- setTileIntersectionFunctionTable:atBufferIndex:](<settileintersectionfunctiontable(__bufferindex_).md>) — Assigns an intersection function table to an entry in the tile shader argument table.
