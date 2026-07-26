---
title: 'makeRenderPipelineState(descriptor:options:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makerenderpipelinestate(descriptor:options:)-yrak'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makerenderpipelinestate(descriptor:options:)-yrak'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makerenderpipelinestate%28descriptor%3Aoptions%3A%29-yrak.json'
content_hash: 'sha256:cf87e30d0ee90c5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeRenderPipelineState(descriptor:options:)

<sub>Instance Method</sub>

Synchronously creates a mesh render pipeline state and reflection information in a tuple.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeRenderPipelineState(descriptor: MTLMeshRenderPipelineDescriptor, options: MTLPipelineOption) throws -> (any MTLRenderPipelineState, MTLRenderPipelineReflection?)
```

## Parameters

- `descriptor` — An [MTLMeshRenderPipelineDescriptor](../mtlmeshrenderpipelinedescriptor.md) instance.

- `options` — An [MTLPipelineOption](../mtlpipelineoption.md) instance that represents the reflection information you want the method to generate.

## Return Value

A tuple with a new [MTLRenderPipelineState](../mtlrenderpipelinestate.md) instance and an [MTLRenderPipelineReflection](../mtlrenderpipelinereflection.md) optional instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

## Discussion

Use the graphics-rendering pipeline state to configure a render pass by calling the [- setRenderPipelineState:](<../mtlrendercommandencoder/setrenderpipelinestate(__).md>) method of an [MTLRenderCommandEncoder](../mtlrendercommandencoder.md) instance.

## See Also

### Creating render pipeline states with mesh shaders

- [- newRenderPipelineStateWithMeshDescriptor:options:completionHandler:](<makerenderpipelinestate(descriptor_options_completionhandler_)-1wvya.md>) — Asynchronously creates a mesh render pipeline state and reflection information.
