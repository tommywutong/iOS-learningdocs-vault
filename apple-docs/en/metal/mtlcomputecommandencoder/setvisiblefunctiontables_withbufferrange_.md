---
title: 'setVisibleFunctionTables:withBufferRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/setvisiblefunctiontables:withbufferrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setvisiblefunctiontables:withbufferrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/setvisiblefunctiontables%3Awithbufferrange%3A.json'
content_hash: 'sha256:fd1ebe8eb0c5cb3f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# setVisibleFunctionTables:withBufferRange:

<sub>Instance Method</sub>

Binds multiple visible function tables to the buffer argument table, allowing you to call their functions on the GPU.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setVisibleFunctionTables:(id<MTLVisibleFunctionTable> const[]) visibleFunctionTables withBufferRange:(NSRange) range;
```

## Parameters

- `visibleFunctionTables` — An array of [MTLVisibleFunctionTable](../mtlvisiblefunctiontable.md) instances to bind.

- `range` — The buffer argument table indices to bind each of the `visibleFunctionTables` to, in the order they appear.

## Discussion

> [!warning] Warning
> This method requires that the number of instances in `visibleFunctionTables` be the same as the length of `range`.

## See Also

### Binding function tables

- [- setVisibleFunctionTable:atBufferIndex:](<setvisiblefunctiontable(__bufferindex_).md>) — Binds a visible function table to the buffer argument table, allowing you to call its functions on the GPU.
- [setIntersectionFunctionTables:withBufferRange:](setintersectionfunctiontables_withbufferrange_.md) — Binds multiple intersection function tables to the buffer argument table, allowing you to call their functions on the GPU.
