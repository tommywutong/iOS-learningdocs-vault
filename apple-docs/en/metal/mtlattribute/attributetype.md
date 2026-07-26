---
title: attributeType
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlattribute/attributetype
source_url: 'https://developer.apple.com/documentation/metal/mtlattribute/attributetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlattribute/attributetype.json'
content_hash: 'sha256:fbaf28e90496314d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAttribute](../mtlattribute.md)

# attributeType

<sub>Instance Property</sub>

The data type for the attribute, as declared in Metal shader source code.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var attributeType: MTLDataType { get }
```

## See Also

### Reading an attribute’s properties

- [name](name.md) — The name of the attribute.
- [attributeIndex](attributeindex.md) — The index of the attribute, as declared in Metal shader source code.
- [active](isactive.md) — A Boolean value that indicates whether the attribute is active.
- [patchControlPointData](ispatchcontrolpointdata.md) — A Boolean value that indicates whether the attribute represents control point data.
- [patchData](ispatchdata.md) — A Boolean value that indicates whether the attribute represents tessellation patch data.
