---
title: Command encoder factory methods
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/command-encoder-factory-methods
source_url: 'https://developer.apple.com/documentation/metal/command-encoder-factory-methods'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/command-encoder-factory-methods.json'
content_hash: 'sha256:08f76eb35be1256e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [GPU devices and work submission](gpu-devices-and-work-submission.md) · [MTLCommandBuffer](mtlcommandbuffer.md)

# Command encoder factory methods

<sub>API Collection</sub>

A command encoder defines the actions of a single pass, such as GPU commands that draw, compute, or quickly copy resource data.

## Topics

### Creating render encoders

- [- renderCommandEncoderWithDescriptor:](<mtlcommandbuffer/makerendercommandencoder(descriptor_).md>) — Creates a render command encoder from a descriptor.

### Creating parallel render encoders

- [- parallelRenderCommandEncoderWithDescriptor:](<mtlcommandbuffer/makeparallelrendercommandencoder(descriptor_).md>) — Creates a parallel render command encoder from a descriptor.

### Creating acceleration structure encoders

- [- accelerationStructureCommandEncoderWithDescriptor:](<mtlcommandbuffer/makeaccelerationstructurecommandencoder(descriptor_).md>) — Creates a ray-tracing acceleration structure command encoder from a descriptor.
- [- accelerationStructureCommandEncoder](<mtlcommandbuffer/makeaccelerationstructurecommandencoder().md>) — Creates a ray-tracing acceleration structure command encoder that uses default settings.

### Creating compute encoders

- [- computeCommandEncoderWithDescriptor:](<mtlcommandbuffer/makecomputecommandencoder(descriptor_).md>) — Creates a compute command encoder from a descriptor.
- [- computeCommandEncoder](<mtlcommandbuffer/makecomputecommandencoder().md>) — Creates a compute command encoder that uses default settings.
- [- computeCommandEncoderWithDispatchType:](<mtlcommandbuffer/makecomputecommandencoder(dispatchtype_).md>) — Creates a compute command encoder with a dispatch type.
- [MTLDispatchType](mtldispatchtype.md) — The type of dispatch method to use when calling encoded functions.

### Creating blit encoders

- [- blitCommandEncoder](<mtlcommandbuffer/makeblitcommandencoder().md>) — Creates a block information transfer (blit) encoder.
- [- blitCommandEncoderWithDescriptor:](<mtlcommandbuffer/makeblitcommandencoder(descriptor_).md>) — Creates a block information transfer (blit) encoder from a descriptor.

### Creating resource state encoders

- [- resourceStateCommandEncoderWithDescriptor:](<mtlcommandbuffer/resourcestatecommandencoder(with_).md>) — Creates a resource state command encoder from a descriptor.
- [- resourceStateCommandEncoder](<mtlcommandbuffer/makeresourcestatecommandencoder().md>) — Creates a resource state command encoder that uses default settings.
