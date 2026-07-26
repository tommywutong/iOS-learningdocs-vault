---
title: maxVertexAmplificationCount
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinedescriptor/maxvertexamplificationcount
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/maxvertexamplificationcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinedescriptor/maxvertexamplificationcount.json'
content_hash: 'sha256:63551bb00d57d8c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineDescriptor](../mtlrenderpipelinedescriptor.md)

# maxVertexAmplificationCount

<sub>Instance Property</sub>

The maximum vertex amplification count you can set when encoding render commands.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var maxVertexAmplificationCount: Int { get set }
```

## Discussion

Before setting this property, call the [- supportsVertexAmplificationCount:](<../mtldevice/supportsvertexamplificationcount(__).md>) method on the device object to determine whether that amplification count is supported.

## See Also

### Related Documentation

- [- setVertexAmplificationCount:viewMappings:](<../mtlrendercommandencoder/setvertexamplificationcount(__viewmappings_).md>) — Configures the number of output vertices the render pipeline produces for each input vertex, optionally with render target and viewport offsets.
- [- supportsVertexAmplificationCount:](<../mtldevice/supportsvertexamplificationcount(__).md>) — Returns a Boolean value that indicates whether the GPU supports an amplification factor.
