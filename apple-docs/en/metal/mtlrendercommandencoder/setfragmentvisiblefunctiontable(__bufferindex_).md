---
title: 'setFragmentVisibleFunctionTable(_:bufferIndex:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setfragmentvisiblefunctiontable(_:bufferindex:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setfragmentvisiblefunctiontable(_:bufferindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setfragmentvisiblefunctiontable%28_%3Abufferindex%3A%29.json'
content_hash: 'sha256:523c7b6c73901ac6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setFragmentVisibleFunctionTable(_:bufferIndex:)

<sub>Instance Method</sub>

Assigns a visible function table to an entry in the fragment shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setFragmentVisibleFunctionTable(_ functionTable: (any MTLVisibleFunctionTable)?, bufferIndex: Int)
```

## Parameters

- `functionTable` — An [MTLVisibleFunctionTable](../mtlvisiblefunctiontable.md) instance the command assigns to an entry in the fragment shader argument table for visible function tables.

- `bufferIndex` — An integer that represents the entry in the fragment shader argument table for visible function tables that stores a record of `functionTable`.

## Discussion

By default, the visible function table at each index is `nil`.

## See Also

### Assigning visible function tables

- [setFragmentVisibleFunctionTables(_:bufferRange:)](<setfragmentvisiblefunctiontables(__bufferrange_).md>) — Assigns multiple visible function tables to a range of entries in the fragment shader argument table.
