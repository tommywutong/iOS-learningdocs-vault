---
title: 'makeBlitCommandEncoder(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcommandbuffer/makeblitcommandencoder(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/makeblitcommandencoder(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/makeblitcommandencoder%28descriptor%3A%29.json'
content_hash: 'sha256:98264408b0e3b883'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# makeBlitCommandEncoder(descriptor:)

<sub>Instance Method</sub>

Creates a block information transfer (blit) encoder from a descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeBlitCommandEncoder(descriptor blitPassDescriptor: MTLBlitPassDescriptor) -> (any MTLBlitCommandEncoder)?
```

## Parameters

- `blitPassDescriptor` — An [MTLBlitPassDescriptor](../mtlblitpassdescriptor.md) instance that configures the [MTLBlitCommandEncoder](../mtlblitcommandencoder.md) the method returns.

## Discussion

Use an [MTLBlitCommandEncoder](../mtlblitcommandencoder.md) instance’s methods to create a block information transfer (blit) pass that quickly copies memory between a GPU device’s resources.

## See Also

### Creating blit encoders

- [- blitCommandEncoder](<makeblitcommandencoder().md>) — Creates a block information transfer (blit) encoder.
