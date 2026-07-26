---
title: 'setIntersectionFunctionTables(_:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlargumentencoder/setintersectionfunctiontables(_:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/setintersectionfunctiontables(_:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/setintersectionfunctiontables%28_%3Arange%3A%29.json'
content_hash: 'sha256:9ed31c87cd34f276'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# setIntersectionFunctionTables(_:range:)

<sub>Instance Method</sub>

Encodes references to an array of ray-tracing intersection-function tables into the argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setIntersectionFunctionTables(_ intersectionFunctionTables: [(any MTLIntersectionFunctionTable)?], range: Range<Int>)
```

## Parameters

- `intersectionFunctionTables` — An array of intersection-function tables the method encodes.

- `range` — A range of indices within the argument buffer for each element in `intersectionFunctionTables`. The values correspond to either the index IDs of declarations in Metal Shading Language (MSL) or the [index](../mtlargumentdescriptor/index.md) property of [MTLArgumentDescriptor](../mtlargumentdescriptor.md) instances.

## See Also

### Encoding function tables

- [- setVisibleFunctionTable:atIndex:](<setvisiblefunctiontable(__index_).md>) — Encodes a reference to a visible-function table into the argument buffer.
- [- setIntersectionFunctionTable:atIndex:](<setintersectionfunctiontable(__index_).md>) — Encodes a reference to a ray-tracing intersection-function table into the argument buffer.
- [setVisibleFunctionTables(_:range:)](<setvisiblefunctiontables(__range_).md>) — Encodes references to an array of ray-tracing intersection-function tables into the argument buffer.
