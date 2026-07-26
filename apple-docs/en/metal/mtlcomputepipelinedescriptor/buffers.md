---
title: buffers
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcomputepipelinedescriptor/buffers
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor/buffers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepipelinedescriptor/buffers.json'
content_hash: 'sha256:cf1eef6d4f875b84'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputePipelineDescriptor](../mtlcomputepipelinedescriptor.md)

# buffers

<sub>Instance Property</sub>

The buffer mutability options to apply to the next kernel call.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var buffers: MTLPipelineBufferDescriptorArray { get }
```

## Discussion

This property holds an array of [MTLPipelineBufferDescriptor](../mtlpipelinebufferdescriptor.md) instances, where each index corresponds to the same entry in the buffer argument table.

Metal can perform additional optimizations if you guarantee that neither the CPU nor the GPU modify a buffer’s contents after set in a function’s argument table and before its command buffer completes. Use immutable buffers as much as possible, for either regular buffers or argument buffers.

```objective-c
// Compute setup.
// Set mutability for buffer at index 9.
MTLComputePipelineDescriptor *computeDescriptor = [MTLComputePipelineDescriptor new];
computeDescriptor.buffers[9].mutability = MTLMutabilityImmutable;
// Compute pass.
// Set immutable buffer at index 9.
id <MTLComputeCommandEncoder> computeEncoder = [_commandBuffer computeCommandEncoder];
[computeEncoder setBuffer:_buffer offset:0 atIndex:9];
```
