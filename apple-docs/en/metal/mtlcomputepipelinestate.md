---
title: MTLComputePipelineState
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcomputepipelinestate
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepipelinestate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepipelinestate.json'
content_hash: 'sha256:8335a183915eb3ca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLComputePipelineState

<sub>Protocol</sub>

An interface that represents a GPU pipeline configuration for running kernels in a compute pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLComputePipelineState : MTLAllocation, Sendable
```

## Overview

The [MTLComputePipelineState](mtlcomputepipelinestate.md) protocol is an interface that represents a specific configuration for the GPU pipeline for a compute pass. Use a pipeline state to configure a compute pass by calling the [- setComputePipelineState:](<mtlcomputecommandencoder/setcomputepipelinestate(__).md>) method of an [MTLComputeCommandEncoder](mtlcomputecommandencoder.md) instance.

To create a pipeline state, call the appropriate [MTLDevice](mtldevice.md) method (see [Pipeline state creation](pipeline-state-creation.md)). You typically make pipeline states at a noncritical time, like when your app first launches. This is because graphics drivers may need time to evaluate and build each pipeline state. However, you can quickly use and reuse each pipeline state throughout your app’s lifetime.

## Relationships

- **Inherits From**: [MTLAllocation](mtlallocation.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Identifying a pipeline state

- [device](mtlcomputepipelinestate/device.md) — The device instance that created the pipeline state.
- [gpuResourceID](mtlcomputepipelinestate/gpuresourceid.md) — An unique identifier that represents the pipeline state, which you can add to an argument buffer.
- [label](mtlcomputepipelinestate/label.md) — A string that helps you identify the compute pipeline state during debugging.

### Checking threadgroup attributes

- [maxTotalThreadsPerThreadgroup](mtlcomputepipelinestate/maxtotalthreadsperthreadgroup.md) — The maximum number of threads in a threadgroup that you can dispatch to the pipeline.
- [threadExecutionWidth](mtlcomputepipelinestate/threadexecutionwidth.md) — The number of threads that the GPU executes simultaneously.
- [staticThreadgroupMemoryLength](mtlcomputepipelinestate/staticthreadgroupmemorylength.md) — The length, in bytes, of statically allocated threadgroup memory.

### Checking imageblock attributes

- [- imageblockMemoryLengthForDimensions:](<mtlcomputepipelinestate/imageblockmemorylength(fordimensions_).md>) — Returns the length of reserved memory for an imageblock of a given size.

### Checking indirect command buffer support

- [supportIndirectCommandBuffers](mtlcomputepipelinestate/supportindirectcommandbuffers.md) — A Boolean value that indicates whether the compute pipeline supports indirect command buffers.

### Checking shader validation

- [shaderValidation](mtlcomputepipelinestate/shadervalidation.md) — The current state of shader validation for the pipeline.

### Creating function handles

- [- functionHandleWithFunction:](<mtlcomputepipelinestate/functionhandle(function_)-7d523.md>) — Creates a function handle for a visible function.

### Adding visible functions

- [- newComputePipelineStateWithAdditionalBinaryFunctions:error:](<mtlcomputepipelinestate/makecomputepipelinestatewithadditionalbinaryfunctions(functions_).md>) — Creates a new pipeline state object with additional callable functions.

### Creating function tables

- [- newVisibleFunctionTableWithDescriptor:](<mtlcomputepipelinestate/makevisiblefunctiontable(descriptor_).md>) — Creates a new visible function table.
- [- newIntersectionFunctionTableWithDescriptor:](<mtlcomputepipelinestate/makeintersectionfunctiontable(descriptor_).md>) — Creates a new intersection function table.

### Instance Properties

- [reflection](mtlcomputepipelinestate/reflection.md) — The compute pipeline’s reflection information, if available.
- [requiredThreadsPerThreadgroup](mtlcomputepipelinestate/requiredthreadsperthreadgroup.md)

### Instance Methods

- [- functionHandleWithBinaryFunction:](<mtlcomputepipelinestate/functionhandle(function_)-8spaa.md>) — Gets the function handle for a function this pipeline links at the binary level.
- [- functionHandleWithName:](<mtlcomputepipelinestate/functionhandle(withname_).md>) — Gets the function handle for a function this pipeline links at the Metal IR level by name.
- [- newComputePipelineStateWithBinaryFunctions:error:](<mtlcomputepipelinestate/makecomputepipelinestate(additionalbinaryfunctions_).md>) — Allocates a new compute pipeline state by adding binary functions to this pipeline state.

## See Also

### Configuring a compute pipeline state

- [MTL4ComputePipelineDescriptor](mtl4computepipelinedescriptor.md) — Describes a compute pipeline state.
- [MTLComputePipelineDescriptor](mtlcomputepipelinedescriptor.md) — An instance describing the desired GPU state for a kernel call in a compute pass.
- [MTLStageInputOutputDescriptor](mtlstageinputoutputdescriptor.md) — A description of the input and output data of a function.
- [MTLPipelineBufferDescriptor](mtlpipelinebufferdescriptor.md) — The mutability options for a buffer that a render or compute pipeline uses.
- [MTLPipelineBufferDescriptorArray](mtlpipelinebufferdescriptorarray.md) — An array of pipeline buffer descriptors.
- [MTLPipelineOption](mtlpipelineoption.md) — Options that determine how Metal prepares the pipeline.
