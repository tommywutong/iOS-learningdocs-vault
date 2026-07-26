---
title: MTLSamplerState
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsamplerstate
source_url: 'https://developer.apple.com/documentation/metal/mtlsamplerstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsamplerstate.json'
content_hash: 'sha256:203622f6c32d3b09'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLSamplerState

<sub>Protocol</sub>

An instance that defines how a texture should be sampled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLSamplerState : NSObjectProtocol, Sendable
```

## Overview

The [MTLSamplerState](mtlsamplerstate.md) protocol defines the interface for a lightweight instance used to encode how a shader or compute kernel should sample a texture. To create a sampler state instance:

1. Create an [MTLSamplerDescriptor](mtlsamplerdescriptor.md) instance.
2. Set the desired properties of the sampler descriptor, including filtering options, addressing modes, maximum anisotropy, and level-of-detail parameters.
3. Call the [- newSamplerStateWithDescriptor:](<mtldevice/makesamplerstate(descriptor_).md>) method of the [MTLDevice](mtldevice.md) instance.

(Your app does not define a class that implements the [MTLSamplerState](mtlsamplerstate.md) protocol.)

You can either release the [MTLSamplerDescriptor](mtlsamplerdescriptor.md) instance or modify its property values and reuse it to create more [MTLSamplerState](mtlsamplerstate.md) instances. The descriptor’s properties are only used during instance creation; once created the behavior of a sampler state instance is fixed and cannot be changed.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Identifying the sampler

- [device](mtlsamplerstate/device.md) — The device object that created the sampler.
- [label](mtlsamplerstate/label.md) — A string that identifies the sampler.

### Instance Properties

- [gpuResourceID](mtlsamplerstate/gpuresourceid.md)

## See Also

### Texture samplers

- [Creating and sampling textures](creating-and-sampling-textures.md) — Load image data into a texture and apply it to a quadrangle.
- [MTLSamplerDescriptor](mtlsamplerdescriptor.md) — An object that you use to configure a texture sampler.
- [MTLSamplePosition](mtlsampleposition.md) — A subpixel sample position for use in multisample antialiasing (MSAA).
- [MTLSamplerReductionMode](mtlsamplerreductionmode.md) — Configures how the sampler aggregates contributing samples to a final value.
