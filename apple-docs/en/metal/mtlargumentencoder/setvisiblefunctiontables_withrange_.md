---
title: 'setVisibleFunctionTables:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlargumentencoder/setvisiblefunctiontables:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/setvisiblefunctiontables:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/setvisiblefunctiontables%3Awithrange%3A.json'
content_hash: 'sha256:2db9c5aae771274b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# setVisibleFunctionTables:withRange:

<sub>Instance Method</sub>

Encodes references to an array of visible function tables into the argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setVisibleFunctionTables:(id<MTLVisibleFunctionTable> const[]) visibleFunctionTables withRange:(NSRange) range;
```

## Parameters

- `visibleFunctionTables` — An array of visible-function tables the method encodes.

- `range` — A range of indices within the argument buffer for each element in `visibleFunctionTables`. The values correspond to either the index IDs of declarations in Metal Shading Language (MSL) or the [index](../mtlargumentdescriptor/index.md) property of [MTLArgumentDescriptor](../mtlargumentdescriptor.md) instances.

## See Also

### Encoding function tables

- [- setVisibleFunctionTable:atIndex:](<setvisiblefunctiontable(__index_).md>) — Encodes a reference to a visible-function table into the argument buffer.
- [- setIntersectionFunctionTable:atIndex:](<setintersectionfunctiontable(__index_).md>) — Encodes a reference to a ray-tracing intersection-function table into the argument buffer.
- [setIntersectionFunctionTables:withRange:](setintersectionfunctiontables_withrange_.md) — Encodes references to an array of ray-tracing intersection-function tables into the argument buffer.
