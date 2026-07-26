---
title: layouts
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlvertexdescriptor/layouts
source_url: 'https://developer.apple.com/documentation/metal/mtlvertexdescriptor/layouts'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvertexdescriptor/layouts.json'
content_hash: 'sha256:fd40bbaa8b795a0a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLVertexDescriptor](../mtlvertexdescriptor.md)

# layouts

<sub>Instance Property</sub>

An array of state data that describes how data are fetched by a vertex shader function when rendering primitives.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var layouts: MTLVertexBufferLayoutDescriptorArray { get }
```

## See Also

### Accessing the vertex buffer layouts and vertex attributes

- [attributes](attributes.md) — An array of state data that describes how vertex attribute data is stored in memory and is mapped to arguments for a vertex shader function.
