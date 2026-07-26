---
title: 'commit(_:options:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandqueue/commit(_:options:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandqueue/commit(_:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandqueue/commit%28_%3Aoptions%3A%29.json'
content_hash: 'sha256:4b082c5833fb094c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandQueue](../mtl4commandqueue.md)

# commit(_:options:)

<sub>Instance Method</sub>

Enqueues an array of command buffer instances for execution with a set of options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func commit(_ commandBuffers: [any MTL4CommandBuffer], options: MTL4CommitOptions? = nil)
```

## Parameters

- `commandBuffers` — A Swift array of `MTL4CommandBuffers` to commit.

- `options` — An instance of [MTL4CommitOptions](../mtl4commitoptions.md) that configures the commit operation.

## Discussion

Provide an [MTL4CommitOptions](../mtl4commitoptions.md) instance to configure the commit operation.

The order in which you sort the command buffers in the array is meaningful, especially when it contains suspending/resuming render passes. A suspending/resuming render pass is a render pass you create by calling [- renderCommandEncoderWithDescriptor:options:](<../mtl4commandbuffer/makerendercommandencoder(descriptor_options_).md>), and provide `MTL4RenderEncoderOptionSuspending` or `MTL4RenderEncoderOptionResuming` for the `options` parameter.

If your command buffers contain suspend/resume render passes, ensure that the first command buffer only suspends, and the last one only resumes. Additionally, make sure that all intermediate command buffers are both suspending and resuming.

When you commit work from multiple threads, modifying and reusing the same options instance, you are responsible for externally synchronizing access to it.
