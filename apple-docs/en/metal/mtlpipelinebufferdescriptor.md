---
title: MTLPipelineBufferDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlpipelinebufferdescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlpipelinebufferdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpipelinebufferdescriptor.json'
content_hash: 'sha256:48b674a1f8c45b04'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLPipelineBufferDescriptor

<sub>Class</sub>

The mutability options for a buffer that a render or compute pipeline uses.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLPipelineBufferDescriptor
```

## Overview

Metal can perform additional optimizations if you guarantee that neither the CPU nor the GPU modify a buffer’s contents before starting a pass. Use immutable buffers as much as possible to take advantage of Metal optimizations.

To declare that a buffer is immutable, set the [mutability](mtlpipelinebufferdescriptor/mutability.md) property of their associated [MTLPipelineBufferDescriptor](mtlpipelinebufferdescriptor.md) object to [MTLMutabilityImmutable](mtlmutability/immutable.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Setting buffer mutability

- [mutability](mtlpipelinebufferdescriptor/mutability.md) — A mutability option that determines whether you can update a buffer’s contents before related commands use the buffer.
- [MTLMutability](mtlmutability.md) — The options that determine the mutability of a buffer’s contents.

## See Also

### Configuring a compute pipeline state

- [MTL4ComputePipelineDescriptor](mtl4computepipelinedescriptor.md) — Describes a compute pipeline state.
- [MTLComputePipelineDescriptor](mtlcomputepipelinedescriptor.md) — An instance describing the desired GPU state for a kernel call in a compute pass.
- [MTLComputePipelineState](mtlcomputepipelinestate.md) — An interface that represents a GPU pipeline configuration for running kernels in a compute pass.
- [MTLStageInputOutputDescriptor](mtlstageinputoutputdescriptor.md) — A description of the input and output data of a function.
- [MTLPipelineBufferDescriptorArray](mtlpipelinebufferdescriptorarray.md) — An array of pipeline buffer descriptors.
- [MTLPipelineOption](mtlpipelineoption.md) — Options that determine how Metal prepares the pipeline.
