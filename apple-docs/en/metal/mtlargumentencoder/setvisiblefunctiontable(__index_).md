---
title: 'setVisibleFunctionTable(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlargumentencoder/setvisiblefunctiontable(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/setvisiblefunctiontable(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/setvisiblefunctiontable%28_%3Aindex%3A%29.json'
content_hash: 'sha256:6685ee30638ed1f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# setVisibleFunctionTable(_:index:)

<sub>Instance Method</sub>

Encodes a reference to a visible-function table into the argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setVisibleFunctionTable(_ visibleFunctionTable: (any MTLVisibleFunctionTable)?, index: Int)
```

## Parameters

- `visibleFunctionTable` — A visible-function table the method encodes.

- `index` — The index of a visible-function table within the argument buffer. The value corresponds to either the index ID of a declaration in Metal Shading Language (MSL) or the [index](../mtlargumentdescriptor/index.md) property of an [MTLArgumentDescriptor](../mtlargumentdescriptor.md) instance.

## See Also

### Encoding function tables

- [- setIntersectionFunctionTable:atIndex:](<setintersectionfunctiontable(__index_).md>) — Encodes a reference to a ray-tracing intersection-function table into the argument buffer.
- [setIntersectionFunctionTables(_:range:)](<setintersectionfunctiontables(__range_).md>) — Encodes references to an array of ray-tracing intersection-function tables into the argument buffer.
- [setVisibleFunctionTables(_:range:)](<setvisiblefunctiontables(__range_).md>) — Encodes references to an array of ray-tracing intersection-function tables into the argument buffer.
