---
title: isPatchData
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlvertexattribute/ispatchdata
source_url: 'https://developer.apple.com/documentation/metal/mtlvertexattribute/ispatchdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvertexattribute/ispatchdata.json'
content_hash: 'sha256:5486ee3c9683f31d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLVertexAttribute](../mtlvertexattribute.md)

# isPatchData

<sub>Instance Property</sub>

A Boolean value that indicates whether this vertex attribute represents patch data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isPatchData: Bool { get }
```

## Discussion

This value is always [false](../../swift/false.md) if the vertex function is not a post-tessellation vertex function.

## See Also

### Describing the attribute

- [name](name.md) — The name of the attribute.
- [attributeIndex](attributeindex.md) — The index of the attribute, as declared in Metal shader source code.
- [attributeType](attributetype.md) — The data type for the attribute, as declared in Metal shader source code.
- [active](isactive.md) — A Boolean value that indicates whether this vertex attribute is active.
- [patchControlPointData](ispatchcontrolpointdata.md) — A Boolean value that indicates whether this vertex attribute represents control point data.
