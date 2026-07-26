---
title: 'makeArgumentEncoder(bufferBinding:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makeargumentencoder(bufferbinding:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makeargumentencoder(bufferbinding:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makeargumentencoder%28bufferbinding%3A%29.json'
content_hash: 'sha256:2f9181244984e518'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeArgumentEncoder(bufferBinding:)

<sub>Instance Method</sub>

Creates a new argument encoder for a buffer binding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeArgumentEncoder(bufferBinding: any MTLBufferBinding) -> any MTLArgumentEncoder
```

## Parameters

- `bufferBinding` — An [MTLBufferBinding](../mtlbufferbinding.md) instance.

## See Also

### Creating argument buffer encoders

- [argumentBuffersSupport](argumentbufferssupport.md) — Returns the GPU device’s support tier for argument buffers.
- [maxArgumentBufferSamplerCount](maxargumentbuffersamplercount.md) — The maximum number of unique argument buffer samplers per app.
- [- newArgumentEncoderWithArguments:](<makeargumentencoder(arguments_).md>) — Creates a new argument encoder for an array of arguments.
