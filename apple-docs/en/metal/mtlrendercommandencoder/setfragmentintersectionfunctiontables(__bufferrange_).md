---
title: 'setFragmentIntersectionFunctionTables(_:bufferRange:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setfragmentintersectionfunctiontables(_:bufferrange:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setfragmentintersectionfunctiontables(_:bufferrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setfragmentintersectionfunctiontables%28_%3Abufferrange%3A%29.json'
content_hash: 'sha256:8a0232d17c1a163e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setFragmentIntersectionFunctionTables(_:bufferRange:)

<sub>Instance Method</sub>

Assigns multiple intersection function tables to a range of entries in the fragment shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setFragmentIntersectionFunctionTables(_ functionTables: [(any MTLIntersectionFunctionTable)?], bufferRange: Range<Int>)
```

## Parameters

- `functionTables` — An array of [MTLIntersectionFunctionTable](../mtlintersectionfunctiontable.md) instances the command assigns to entries in the fragment shader argument table for intersection function tables.

- `bufferRange` — A span of integers that represent the entries in the fragment shader argument table for intersection function tables. Each entry stores a record of the corresponding element in `functionTables`.

## Discussion

By default, the intersection function table at each index is `nil`.

> [!note] Note
> The Objective-C version of this method is [setFragmentIntersectionFunctionTables:withBufferRange:](setfragmentintersectionfunctiontables_withbufferrange_.md).

## See Also

### Assigning intersection function tables

- [- setFragmentIntersectionFunctionTable:atBufferIndex:](<setfragmentintersectionfunctiontable(__bufferindex_).md>) — Assigns an intersection function table to an entry in the fragment shader argument table.
