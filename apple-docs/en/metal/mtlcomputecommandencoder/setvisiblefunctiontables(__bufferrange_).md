---
title: 'setVisibleFunctionTables(_:bufferRange:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/setvisiblefunctiontables(_:bufferrange:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setvisiblefunctiontables(_:bufferrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/setvisiblefunctiontables%28_%3Abufferrange%3A%29.json'
content_hash: 'sha256:3862e24269d97a9a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# setVisibleFunctionTables(_:bufferRange:)

<sub>Instance Method</sub>

Binds multiple visible function tables to the buffer argument table, allowing you to call their functions on the GPU.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setVisibleFunctionTables(_ visibleFunctionTables: [(any MTLVisibleFunctionTable)?], bufferRange: Range<Int>)
```

## Parameters

- `visibleFunctionTables` — An array of [MTLVisibleFunctionTable](../mtlvisiblefunctiontable.md) instances to bind.

- `bufferRange` — The buffer argument table indices to bind each of the `visibleFunctionTables` to, in the order they appear.

## Discussion

> [!warning] Warning
> This method requires that the number of instances in `visibleFunctionTables` be the same as the length of `bufferRange`.

## See Also

### Binding function tables

- [- setVisibleFunctionTable:atBufferIndex:](<setvisiblefunctiontable(__bufferindex_).md>) — Binds a visible function table to the buffer argument table, allowing you to call its functions on the GPU.
- [setIntersectionFunctionTables(_:bufferRange:)](<setintersectionfunctiontables(__bufferrange_).md>) — Binds multiple intersection function tables to the buffer argument table, allowing you to call their functions on the GPU.
