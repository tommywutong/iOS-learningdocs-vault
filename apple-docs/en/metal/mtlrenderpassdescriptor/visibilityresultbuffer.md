---
title: visibilityResultBuffer
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpassdescriptor/visibilityresultbuffer
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/visibilityresultbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpassdescriptor/visibilityresultbuffer.json'
content_hash: 'sha256:29402ef2dcd77dfb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassDescriptor](../mtlrenderpassdescriptor.md)

# visibilityResultBuffer

<sub>Instance Property</sub>

A buffer where the GPU writes visibility test results when fragments pass depth and stencil tests.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var visibilityResultBuffer: (any MTLBuffer)? { get set }
```

## Discussion

When encoding a render pass, you can tell the GPU to record data about fragments that pass depth and stencil tests. Typically, you use visibility testing to track whether a particular piece of geometry is visible in the current frame, so you can omit drawing calls for hidden objects when encoding future frames. This technique is sometimes called _occlusion culling_. You can record separate tests for different pieces of geometry.

Set this property to provide the buffer for the GPU to store visibility results when it executes the render pass. The GPU stores visibility results as 64-bit integers, so you need to reserve `8` bytes for each visibility result that you want to track. After creating the render command encoder, call [- setVisibilityResultMode:offset:](<../mtlrendercommandencoder/setvisibilityresultmode(__offset_).md>) to start each visibility test.

## See Also

### Related Documentation

- [- setVisibilityResultMode:offset:](<../mtlrendercommandencoder/setvisibilityresultmode(__offset_).md>) — Configures which visibility test the GPU runs and the destination for any results it generates.
