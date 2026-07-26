---
title: CGBlendMode
framework: Core Graphics
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgblendmode
source_url: 'https://developer.apple.com/documentation/coregraphics/cgblendmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgblendmode.json'
content_hash: 'sha256:de006313a9d73178'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGBlendMode

<sub>Enumeration</sub>

Compositing operations for images.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CGBlendMode
```

## Overview

These blend mode constants represent the Porter-Duff blend modes. The symbols in the equations for these blend modes are:

- R is the premultiplied result
- S is the source color, and includes alpha
- D is the destination color, and includes alpha
- Ra, Sa, and Da are the alpha components of R, S, and D

You can find more information on blend modes, including examples of images produced using them, and many mathematical descriptions of the modes, in _PDF Reference, Fourth Edition_, Version 1.5, Adobe Systems, Inc. If you are a former QuickDraw developer, it may be helpful for you to think of blend modes as an alternative to transfer modes

For examples of using blend modes see “Setting Blend Modes” and “Using Blend Modes With Images” in [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCGBlendModeNormal](cgblendmode/normal.md) — Paints the source image samples over the background image samples.
- [kCGBlendModeMultiply](cgblendmode/multiply.md) — Multiplies the source image samples with the background image samples. This results in colors that are at least as dark as either of the two contributing sample colors.
- [kCGBlendModeScreen](cgblendmode/screen.md) — Multiplies the inverse of the source image samples with the inverse of the background image samples, resulting in colors that are at least as light as either of the two contributing sample colors.
- [kCGBlendModeOverlay](cgblendmode/overlay.md)
- [kCGBlendModeDarken](cgblendmode/darken.md)
- [kCGBlendModeLighten](cgblendmode/lighten.md)
- [kCGBlendModeColorDodge](cgblendmode/colordodge.md) — Brightens the background image samples to reflect the source image samples. Source image sample values that specify black do not produce a change.
- [kCGBlendModeColorBurn](cgblendmode/colorburn.md) — Darkens the background image samples to reflect the source image samples. Source image sample values that specify white do not produce a change.
- [kCGBlendModeSoftLight](cgblendmode/softlight.md)
- [kCGBlendModeHardLight](cgblendmode/hardlight.md)
- [kCGBlendModeDifference](cgblendmode/difference.md)
- [kCGBlendModeExclusion](cgblendmode/exclusion.md) — Produces an effect similar to that produced by [kCGBlendModeDifference](cgblendmode/difference.md), but with lower contrast. Source image sample values that are black don’t produce a change; white inverts the background color values.
- [kCGBlendModeHue](cgblendmode/hue.md) — Uses the luminance and saturation values of the background with the hue of the source image.
- [kCGBlendModeSaturation](cgblendmode/saturation.md) — Uses the luminance and hue values of the background with the saturation of the source image. Areas of the background that have no saturation (that is, pure gray areas) don’t produce a change.
- [kCGBlendModeColor](cgblendmode/color.md) — Uses the luminance values of the background with the hue and saturation values of the source image. This mode preserves the gray levels in the image. You can use this mode to color monochrome images or to tint color images.
- [kCGBlendModeLuminosity](cgblendmode/luminosity.md) — Uses the hue and saturation of the background with the luminance of the source image. This mode creates an effect that is inverse to the effect created by [kCGBlendModeColor](cgblendmode/color.md).
- [kCGBlendModeClear](cgblendmode/clear.md) — `R = 0`
- [kCGBlendModeCopy](cgblendmode/copy.md) — `R = S`
- [kCGBlendModeSourceIn](cgblendmode/sourcein.md) — `R = S*Da`
- [kCGBlendModeSourceOut](cgblendmode/sourceout.md) — `R = S*(1 - Da)`
- [kCGBlendModeSourceAtop](cgblendmode/sourceatop.md) — `R = S*Da + D*(1 - Sa)`
- [kCGBlendModeDestinationOver](cgblendmode/destinationover.md) — `R = S*(1 - Da) + D`
- [kCGBlendModeDestinationIn](cgblendmode/destinationin.md) — `R = D*Sa`
- [kCGBlendModeDestinationOut](cgblendmode/destinationout.md) — `R = D*(1 - Sa)`
- [kCGBlendModeDestinationAtop](cgblendmode/destinationatop.md) — `R = S*(1 - Da) + D*Sa`
- [kCGBlendModeXOR](cgblendmode/xor.md) — `R = S*(1 - Da) + D*(1 - Sa)`. This XOR mode is only nominally related to the classical bitmap XOR operation, which is not supported by Core Graphics
- [kCGBlendModePlusDarker](cgblendmode/plusdarker.md) — `R = MAX(0, 1 - ((1 - D) + (1 - S)))`
- [kCGBlendModePlusLighter](cgblendmode/pluslighter.md) — `R = MIN(1, S + D)`

### Initializers

- [init(rawValue:)](<cgblendmode/init(rawvalue_).md>)

## See Also

### Managing a Graphics Context

- [CGContextFlush](<cgcontext/flush().md>) — Forces all pending drawing operations in a window context to be rendered immediately to the destination device.
- [CGContextSynchronize](<cgcontext/synchronize().md>) — Marks a window context for update.
- [CGContextSetBlendMode](<cgcontext/setblendmode(__).md>) — Sets how sample values are composited by a graphics context.
- [CGContextSetRenderingIntent](<cgcontext/setrenderingintent(__).md>) — Sets the rendering intent in the current graphics state.
