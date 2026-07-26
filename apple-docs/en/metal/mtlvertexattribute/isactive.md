---
title: isActive
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlvertexattribute/isactive
source_url: 'https://developer.apple.com/documentation/metal/mtlvertexattribute/isactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvertexattribute/isactive.json'
content_hash: 'sha256:db294844aed2f3a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLVertexAttribute](../mtlvertexattribute.md)

# isActive

<sub>Instance Property</sub>

A Boolean value that indicates whether this vertex attribute is active.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isActive: Bool { get }
```

## Discussion

If [false](../../swift/false.md), this attribute is inactive and can be ignored.

## See Also

### Describing the attribute

- [name](name.md) — The name of the attribute.
- [attributeIndex](attributeindex.md) — The index of the attribute, as declared in Metal shader source code.
- [attributeType](attributetype.md) — The data type for the attribute, as declared in Metal shader source code.
- [patchControlPointData](ispatchcontrolpointdata.md) — A Boolean value that indicates whether this vertex attribute represents control point data.
- [patchData](ispatchdata.md) — A Boolean value that indicates whether this vertex attribute represents patch data.
