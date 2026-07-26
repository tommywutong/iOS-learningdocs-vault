---
title: 'commit:count:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandqueue/commit:count:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandqueue/commit:count:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandqueue/commit%3Acount%3A.json'
content_hash: 'sha256:760aee48abd6aeff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandQueue](../mtl4commandqueue.md)

# commit:count:

<sub>Instance Method</sub>

Enqueues an array of command buffers for execution.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) commit:(id<MTL4CommandBuffer> const[]) commandBuffers count:(NSUInteger) count;
```

## Parameters

- `commandBuffers` — An array of [MTL4CommandBuffer](../mtl4commandbuffer.md).

- `count` — The number of [MTL4CommandBuffer](../mtl4commandbuffer.md) instances in the `commandBuffers` array.

## Discussion

The order in which you sort the command buffers in the array is meaningful, especially when it contains suspending/resuming render passes. A suspending/resuming render pass is a render pass you create by calling [- renderCommandEncoderWithDescriptor:options:](<../mtl4commandbuffer/makerendercommandencoder(descriptor_options_).md>), and provide `MTL4RenderEncoderOptionSuspending` or `MTL4RenderEncoderOptionResuming` for the `options` parameter.

If your command buffers contain suspend/resume render passes, ensure that the first command buffer only suspends, and the last one only resumes. Additionally, make sure that all intermediate command buffers are both suspending and resuming.
