---
title: 'makeComputePipelineState(descriptor:options:reflection:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makecomputepipelinestate(descriptor:options:reflection:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makecomputepipelinestate(descriptor:options:reflection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makecomputepipelinestate%28descriptor%3Aoptions%3Areflection%3A%29.json'
content_hash: 'sha256:8919e9a143c524f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeComputePipelineState(descriptor:options:reflection:)

<sub>Instance Method</sub>

Synchronously creates a compute pipeline state and reflection information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeComputePipelineState(descriptor: MTLComputePipelineDescriptor, options: MTLPipelineOption, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedComputePipelineReflection?>?) throws -> any MTLComputePipelineState
```

## Parameters

- `descriptor` — An [MTLComputePipelineDescriptor](../mtlcomputepipelinedescriptor.md) instance.

- `options` — An [MTLPipelineOption](../mtlpipelineoption.md) instance that represents the reflection information you want the method to generate.

- `reflection` — In Swift, an optional pointer to an [MTLAutoreleasedComputePipelineReflection](../mtlautoreleasedcomputepipelinereflection.md) optional. In Objective-C, a pointer to an [MTLAutoreleasedComputePipelineReflection](../mtlautoreleasedcomputepipelinereflection.md) instance. Pass `nil` in either language when you don’t need reflection data. Otherwise on return, if the method completes successfully, it assigns an [MTLComputePipelineReflection](../mtlcomputepipelinereflection.md) instance to the pointee, which contains the details about the function arguments.

## Discussion

Use the compute pipeline state to configure a compute pass by calling the [- setComputePipelineState:](<../mtlcomputecommandencoder/setcomputepipelinestate(__).md>) method of an [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md) instance.

## See Also

### Creating compute pipeline states

- [- newComputePipelineStateWithDescriptor:options:completionHandler:](<makecomputepipelinestate(descriptor_options_completionhandler_).md>) — Asynchronously creates a compute pipeline state and reflection information.
- [- newComputePipelineStateWithFunction:error:](<makecomputepipelinestate(function_).md>) — Synchronously creates a compute pipeline state with a function instance.
- [- newComputePipelineStateWithFunction:completionHandler:](<makecomputepipelinestate(function_completionhandler_).md>) — Asynchronously creates a compute pipeline state with a function instance.
- [- newComputePipelineStateWithFunction:options:reflection:error:](<makecomputepipelinestate(function_options_reflection_).md>) — Synchronously creates a compute pipeline state and reflection with a function instance.
- [- newComputePipelineStateWithFunction:options:completionHandler:](<makecomputepipelinestate(function_options_completionhandler_).md>) — Asynchronously creates a compute pipeline state and reflection with a function instance.
