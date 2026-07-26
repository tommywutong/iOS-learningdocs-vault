---
title: MTLSamplerReductionMode
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsamplerreductionmode
source_url: 'https://developer.apple.com/documentation/metal/mtlsamplerreductionmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsamplerreductionmode.json'
content_hash: 'sha256:115f01c5589c245b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLSamplerReductionMode

<sub>Enumeration</sub>

Configures how the sampler aggregates contributing samples to a final value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLSamplerReductionMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [MTLSamplerReductionModeMaximum](mtlsamplerreductionmode/maximum.md) — A reduction mode that finds the maximum contributing sample value by separately evaluating each channel.
- [MTLSamplerReductionModeMinimum](mtlsamplerreductionmode/minimum.md) — A reduction mode that finds the minimum contributing sample value by separately evaluating each channel.
- [MTLSamplerReductionModeWeightedAverage](mtlsamplerreductionmode/weightedaverage.md) — A reduction mode that adds together the product of each contributing sample value by its weight.

### Initializers

- [init(rawValue:)](<mtlsamplerreductionmode/init(rawvalue_).md>)

## See Also

### Texture samplers

- [Creating and sampling textures](creating-and-sampling-textures.md) — Load image data into a texture and apply it to a quadrangle.
- [MTLSamplerState](mtlsamplerstate.md) — An instance that defines how a texture should be sampled.
- [MTLSamplerDescriptor](mtlsamplerdescriptor.md) — An object that you use to configure a texture sampler.
- [MTLSamplePosition](mtlsampleposition.md) — A subpixel sample position for use in multisample antialiasing (MSAA).
