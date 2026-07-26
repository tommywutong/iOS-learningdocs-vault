---
title: 'makeRenderPipelineState(descriptor:options:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.11+, tvOS 9.0+, visionOS]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makerenderpipelinestate(descriptor:options:)-89vxc'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makerenderpipelinestate(descriptor:options:)-89vxc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makerenderpipelinestate%28descriptor%3Aoptions%3A%29-89vxc.json'
content_hash: 'sha256:3de957655885b4a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeRenderPipelineState(descriptor:options:)

<sub>Instance Method</sub>

Synchronously creates a render pipeline state and reflection information in a tuple.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, options: MTLPipelineOption) throws -> (any MTLRenderPipelineState, MTLRenderPipelineReflection?)
```

## Parameters

- `descriptor` — An [MTLRenderPipelineDescriptor](../mtlrenderpipelinedescriptor.md) instance.

- `options` — An [MTLPipelineOption](../mtlpipelineoption.md) instance that represents the reflection information you want the method to generate.

## Return Value

A tuple with a new [MTLRenderPipelineState](../mtlrenderpipelinestate.md) instance and an [MTLRenderPipelineReflection](../mtlrenderpipelinereflection.md) optional instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

## Discussion

Use the graphics-rendering pipeline state to configure a render pass by calling the [- setRenderPipelineState:](<../mtlrendercommandencoder/setrenderpipelinestate(__).md>) method of an [MTLRenderCommandEncoder](../mtlrendercommandencoder.md) instance.

## See Also

### Creating render pipeline states with vertex shaders

- [- newRenderPipelineStateWithDescriptor:error:](<makerenderpipelinestate(descriptor_).md>) — Synchronously creates a render pipeline state.
- [- newRenderPipelineStateWithDescriptor:completionHandler:](<makerenderpipelinestate(descriptor_completionhandler_).md>) — Asynchronously creates a render pipeline state.
- [- newRenderPipelineStateWithDescriptor:options:reflection:error:](<makerenderpipelinestate(descriptor_options_reflection_).md>) — Synchronously creates a render pipeline state and reflection information.
- [- newRenderPipelineStateWithDescriptor:options:completionHandler:](<makerenderpipelinestate(descriptor_options_completionhandler_)-5gdww.md>) — Asynchronously creates a render pipeline state and reflection information.
