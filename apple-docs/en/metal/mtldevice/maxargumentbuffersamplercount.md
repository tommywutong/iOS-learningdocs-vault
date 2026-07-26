---
title: maxArgumentBufferSamplerCount
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldevice/maxargumentbuffersamplercount
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/maxargumentbuffersamplercount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/maxargumentbuffersamplercount.json'
content_hash: 'sha256:b526d5bf19afe2e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# maxArgumentBufferSamplerCount

<sub>Instance Property</sub>

The maximum number of unique argument buffer samplers per app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var maxArgumentBufferSamplerCount: Int { get }
```

## Discussion

This limit only applies to samplers that support argument buffers (see [supportArgumentBuffers](../mtlsamplerdescriptor/supportargumentbuffers.md)). An [MTLSamplerState](../mtlsamplerstate.md) instance is only unique if the properties of the [MTLSamplerDescriptor](../mtlsamplerdescriptor.md) instance that created it are unique. For example, two samplers with equal [minFilter](../mtlsamplerdescriptor/minfilter.md) values but different [magFilter](../mtlsamplerdescriptor/magfilter.md) values are unique.

See [Improving CPU performance by using argument buffers](../improving-cpu-performance-by-using-argument-buffers.md) for more information about argument buffer tiers, limits, and capabilities.

## See Also

### Creating argument buffer encoders

- [argumentBuffersSupport](argumentbufferssupport.md) — Returns the GPU device’s support tier for argument buffers.
- [- newArgumentEncoderWithArguments:](<makeargumentencoder(arguments_).md>) — Creates a new argument encoder for an array of arguments.
- [- newArgumentEncoderWithBufferBinding:](<makeargumentencoder(bufferbinding_).md>) — Creates a new argument encoder for a buffer binding.
