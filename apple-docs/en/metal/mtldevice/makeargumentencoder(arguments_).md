---
title: 'makeArgumentEncoder(arguments:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makeargumentencoder(arguments:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makeargumentencoder(arguments:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makeargumentencoder%28arguments%3A%29.json'
content_hash: 'sha256:207225ec15bbb343'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeArgumentEncoder(arguments:)

<sub>Instance Method</sub>

Creates a new argument encoder for an array of arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeArgumentEncoder(arguments: [MTLArgumentDescriptor]) -> (any MTLArgumentEncoder)?
```

## Parameters

- `arguments` — An array of [MTLArgumentDescriptor](../mtlargumentdescriptor.md) instances that you need to sort by their [index](../mtlargumentdescriptor/index.md) properties in monotonically increasing order.

## See Also

### Creating argument buffer encoders

- [argumentBuffersSupport](argumentbufferssupport.md) — Returns the GPU device’s support tier for argument buffers.
- [maxArgumentBufferSamplerCount](maxargumentbuffersamplercount.md) — The maximum number of unique argument buffer samplers per app.
- [- newArgumentEncoderWithBufferBinding:](<makeargumentencoder(bufferbinding_).md>) — Creates a new argument encoder for a buffer binding.
