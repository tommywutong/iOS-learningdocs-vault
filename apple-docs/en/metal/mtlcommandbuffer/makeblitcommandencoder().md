---
title: makeBlitCommandEncoder()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbuffer/makeblitcommandencoder()
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/makeblitcommandencoder()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/makeblitcommandencoder%28%29.json'
content_hash: 'sha256:aed01f53e3ad638c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# makeBlitCommandEncoder()

<sub>Instance Method</sub>

Creates a block information transfer (blit) encoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeBlitCommandEncoder() -> (any MTLBlitCommandEncoder)?
```

## Discussion

Use an [MTLBlitCommandEncoder](../mtlblitcommandencoder.md) instance’s methods to create a block information transfer (blit) pass that quickly copies memory between a GPU device’s resources.

## See Also

### Creating blit encoders

- [- blitCommandEncoderWithDescriptor:](<makeblitcommandencoder(descriptor_).md>) — Creates a block information transfer (blit) encoder from a descriptor.
