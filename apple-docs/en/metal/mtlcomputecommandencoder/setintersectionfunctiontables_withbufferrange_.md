---
title: 'setIntersectionFunctionTables:withBufferRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/setintersectionfunctiontables:withbufferrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setintersectionfunctiontables:withbufferrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/setintersectionfunctiontables%3Awithbufferrange%3A.json'
content_hash: 'sha256:90d452bc1666be2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# setIntersectionFunctionTables:withBufferRange:

<sub>Instance Method</sub>

Binds multiple intersection function tables to the buffer argument table, allowing you to call their functions on the GPU.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setIntersectionFunctionTables:(id<MTLIntersectionFunctionTable> const[]) intersectionFunctionTables withBufferRange:(NSRange) range;
```

## Parameters

- `intersectionFunctionTables` — An array of [MTLIntersectionFunctionTable](../mtlintersectionfunctiontable.md) instances to bind.

- `range` — The argument buffer table indices to bind each of the `intersectionFunctionTables` to, in the order they appear.

## Discussion

> [!warning] Warning
> This method requires that the number of instances in `visibleFunctionTables` be the same as the length of `range`.

## See Also

### Binding function tables

- [- setVisibleFunctionTable:atBufferIndex:](<setvisiblefunctiontable(__bufferindex_).md>) — Binds a visible function table to the buffer argument table, allowing you to call its functions on the GPU.
- [setVisibleFunctionTables:withBufferRange:](setvisiblefunctiontables_withbufferrange_.md) — Binds multiple visible function tables to the buffer argument table, allowing you to call their functions on the GPU.
