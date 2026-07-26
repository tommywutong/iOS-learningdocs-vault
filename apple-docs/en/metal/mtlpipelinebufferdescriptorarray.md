---
title: MTLPipelineBufferDescriptorArray
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlpipelinebufferdescriptorarray
source_url: 'https://developer.apple.com/documentation/metal/mtlpipelinebufferdescriptorarray'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpipelinebufferdescriptorarray.json'
content_hash: 'sha256:2e3bc150e110815d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLPipelineBufferDescriptorArray

<sub>Class</sub>

An array of pipeline buffer descriptors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLPipelineBufferDescriptorArray
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing array elements

- [- objectAtIndexedSubscript:](<mtlpipelinebufferdescriptorarray/subscript(__).md>) — Returns the pipeline buffer descriptor at the specified array index.

## See Also

### Configuring a compute pipeline state

- [MTL4ComputePipelineDescriptor](mtl4computepipelinedescriptor.md) — Describes a compute pipeline state.
- [MTLComputePipelineDescriptor](mtlcomputepipelinedescriptor.md) — An instance describing the desired GPU state for a kernel call in a compute pass.
- [MTLComputePipelineState](mtlcomputepipelinestate.md) — An interface that represents a GPU pipeline configuration for running kernels in a compute pass.
- [MTLStageInputOutputDescriptor](mtlstageinputoutputdescriptor.md) — A description of the input and output data of a function.
- [MTLPipelineBufferDescriptor](mtlpipelinebufferdescriptor.md) — The mutability options for a buffer that a render or compute pipeline uses.
- [MTLPipelineOption](mtlpipelineoption.md) — Options that determine how Metal prepares the pipeline.
