---
title: 'makeRenderCommandEncoder(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcommandbuffer/makerendercommandencoder(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/makerendercommandencoder(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/makerendercommandencoder%28descriptor%3A%29.json'
content_hash: 'sha256:5035281565b88825'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# makeRenderCommandEncoder(descriptor:)

<sub>Instance Method</sub>

Creates a render command encoder from a descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeRenderCommandEncoder(descriptor renderPassDescriptor: MTLRenderPassDescriptor) -> (any MTLRenderCommandEncoder)?
```

## Parameters

- `renderPassDescriptor` — An [MTLRenderPassDescriptor](../mtlrenderpassdescriptor.md) instance that configures the [MTLRenderCommandEncoder](../mtlrendercommandencoder.md) the method returns.

## Discussion

Use an [MTLRenderCommandEncoder](../mtlrendercommandencoder.md) instance’s methods to set up a single graphics-rendering pass.
