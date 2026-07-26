---
title: 'makeRenderPipelineState(descriptor:options:reflection:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makerenderpipelinestate(descriptor:options:reflection:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makerenderpipelinestate(descriptor:options:reflection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makerenderpipelinestate%28descriptor%3Aoptions%3Areflection%3A%29.json'
content_hash: 'sha256:5b34ad82cdae5f96'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeRenderPipelineState(descriptor:options:reflection:)

<sub>Instance Method</sub>

Synchronously creates a render pipeline state and reflection information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, options: MTLPipelineOption, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedRenderPipelineReflection?>?) throws -> any MTLRenderPipelineState
```

## Parameters

- `descriptor` — An [MTLRenderPipelineDescriptor](../mtlrenderpipelinedescriptor.md) instance.

- `options` — An [MTLPipelineOption](../mtlpipelineoption.md) instance that represents the reflection information you want the method to generate.

- `reflection` — In Swift, an optional pointer to an [MTLAutoreleasedRenderPipelineReflection](../mtlautoreleasedrenderpipelinereflection.md) optional. In Objective-C, a pointer to an [MTLAutoreleasedRenderPipelineReflection](../mtlautoreleasedrenderpipelinereflection.md) instance. Pass `nil` in either language when you don’t need reflection data. Otherwise on return, if the method completes successfully, it assigns an [MTLRenderPipelineReflection](../mtlrenderpipelinereflection.md) instance to the pointee, which contains the details about the function arguments.

## Return Value

A new [MTLRenderPipelineState](../mtlrenderpipelinestate.md) instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

## Discussion

Use the graphics-rendering pipeline state to configure a render pass by calling the [- setRenderPipelineState:](<../mtlrendercommandencoder/setrenderpipelinestate(__).md>) method of an [MTLRenderCommandEncoder](../mtlrendercommandencoder.md) instance.

## See Also

### Creating render pipeline states with vertex shaders

- [- newRenderPipelineStateWithDescriptor:error:](<makerenderpipelinestate(descriptor_).md>) — Synchronously creates a render pipeline state.
- [- newRenderPipelineStateWithDescriptor:completionHandler:](<makerenderpipelinestate(descriptor_completionhandler_).md>) — Asynchronously creates a render pipeline state.
- [makeRenderPipelineState(descriptor:options:)](<makerenderpipelinestate(descriptor_options_)-89vxc.md>) — Synchronously creates a render pipeline state and reflection information in a tuple.
- [- newRenderPipelineStateWithDescriptor:options:completionHandler:](<makerenderpipelinestate(descriptor_options_completionhandler_)-5gdww.md>) — Asynchronously creates a render pipeline state and reflection information.
