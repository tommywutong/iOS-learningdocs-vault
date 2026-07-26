---
title: vertexBuffers
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinedescriptor/vertexbuffers
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/vertexbuffers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinedescriptor/vertexbuffers.json'
content_hash: 'sha256:dbb419bfc720bbb5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineDescriptor](../mtlrenderpipelinedescriptor.md)

# vertexBuffers

<sub>Instance Property</sub>

An array that contains the buffer mutability options for a render pipeline’s vertex function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var vertexBuffers: MTLPipelineBufferDescriptorArray { get }
```

## Discussion

This property returns an array of [MTLPipelineBufferDescriptor](../mtlpipelinebufferdescriptor.md) instances, where each element corresponds to the same index in the buffer argument table for the render pipeline’s vertex function.

```objective-c
// Indicate the vertex buffer at index 7 is immutable while setting up the render pipeline.
MTLRenderPipelineDescriptor *renderDescriptor = [MTLRenderPipelineDescriptor new];
renderDescriptor.vertexBuffers[7].mutability = MTLMutabilityImmutable;

// Create an encoder for the render pass.
id <MTLRenderCommandEncoder> renderEncoder;
renderEncoder = [_commandBuffer renderCommandEncoderWithDescriptor:_renderPassDescriptor];

// Assign the buffer at index 7 for the render pass.
[renderEncoder setVertexBuffer:_buffer offset:0 atIndex:7];
```

## See Also

### Specifying buffer mutability

- [fragmentBuffers](fragmentbuffers.md) — An array that contains the buffer mutability options for a render pipeline’s fragment function.
