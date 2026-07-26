---
title: 'setIntersectionFunctionTable(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlargumentencoder/setintersectionfunctiontable(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/setintersectionfunctiontable(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/setintersectionfunctiontable%28_%3Aindex%3A%29.json'
content_hash: 'sha256:7fefb95562e7b78a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# setIntersectionFunctionTable(_:index:)

<sub>Instance Method</sub>

Encodes a reference to a ray-tracing intersection-function table into the argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setIntersectionFunctionTable(_ intersectionFunctionTable: (any MTLIntersectionFunctionTable)?, index: Int)
```

## Parameters

- `intersectionFunctionTable` — An intersection-function table the method encodes.

- `index` — An index of an intersection-function table within the argument buffer. The value corresponds to either the index ID of a declaration in Metal Shading Language (MSL) or the [index](../mtlargumentdescriptor/index.md) property of an [MTLArgumentDescriptor](../mtlargumentdescriptor.md) instance.

## See Also

### Encoding function tables

- [- setVisibleFunctionTable:atIndex:](<setvisiblefunctiontable(__index_).md>) — Encodes a reference to a visible-function table into the argument buffer.
- [setIntersectionFunctionTables(_:range:)](<setintersectionfunctiontables(__range_).md>) — Encodes references to an array of ray-tracing intersection-function tables into the argument buffer.
- [setVisibleFunctionTables(_:range:)](<setvisiblefunctiontables(__range_).md>) — Encodes references to an array of ray-tracing intersection-function tables into the argument buffer.
