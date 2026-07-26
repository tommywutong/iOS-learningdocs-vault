---
title: fragmentBuffers
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinedescriptor/fragmentbuffers
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/fragmentbuffers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinedescriptor/fragmentbuffers.json'
content_hash: 'sha256:b151bc39b77652c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineDescriptor](../mtlrenderpipelinedescriptor.md)

# fragmentBuffers

<sub>Instance Property</sub>

An array that contains the buffer mutability options for a render pipeline’s fragment function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var fragmentBuffers: MTLPipelineBufferDescriptorArray { get }
```

## Discussion

This property returns an array of [MTLPipelineBufferDescriptor](../mtlpipelinebufferdescriptor.md) instances, where each element corresponds to the index in the buffer argument table for the render pipeline’s fragment function.

```objective-c
// Indicate the fragment buffer at index 8 is immutable while setting up the render pipeline.
MTLRenderPipelineDescriptor *renderDescriptor = [MTLRenderPipelineDescriptor new];
renderDescriptor.fragmentBuffers[8].mutability = MTLMutabilityImmutable;

// Create an encoder for the render pass.
id <MTLRenderCommandEncoder> renderEncoder;
renderEncoder = [_commandBuffer renderCommandEncoderWithDescriptor:_renderPassDescriptor];

// Assign the buffer at index 8 for the render pass.
[renderEncoder setFragmentBuffer:_buffer offset:0 atIndex:8];
```

## See Also

### Specifying buffer mutability

- [vertexBuffers](vertexbuffers.md) — An array that contains the buffer mutability options for a render pipeline’s vertex function.
