---
title: 'setFragmentVisibleFunctionTables(_:bufferRange:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setfragmentvisiblefunctiontables(_:bufferrange:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setfragmentvisiblefunctiontables(_:bufferrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setfragmentvisiblefunctiontables%28_%3Abufferrange%3A%29.json'
content_hash: 'sha256:eae7d546082e2769'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setFragmentVisibleFunctionTables(_:bufferRange:)

<sub>Instance Method</sub>

Assigns multiple visible function tables to a range of entries in the fragment shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setFragmentVisibleFunctionTables(_ functionTables: [(any MTLVisibleFunctionTable)?], bufferRange: Range<Int>)
```

## Parameters

- `functionTables` — An array of [MTLVisibleFunctionTable](../mtlvisiblefunctiontable.md) instances the command assigns to entries in the fragment shader argument table for visible function tables.

- `bufferRange` — A span of integers that represent the entries in the fragment shader argument table for visible function tables. Each entry stores a record of the corresponding element in `functionTables`.

## Discussion

By default, the visible function table at each index is `nil`.

> [!note] Note
> The Objective-C version of this method is [setFragmentVisibleFunctionTables:withBufferRange:](setfragmentvisiblefunctiontables_withbufferrange_.md).

## See Also

### Assigning visible function tables

- [- setFragmentVisibleFunctionTable:atBufferIndex:](<setfragmentvisiblefunctiontable(__bufferindex_).md>) — Assigns a visible function table to an entry in the fragment shader argument table.
