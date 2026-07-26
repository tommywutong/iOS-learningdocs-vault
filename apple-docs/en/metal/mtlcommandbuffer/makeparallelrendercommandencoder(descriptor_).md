---
title: 'makeParallelRenderCommandEncoder(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcommandbuffer/makeparallelrendercommandencoder(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/makeparallelrendercommandencoder(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/makeparallelrendercommandencoder%28descriptor%3A%29.json'
content_hash: 'sha256:84ec620c816822f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# makeParallelRenderCommandEncoder(descriptor:)

<sub>Instance Method</sub>

Creates a parallel render command encoder from a descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeParallelRenderCommandEncoder(descriptor renderPassDescriptor: MTLRenderPassDescriptor) -> (any MTLParallelRenderCommandEncoder)?
```

## Parameters

- `renderPassDescriptor` — An [MTLRenderPassDescriptor](../mtlrenderpassdescriptor.md) instance that configures the [MTLParallelRenderCommandEncoder](../mtlparallelrendercommandencoder.md) the method returns.

## Discussion

An [MTLParallelRenderCommandEncoder](../mtlparallelrendercommandencoder.md) instance can create multiple, independent render command encoders that contribute to the same render pass on different threads.
