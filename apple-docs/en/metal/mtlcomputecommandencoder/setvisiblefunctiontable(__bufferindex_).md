---
title: 'setVisibleFunctionTable(_:bufferIndex:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/setvisiblefunctiontable(_:bufferindex:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setvisiblefunctiontable(_:bufferindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/setvisiblefunctiontable%28_%3Abufferindex%3A%29.json'
content_hash: 'sha256:2fd6d777e8222a64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# setVisibleFunctionTable(_:bufferIndex:)

<sub>Instance Method</sub>

Binds a visible function table to the buffer argument table, allowing you to call its functions on the GPU.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setVisibleFunctionTable(_ visibleFunctionTable: (any MTLVisibleFunctionTable)?, bufferIndex: Int)
```

## Parameters

- `visibleFunctionTable` — The [MTLVisibleFunctionTable](../mtlvisiblefunctiontable.md) to bind.

- `bufferIndex` — The index the function table binds to in the buffer argument table.

## See Also

### Binding function tables

- [setVisibleFunctionTables(_:bufferRange:)](<setvisiblefunctiontables(__bufferrange_).md>) — Binds multiple visible function tables to the buffer argument table, allowing you to call their functions on the GPU.
- [setIntersectionFunctionTables(_:bufferRange:)](<setintersectionfunctiontables(__bufferrange_).md>) — Binds multiple intersection function tables to the buffer argument table, allowing you to call their functions on the GPU.
