---
title: 'setIntersectionFunctionTables(_:bufferRange:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/setintersectionfunctiontables(_:bufferrange:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setintersectionfunctiontables(_:bufferrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/setintersectionfunctiontables%28_%3Abufferrange%3A%29.json'
content_hash: 'sha256:4382a740f01873e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# setIntersectionFunctionTables(_:bufferRange:)

<sub>Instance Method</sub>

Binds multiple intersection function tables to the buffer argument table, allowing you to call their functions on the GPU.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setIntersectionFunctionTables(_ intersectionFunctionTables: [(any MTLIntersectionFunctionTable)?], bufferRange: Range<Int>)
```

## Parameters

- `intersectionFunctionTables` — An array of [MTLIntersectionFunctionTable](../mtlintersectionfunctiontable.md) instances to bind.

- `bufferRange` — The argument buffer table indices to bind each of the `intersectionFunctionTables` to, in the order they appear.

## Discussion

> [!warning] Warning
> This method requires that the number of instances in `visibleFunctionTables` be the same as the length of `bufferRange`.

## See Also

### Binding function tables

- [- setVisibleFunctionTable:atBufferIndex:](<setvisiblefunctiontable(__bufferindex_).md>) — Binds a visible function table to the buffer argument table, allowing you to call its functions on the GPU.
- [setVisibleFunctionTables(_:bufferRange:)](<setvisiblefunctiontables(__bufferrange_).md>) — Binds multiple visible function tables to the buffer argument table, allowing you to call their functions on the GPU.
