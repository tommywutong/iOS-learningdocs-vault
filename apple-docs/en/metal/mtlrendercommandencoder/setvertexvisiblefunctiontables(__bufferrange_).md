---
title: 'setVertexVisibleFunctionTables(_:bufferRange:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setvertexvisiblefunctiontables(_:bufferrange:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertexvisiblefunctiontables(_:bufferrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setvertexvisiblefunctiontables%28_%3Abufferrange%3A%29.json'
content_hash: 'sha256:143fccd09d121899'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setVertexVisibleFunctionTables(_:bufferRange:)

<sub>Instance Method</sub>

Assigns multiple visible function tables to a range of entries in the vertex shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setVertexVisibleFunctionTables(_ functionTables: [(any MTLVisibleFunctionTable)?], bufferRange: Range<Int>)
```

## Parameters

- `functionTables` — An array of [MTLVisibleFunctionTable](../mtlvisiblefunctiontable.md) instances the command assigns to entries in the vertex shader argument table for visible function tables.

- `bufferRange` — A span of integers that represent the entries in the vertex shader argument table for visible function tables. Each entry stores a record of the corresponding element in `functionTables`.

## Discussion

By default, the visible function table at each index is `nil`.

> [!note] Note
> The Objective-C version of this method is [setVertexVisibleFunctionTables:withBufferRange:](setvertexvisiblefunctiontables_withbufferrange_.md).

## See Also

### Assigning visible function tables

- [- setVertexVisibleFunctionTable:atBufferIndex:](<setvertexvisiblefunctiontable(__bufferindex_).md>) — Assigns a visible function table to an entry in the vertex shader argument table.
