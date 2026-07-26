---
title: 'makeRenderCommandEncoder(descriptor:options:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandbuffer/makerendercommandencoder(descriptor:options:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandbuffer/makerendercommandencoder(descriptor:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandbuffer/makerendercommandencoder%28descriptor%3Aoptions%3A%29.json'
content_hash: 'sha256:4d9589c440dccac0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandBuffer](../mtl4commandbuffer.md)

# makeRenderCommandEncoder(descriptor:options:)

<sub>Instance Method</sub>

Creates a render command encoder from a render pass descriptor with additional options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeRenderCommandEncoder(descriptor: MTL4RenderPassDescriptor, options: MTL4RenderEncoderOptions = []) -> (any MTL4RenderCommandEncoder)?
```

## Parameters

- `descriptor` — Descriptor for the render pass.

- `options` — [MTL4RenderEncoderOptions](../mtl4renderencoderoptions.md) instance that provide render pass options.

## Return Value

The created [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md) instance, or `nil` if the function fails.

## Discussion

This method creates a render command encoder to encode a render pass, whilst providing you the option to define some render pass characteristics via an instance of [MTL4RenderEncoderOptions](../mtl4renderencoderoptions.md).

Use these options to configure suspending/resuming render command encoders, which allow you to encode render passes from multiple threads simultaneously.
