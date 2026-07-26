---
title: argumentBuffersSupport
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldevice/argumentbufferssupport
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/argumentbufferssupport'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/argumentbufferssupport.json'
content_hash: 'sha256:98c4e983f74819be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# argumentBuffersSupport

<sub>Instance Property</sub>

Returns the GPU device’s support tier for argument buffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var argumentBuffersSupport: MTLArgumentBuffersTier { get }
```

## Topics

### Argument buffer tiers

- [MTLArgumentBuffersTier](../mtlargumentbufferstier.md) — The values that determine the limits and capabilities of argument buffers.

## See Also

### Creating argument buffer encoders

- [maxArgumentBufferSamplerCount](maxargumentbuffersamplercount.md) — The maximum number of unique argument buffer samplers per app.
- [- newArgumentEncoderWithArguments:](<makeargumentencoder(arguments_).md>) — Creates a new argument encoder for an array of arguments.
- [- newArgumentEncoderWithBufferBinding:](<makeargumentencoder(bufferbinding_).md>) — Creates a new argument encoder for a buffer binding.
