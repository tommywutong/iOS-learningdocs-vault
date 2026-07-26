---
title: viewportArrayIndexOffset
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlvertexamplificationviewmapping/viewportarrayindexoffset
source_url: 'https://developer.apple.com/documentation/metal/mtlvertexamplificationviewmapping/viewportarrayindexoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvertexamplificationviewmapping/viewportarrayindexoffset.json'
content_hash: 'sha256:df1eca5022a80ca2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLVertexAmplificationViewMapping](../mtlvertexamplificationviewmapping.md)

# viewportArrayIndexOffset

<sub>Instance Property</sub>

An offset into the list of viewports.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var viewportArrayIndexOffset: UInt32
```

## Discussion

To specify a list of offsets, call the [- setVertexAmplificationCount:viewMappings:](<../mtlrendercommandencoder/setvertexamplificationcount(__viewmappings_).md>) method.

When your app renders to different render targets, you specify the render target index to render to in your vertex shader by adding the `viewport_array_index` attribute to one of the vertex shader’s outputs. If you are using vertex amplification, Metal calculates the index for each amplified vertex by adding the index offset for the vertex to the value returned from your shader.

## See Also

### Specifying mapping offsets

- [renderTargetArrayIndexOffset](rendertargetarrayindexoffset.md) — An offset into the list of render targets.
