---
title: MTLPipelineOption
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlpipelineoption
source_url: 'https://developer.apple.com/documentation/metal/mtlpipelineoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpipelineoption.json'
content_hash: 'sha256:a70623d25c25762e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLPipelineOption

<sub>Structure</sub>

Options that determine how Metal prepares the pipeline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLPipelineOption
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Retrieving argument information

- [MTLPipelineOptionBufferTypeInfo](mtlpipelineoption/buffertypeinfo.md) — An option instance that provides detailed buffer type information for buffer arguments.
- [MTLPipelineOptionFailOnBinaryArchiveMiss](mtlpipelineoption/failonbinaryarchivemiss.md) — An option that instructs the compiler to return an error when a GPU function isn’t in a binary archive.
- [MTLPipelineOptionArgumentInfo](mtlpipelineoption/argumentinfo.md) — An option instance that provides argument information for textures and threadgroup memory. _(deprecated)_

### Creating compilation options

- [init(rawValue:)](<mtlpipelineoption/init(rawvalue_).md>) — Creates empty compilation options.

### Type properties

- [MTLPipelineOptionBindingInfo](mtlpipelineoption/bindinginfo.md) — An option that provides binding information for pipeline state resources.

## See Also

### Configuring a compute pipeline state

- [MTL4ComputePipelineDescriptor](mtl4computepipelinedescriptor.md) — Describes a compute pipeline state.
- [MTLComputePipelineDescriptor](mtlcomputepipelinedescriptor.md) — An instance describing the desired GPU state for a kernel call in a compute pass.
- [MTLComputePipelineState](mtlcomputepipelinestate.md) — An interface that represents a GPU pipeline configuration for running kernels in a compute pass.
- [MTLStageInputOutputDescriptor](mtlstageinputoutputdescriptor.md) — A description of the input and output data of a function.
- [MTLPipelineBufferDescriptor](mtlpipelinebufferdescriptor.md) — The mutability options for a buffer that a render or compute pipeline uses.
- [MTLPipelineBufferDescriptorArray](mtlpipelinebufferdescriptorarray.md) — An array of pipeline buffer descriptors.
