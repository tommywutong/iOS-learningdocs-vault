---
title: 'setFragmentVisibleFunctionTables:withBufferRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setfragmentvisiblefunctiontables:withbufferrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setfragmentvisiblefunctiontables:withbufferrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setfragmentvisiblefunctiontables%3Awithbufferrange%3A.json'
content_hash: 'sha256:8588406e70fee320'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setFragmentVisibleFunctionTables:withBufferRange:

<sub>Instance Method</sub>

Assigns multiple visible function tables to a range of entries in the fragment shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setFragmentVisibleFunctionTables:(id<MTLVisibleFunctionTable> const[]) functionTables withBufferRange:(NSRange) range;
```

## Parameters

- `functionTables` — A pointer to a C array of [MTLVisibleFunctionTable](../mtlvisiblefunctiontable.md) instances the command assigns to entries in the fragment shader argument table for visible function tables.

- `range` — A span of integers that represent the entries in the fragment shader argument table for visible function tables. Each entry stores a record of the corresponding element in `functionTables`.

## Discussion

By default, the visible function table at each index is `nil`.

> [!note] Note
> The Swift version of this method is [setFragmentVisibleFunctionTables(_:bufferRange:)](<setfragmentvisiblefunctiontables(__bufferrange_).md>).

## See Also

### Assigning visible function tables

- [- setFragmentVisibleFunctionTable:atBufferIndex:](<setfragmentvisiblefunctiontable(__bufferindex_).md>) — Assigns a visible function table to an entry in the fragment shader argument table.
