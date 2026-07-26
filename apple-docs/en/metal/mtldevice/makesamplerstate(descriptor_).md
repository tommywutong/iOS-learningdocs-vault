---
title: 'makeSamplerState(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makesamplerstate(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makesamplerstate(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makesamplerstate%28descriptor%3A%29.json'
content_hash: 'sha256:751c5851b5b6871b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeSamplerState(descriptor:)

<sub>Instance Method</sub>

Creates a sampler state instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeSamplerState(descriptor: MTLSamplerDescriptor) -> (any MTLSamplerState)?
```

## Parameters

- `descriptor` — An [MTLSamplerDescriptor](../mtlsamplerdescriptor.md) instance.

## Return Value

A new [MTLSamplerState](../mtlsamplerstate.md) instance if the method completed successfully; otherwise `nil`.

## See Also

### Creating samplers

- [- supportsTextureSampleCount:](<supportstexturesamplecount(__).md>) — Returns a Boolean value that indicates whether the GPU can sample a texture with a specific number of sample points.
- [getDefaultSamplePositions(sampleCount:)](<getdefaultsamplepositions(samplecount_).md>) — Returns the default sample locations based on the number of samples.
