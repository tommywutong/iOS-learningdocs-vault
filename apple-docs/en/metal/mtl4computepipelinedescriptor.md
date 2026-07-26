---
title: MTL4ComputePipelineDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4computepipelinedescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtl4computepipelinedescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computepipelinedescriptor.json'
content_hash: 'sha256:213eb815e3781993'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4ComputePipelineDescriptor

<sub>Class</sub>

Describes a compute pipeline state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTL4ComputePipelineDescriptor
```

## Relationships

- **Inherits From**: [MTL4PipelineDescriptor](mtl4pipelinedescriptor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [computeFunctionDescriptor](mtl4computepipelinedescriptor/computefunctiondescriptor.md) — A descriptor representing the compute pipeline’s function.
- [maxTotalThreadsPerThreadgroup](mtl4computepipelinedescriptor/maxtotalthreadsperthreadgroup.md) — The maximum total number of threads that Metal can execute in a single threadgroup for the compute function.
- [requiredThreadsPerThreadgroup](mtl4computepipelinedescriptor/requiredthreadsperthreadgroup.md) — The required number of threads per threadgroup for compute dispatches.
- [staticLinkingDescriptor](mtl4computepipelinedescriptor/staticlinkingdescriptor.md) — An object that contains information about functions to link to the compute pipeline.
- [supportBinaryLinking](mtl4computepipelinedescriptor/supportbinarylinking.md) — A boolean value indicating whether the compute pipeline supports linking binary functions.
- [supportIndirectCommandBuffers](mtl4computepipelinedescriptor/supportindirectcommandbuffers.md) — A value indicating whether the pipeline supports Metal indirect command buffers.
- [threadGroupSizeIsMultipleOfThreadExecutionWidth](mtl4computepipelinedescriptor/threadgroupsizeismultipleofthreadexecutionwidth.md) — A boolean value indicating whether each dimension of the threadgroup size is a multiple of its corresponding thread execution width.

### Instance Methods

- [- reset](<mtl4computepipelinedescriptor/reset().md>) — Resets the descriptor to its default values.

## See Also

### Configuring a compute pipeline state

- [MTLComputePipelineDescriptor](mtlcomputepipelinedescriptor.md) — An instance describing the desired GPU state for a kernel call in a compute pass.
- [MTLComputePipelineState](mtlcomputepipelinestate.md) — An interface that represents a GPU pipeline configuration for running kernels in a compute pass.
- [MTLStageInputOutputDescriptor](mtlstageinputoutputdescriptor.md) — A description of the input and output data of a function.
- [MTLPipelineBufferDescriptor](mtlpipelinebufferdescriptor.md) — The mutability options for a buffer that a render or compute pipeline uses.
- [MTLPipelineBufferDescriptorArray](mtlpipelinebufferdescriptorarray.md) — An array of pipeline buffer descriptors.
- [MTLPipelineOption](mtlpipelineoption.md) — Options that determine how Metal prepares the pipeline.
