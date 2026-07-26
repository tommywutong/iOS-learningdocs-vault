---
title: MTLSamplePosition
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsampleposition
source_url: 'https://developer.apple.com/documentation/metal/mtlsampleposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsampleposition.json'
content_hash: 'sha256:eaede4cf7cf20df9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLSamplePosition

<sub>Structure</sub>

A subpixel sample position for use in multisample antialiasing (MSAA).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLSamplePosition
```

## Overview

Subpixel sample positions are in a 16 x 16 grid across a pixel. Each subsample position’s [x](mtlsampleposition/x.md) and [y](mtlsampleposition/y.md) values are in 1/16 increments in the floating-point range `[0.0, 15.0/16.0)`. The pixel’s origin point `(0,0)` is at the top-left corner.

See [Positioning samples programmatically](positioning-samples-programmatically.md) for the details on working with subpixels.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<mtlsampleposition/init().md>) — Returns a new sample position on a subpixel grid.
- [init(x:y:)](<mtlsampleposition/init(x_y_).md>) — Returns a new sample position on a subpixel grid at specified coordinates.

### Instance Properties

- [x](mtlsampleposition/x.md) — The x position of the sample on the subpixel grid.
- [y](mtlsampleposition/y.md) — The y position of the sample on the subpixel grid.

## See Also

### Texture samplers

- [Creating and sampling textures](creating-and-sampling-textures.md) — Load image data into a texture and apply it to a quadrangle.
- [MTLSamplerState](mtlsamplerstate.md) — An instance that defines how a texture should be sampled.
- [MTLSamplerDescriptor](mtlsamplerdescriptor.md) — An object that you use to configure a texture sampler.
- [MTLSamplerReductionMode](mtlsamplerreductionmode.md) — Configures how the sampler aggregates contributing samples to a final value.
