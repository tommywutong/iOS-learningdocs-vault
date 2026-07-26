---
title: 'makeRenderPipelineState(descriptor:options:completionHandler:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makerenderpipelinestate(descriptor:options:completionhandler:)-5gdww'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makerenderpipelinestate(descriptor:options:completionhandler:)-5gdww'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makerenderpipelinestate%28descriptor%3Aoptions%3Acompletionhandler%3A%29-5gdww.json'
content_hash: 'sha256:1e6b3041c013a3f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeRenderPipelineState(descriptor:options:completionHandler:)

<sub>Instance Method</sub>

Asynchronously creates a render pipeline state and reflection information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, options: MTLPipelineOption, completionHandler: @escaping @Sendable ((any MTLRenderPipelineState)?, MTLRenderPipelineReflection?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, options: MTLPipelineOption) async throws -> (any MTLRenderPipelineState, MTLRenderPipelineReflection?)
```

## Parameters

- `descriptor` — An [MTLRenderPipelineDescriptor](../mtlrenderpipelinedescriptor.md) instance.

- `options` — An [MTLPipelineOption](../mtlpipelineoption.md) instance that represents the reflection information you want the method to generate.

- `completionHandler` — A Swift closure or an Objective-C block the method calls when it finishes creating the render pipeline state.

## Discussion

Use the graphics-rendering pipeline state to configure a render pass by calling the [- setRenderPipelineState:](<../mtlrendercommandencoder/setrenderpipelinestate(__).md>) method of an [MTLRenderCommandEncoder](../mtlrendercommandencoder.md) instance.

## Default Implementations

### MTLDevice Implementations

- [makeRenderPipelineState(descriptor:options:)](<makerenderpipelinestate(descriptor_options_)-89vxc.md>) — Synchronously creates a render pipeline state and reflection information in a tuple.
- [makeRenderPipelineState(descriptor:options:)](<makerenderpipelinestate(descriptor_options_)-yrak.md>) — Synchronously creates a mesh render pipeline state and reflection information in a tuple.

## See Also

### Creating render pipeline states with vertex shaders

- [- newRenderPipelineStateWithDescriptor:error:](<makerenderpipelinestate(descriptor_).md>) — Synchronously creates a render pipeline state.
- [- newRenderPipelineStateWithDescriptor:completionHandler:](<makerenderpipelinestate(descriptor_completionhandler_).md>) — Asynchronously creates a render pipeline state.
- [makeRenderPipelineState(descriptor:options:)](<makerenderpipelinestate(descriptor_options_)-89vxc.md>) — Synchronously creates a render pipeline state and reflection information in a tuple.
- [- newRenderPipelineStateWithDescriptor:options:reflection:error:](<makerenderpipelinestate(descriptor_options_reflection_).md>) — Synchronously creates a render pipeline state and reflection information.
