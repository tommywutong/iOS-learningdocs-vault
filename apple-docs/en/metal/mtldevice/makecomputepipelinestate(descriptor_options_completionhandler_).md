---
title: 'makeComputePipelineState(descriptor:options:completionHandler:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makecomputepipelinestate(descriptor:options:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makecomputepipelinestate(descriptor:options:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makecomputepipelinestate%28descriptor%3Aoptions%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:570163a07c390be2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeComputePipelineState(descriptor:options:completionHandler:)

<sub>Instance Method</sub>

Asynchronously creates a compute pipeline state and reflection information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeComputePipelineState(descriptor: MTLComputePipelineDescriptor, options: MTLPipelineOption, completionHandler: @escaping @Sendable ((any MTLComputePipelineState)?, MTLComputePipelineReflection?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeComputePipelineState(descriptor: MTLComputePipelineDescriptor, options: MTLPipelineOption) async throws -> (any MTLComputePipelineState, MTLComputePipelineReflection?)
```

## Parameters

- `descriptor` — An [MTLComputePipelineDescriptor](../mtlcomputepipelinedescriptor.md) instance.

- `options` — An [MTLPipelineOption](../mtlpipelineoption.md) instance that represents the reflection information you want the method to generate.

- `completionHandler` — A Swift closure or an Objective-C block the method calls when it finishes creating the compute pipeline state.

## Discussion

Use the compute pipeline state to configure a compute pass by calling the [- setComputePipelineState:](<../mtlcomputecommandencoder/setcomputepipelinestate(__).md>) method of an [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md) instance.

## Default Implementations

### MTLDevice Implementations

- [makeComputePipelineState(descriptor:options:)](<makecomputepipelinestate(descriptor_options_).md>)

## See Also

### Creating compute pipeline states

- [- newComputePipelineStateWithDescriptor:options:reflection:error:](<makecomputepipelinestate(descriptor_options_reflection_).md>) — Synchronously creates a compute pipeline state and reflection information.
- [- newComputePipelineStateWithFunction:error:](<makecomputepipelinestate(function_).md>) — Synchronously creates a compute pipeline state with a function instance.
- [- newComputePipelineStateWithFunction:completionHandler:](<makecomputepipelinestate(function_completionhandler_).md>) — Asynchronously creates a compute pipeline state with a function instance.
- [- newComputePipelineStateWithFunction:options:reflection:error:](<makecomputepipelinestate(function_options_reflection_).md>) — Synchronously creates a compute pipeline state and reflection with a function instance.
- [- newComputePipelineStateWithFunction:options:completionHandler:](<makecomputepipelinestate(function_options_completionhandler_).md>) — Asynchronously creates a compute pipeline state and reflection with a function instance.
