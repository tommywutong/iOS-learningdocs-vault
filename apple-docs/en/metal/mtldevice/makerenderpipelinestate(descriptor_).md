---
title: 'makeRenderPipelineState(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makerenderpipelinestate(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makerenderpipelinestate(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makerenderpipelinestate%28descriptor%3A%29.json'
content_hash: 'sha256:f0c27aebf10f9135'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeRenderPipelineState(descriptor:)

<sub>Instance Method</sub>

Synchronously creates a render pipeline state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor) throws -> any MTLRenderPipelineState
```

## Parameters

- `descriptor` — An [MTLRenderPipelineDescriptor](../mtlrenderpipelinedescriptor.md) instance.

## Return Value

A new [MTLRenderPipelineState](../mtlrenderpipelinestate.md) instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

## Discussion

Use the graphics-rendering pipeline state to configure a render pass by calling the [- setRenderPipelineState:](<../mtlrendercommandencoder/setrenderpipelinestate(__).md>) method of an [MTLRenderCommandEncoder](../mtlrendercommandencoder.md) instance.

## See Also

### Creating render pipeline states with vertex shaders

- [- newRenderPipelineStateWithDescriptor:completionHandler:](<makerenderpipelinestate(descriptor_completionhandler_).md>) — Asynchronously creates a render pipeline state.
- [makeRenderPipelineState(descriptor:options:)](<makerenderpipelinestate(descriptor_options_)-89vxc.md>) — Synchronously creates a render pipeline state and reflection information in a tuple.
- [- newRenderPipelineStateWithDescriptor:options:reflection:error:](<makerenderpipelinestate(descriptor_options_reflection_).md>) — Synchronously creates a render pipeline state and reflection information.
- [- newRenderPipelineStateWithDescriptor:options:completionHandler:](<makerenderpipelinestate(descriptor_options_completionhandler_)-5gdww.md>) — Asynchronously creates a render pipeline state and reflection information.
