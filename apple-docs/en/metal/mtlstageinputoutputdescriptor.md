---
title: MTLStageInputOutputDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstageinputoutputdescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlstageinputoutputdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstageinputoutputdescriptor.json'
content_hash: 'sha256:8266da1f57b62ad9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLStageInputOutputDescriptor

<sub>Class</sub>

A description of the input and output data of a function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLStageInputOutputDescriptor
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Describing argument layouts

- [attributes](mtlstageinputoutputdescriptor/attributes.md) — An array that describes where and how to fetch data for the function.
- [layouts](mtlstageinputoutputdescriptor/layouts.md) — An array that describes how the function fetches data.

### Declaring index buffers for indirect compute commands

- [indexBufferIndex](mtlstageinputoutputdescriptor/indexbufferindex.md) — The location of the index buffer for a compute function using indexed thread addressing.
- [indexType](mtlstageinputoutputdescriptor/indextype.md) — The data type of the indices stored in the index buffer.

### Resetting the descriptor

- [- reset](<mtlstageinputoutputdescriptor/reset().md>) — Resets the default state for the descriptor.

## See Also

### Configuring a compute pipeline state

- [MTL4ComputePipelineDescriptor](mtl4computepipelinedescriptor.md) — Describes a compute pipeline state.
- [MTLComputePipelineDescriptor](mtlcomputepipelinedescriptor.md) — An instance describing the desired GPU state for a kernel call in a compute pass.
- [MTLComputePipelineState](mtlcomputepipelinestate.md) — An interface that represents a GPU pipeline configuration for running kernels in a compute pass.
- [MTLPipelineBufferDescriptor](mtlpipelinebufferdescriptor.md) — The mutability options for a buffer that a render or compute pipeline uses.
- [MTLPipelineBufferDescriptorArray](mtlpipelinebufferdescriptorarray.md) — An array of pipeline buffer descriptors.
- [MTLPipelineOption](mtlpipelineoption.md) — Options that determine how Metal prepares the pipeline.
