---
title: CGBlendMode.screen
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgblendmode/screen
source_url: 'https://developer.apple.com/documentation/coregraphics/cgblendmode/screen'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgblendmode/screen.json'
content_hash: 'sha256:de47645b568f76dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGBlendMode](../cgblendmode.md)

# CGBlendMode.screen

<sub>Case</sub>

Multiplies the inverse of the source image samples with the inverse of the background image samples, resulting in colors that are at least as light as either of the two contributing sample colors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case screen
```

## See Also

### Constants

- [kCGBlendModeNormal](normal.md) — Paints the source image samples over the background image samples.
- [kCGBlendModeMultiply](multiply.md) — Multiplies the source image samples with the background image samples. This results in colors that are at least as dark as either of the two contributing sample colors.
- [kCGBlendModeOverlay](overlay.md)
- [kCGBlendModeDarken](darken.md)
- [kCGBlendModeLighten](lighten.md)
- [kCGBlendModeColorDodge](colordodge.md) — Brightens the background image samples to reflect the source image samples. Source image sample values that specify black do not produce a change.
- [kCGBlendModeColorBurn](colorburn.md) — Darkens the background image samples to reflect the source image samples. Source image sample values that specify white do not produce a change.
- [kCGBlendModeSoftLight](softlight.md)
- [kCGBlendModeHardLight](hardlight.md)
- [kCGBlendModeDifference](difference.md)
- [kCGBlendModeExclusion](exclusion.md) — Produces an effect similar to that produced by [kCGBlendModeDifference](difference.md), but with lower contrast. Source image sample values that are black don’t produce a change; white inverts the background color values.
- [kCGBlendModeHue](hue.md) — Uses the luminance and saturation values of the background with the hue of the source image.
- [kCGBlendModeSaturation](saturation.md) — Uses the luminance and hue values of the background with the saturation of the source image. Areas of the background that have no saturation (that is, pure gray areas) don’t produce a change.
- [kCGBlendModeColor](color.md) — Uses the luminance values of the background with the hue and saturation values of the source image. This mode preserves the gray levels in the image. You can use this mode to color monochrome images or to tint color images.
- [kCGBlendModeLuminosity](luminosity.md) — Uses the hue and saturation of the background with the luminance of the source image. This mode creates an effect that is inverse to the effect created by [kCGBlendModeColor](color.md).
