---
title: 'setRenderPipelineState(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setrenderpipelinestate(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setrenderpipelinestate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setrenderpipelinestate%28_%3A%29.json'
content_hash: 'sha256:cb075a2c0fa76e87'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setRenderPipelineState(_:)

<sub>Instance Method</sub>

Configures the encoder with a render or tile pipeline state that applies to your subsequent draw commands.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setRenderPipelineState(_ pipelineState: any MTLRenderPipelineState)
```

## Parameters

- `pipelineState` — A render pipeline state that you create by calling an [MTLDevice](../mtldevice.md) methods (see [Pipeline state creation](../pipeline-state-creation.md)).

## Discussion

Set the render pass’s render pipeline state before encoding any draw or tile commands by calling this method because the default pipeline state is `nil`.

You can change which pipeline state the encoder uses multiple times during its lifetime. For example, your app may want render some things with a vertex shader, and render others with an object and mesh shader. Changing the pipeline state only affects the subsequent commands and has no effect on the commands you encode before changing the state.

The render pipeline you pass to this method needs to be compatible with the render pass’s attachments. You configure these attachments with the properties of an [MTLRenderPassDescriptor](../mtlrenderpassdescriptor.md) instance, including [colorAttachments](../mtlrenderpassdescriptor/colorattachments.md), [depthAttachment](../mtlrenderpassdescriptor/depthattachment.md), and [stencilAttachment](../mtlrenderpassdescriptor/stencilattachment.md).
