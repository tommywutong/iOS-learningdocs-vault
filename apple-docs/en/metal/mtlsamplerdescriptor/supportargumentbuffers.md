---
title: supportArgumentBuffers
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsamplerdescriptor/supportargumentbuffers
source_url: 'https://developer.apple.com/documentation/metal/mtlsamplerdescriptor/supportargumentbuffers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsamplerdescriptor/supportargumentbuffers.json'
content_hash: 'sha256:3858a108642122cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLSamplerDescriptor](../mtlsamplerdescriptor.md)

# supportArgumentBuffers

<sub>Instance Property</sub>

A Boolean value that indicates whether you can reference a sampler, that you make with this descriptor, by its resource ID from an argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var supportArgumentBuffers: Bool { get set }
```

## Discussion

The default value is  [false](../../swift/false.md), which means that you can only encode the samplers you make with this descriptor as individual resources in the sampler state argument table.

Your app can encode samplers into an argument buffer if you create them with an [MTLSamplerDescriptor](../mtlsamplerdescriptor.md) instance that has this property equal to [true](../../swift/true.md).

> [!tip] Tip
> Check [maxArgumentBufferSamplerCount](../mtldevice/maxargumentbuffersamplercount.md) at runtime to query the number of samplers your app can encode into an argument buffer.

Each unique configuration of an [MTLSamplerDescriptor](../mtlsamplerdescriptor.md) instance’s properties creates a unique [MTLSamplerState](../mtlsamplerstate.md) instance. For example, you can create unique samplers with the same [MTLSamplerDescriptor](../mtlsamplerdescriptor.md) instance by changing one or more values of its properties, such as [minFilter](minfilter.md) or [magFilter](magfilter.md) before creating another instance.

Conversely, creating secondary sampler instances with the same descriptor property values doesn’t create any additional, unique samplers. Instead, they refer to the same underlying sampler, even if you create it with a difference descriptor instance because the configuration is the same.
