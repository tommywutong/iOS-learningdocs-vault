---
title: MetalFX
framework: MetalFX
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/metalfx
source_url: 'https://developer.apple.com/documentation/metalfx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metalfx.json'
content_hash: 'sha256:bc3cf3efc64f74b0'
translated: false
---

> Navigation: [Technologies](technologies.md)

# MetalFX

<sub>Framework</sub>

Boost your Metal app’s performance by upscaling lower-resolution content to save GPU time.

## Overview

The `MetalFX` framework integrates with [Metal](metal.md) to upscale a relatively low-resolution image to a higher output resolution in less time than it takes to render directly to the output resolution.

![](../../attachments/d0d41d9865689f453bc27b90af756121/media-4085441@2x.png)

<sub>A timeline diagram that compares a traditional rendering timespan and compares it to a MetalFX upscaling timespan. The MetalFX upscaling method, which renders at a lower resolution and then upscales to the final resolution with MetalFX, takes about half the time traditional rendering, which renders directly to the higher, final resolution.</sub>

Use the GPU time savings to further enhance your app or game’s experience. For example, add more effects or scene details.

`MetalFX` gives you two different ways to upscale your input renderings:

- Temporal antialiased upscaling
- Spatial upscaling

If you can provide pixel color, depth, and motion information, add an [MTLFXTemporalScaler](metalfx/mtlfxtemporalscaler.md) instance to your render pipeline. Otherwise, add an [MTLFXSpatialScaler](metalfx/mtlfxspatialscaler.md) instance, which only requires a pixel color input texture.

Because the scaling effects take time to initialize, make an instance of either effect at launch or when a display changes resolutions. Once you’ve created an effect instance, you can use it repeatedly, typically once per frame.

## Topics

### Temporal scaling

- [Applying temporal antialiasing and upscaling using MetalFX](metalfx/applying-temporal-antialiasing-and-upscaling-using-metalfx.md) — Reduce render workloads while increasing image detail with MetalFX.
- [MTLFXTemporalScaler](metalfx/mtlfxtemporalscaler.md) — An upscaling effect that generates a higher resolution texture in a render pass by analyzing multiple input textures over time.
- [MTLFXTemporalScalerDescriptor](metalfx/mtlfxtemporalscalerdescriptor.md) — A set of properties that configure a temporal scaling effect, and a factory method that creates the effect.

### Spatial scaling

- [MTLFXSpatialScaler](metalfx/mtlfxspatialscaler.md) — An upscaling effect that generates a higher resolution texture in a render pass by spatially analyzing an input texture.
- [MTLFXSpatialScalerDescriptor](metalfx/mtlfxspatialscalerdescriptor.md) — A set of properties that configure a spatial scaling effect, and a factory method that creates the effect.
- [MTLFXSpatialScalerColorProcessingMode](metalfx/mtlfxspatialscalercolorprocessingmode.md) — The color space modes for the input and output textures you use with a spatial scaling effect instance.

### Classes

- [MTLFXFrameInterpolatorDescriptor](metalfx/mtlfxframeinterpolatordescriptor.md) — A set of properties that configure a frame interpolator, and a factory method that creates the effect.
- [MTLFXTemporalDenoisedScalerDescriptor](metalfx/mtlfxtemporaldenoisedscalerdescriptor.md)

### Protocols

- [MTL4FXFrameInterpolator](metalfx/mtl4fxframeinterpolator.md)
- [MTL4FXSpatialScaler](metalfx/mtl4fxspatialscaler.md) — An upscaling effect that generates a higher resolution texture in a render pass by spatially analyzing an input texture.
- [MTL4FXTemporalDenoisedScaler](metalfx/mtl4fxtemporaldenoisedscaler.md)
- [MTL4FXTemporalScaler](metalfx/mtl4fxtemporalscaler.md)
- [MTLFXFrameInterpolatableScaler](metalfx/mtlfxframeinterpolatablescaler.md)
- [MTLFXFrameInterpolator](metalfx/mtlfxframeinterpolator.md)
- [MTLFXFrameInterpolatorBase](metalfx/mtlfxframeinterpolatorbase.md)
- [MTLFXSpatialScalerBase](metalfx/mtlfxspatialscalerbase.md) — An upscaling effect that generates a higher resolution texture in a render pass by spatially analyzing an input texture.
- [MTLFXTemporalDenoisedScaler](metalfx/mtlfxtemporaldenoisedscaler.md)
- [MTLFXTemporalDenoisedScalerBase](metalfx/mtlfxtemporaldenoisedscalerbase.md)
- [MTLFXTemporalScalerBase](metalfx/mtlfxtemporalscalerbase.md) — An upscaling effect that generates a higher resolution texture in a render pass by analyzing multiple input textures over time.
