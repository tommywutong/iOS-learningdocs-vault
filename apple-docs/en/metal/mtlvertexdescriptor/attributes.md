---
title: attributes
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlvertexdescriptor/attributes
source_url: 'https://developer.apple.com/documentation/metal/mtlvertexdescriptor/attributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvertexdescriptor/attributes.json'
content_hash: 'sha256:4e1dd28eea0ce076'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLVertexDescriptor](../mtlvertexdescriptor.md)

# attributes

<sub>Instance Property</sub>

An array of state data that describes how vertex attribute data is stored in memory and is mapped to arguments for a vertex shader function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var attributes: MTLVertexAttributeDescriptorArray { get }
```

## See Also

### Accessing the vertex buffer layouts and vertex attributes

- [layouts](layouts.md) — An array of state data that describes how data are fetched by a vertex shader function when rendering primitives.
