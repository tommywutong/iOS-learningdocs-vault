---
title: CGBlendMode.softLight
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgblendmode/softlight
source_url: 'https://developer.apple.com/documentation/coregraphics/cgblendmode/softlight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgblendmode/softlight.json'
content_hash: 'sha256:a7ed39c039355083'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGBlendMode](../cgblendmode.md)

# CGBlendMode.softLight

<sub>Case</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case softLight
```

## Discussion

Either darkens or lightens colors, depending on the source image sample color. If the source image sample color is lighter than 50% gray, the background is lightened, similar to dodging. If the source image sample color is darker than 50% gray, the background is darkened, similar to burning. If the source image sample color is equal to 50% gray, the background is not changed. Image samples that are equal to pure black or pure white produce darker or lighter areas, but do not result in pure black or white. The overall effect is similar to what you’d achieve by shining a diffuse spotlight on the source image. Use this to add highlights to a scene.

## See Also

### Constants

- [kCGBlendModeNormal](normal.md) — Paints the source image samples over the background image samples.
- [kCGBlendModeMultiply](multiply.md) — Multiplies the source image samples with the background image samples. This results in colors that are at least as dark as either of the two contributing sample colors.
- [kCGBlendModeScreen](screen.md) — Multiplies the inverse of the source image samples with the inverse of the background image samples, resulting in colors that are at least as light as either of the two contributing sample colors.
- [kCGBlendModeOverlay](overlay.md)
- [kCGBlendModeDarken](darken.md)
- [kCGBlendModeLighten](lighten.md)
- [kCGBlendModeColorDodge](colordodge.md) — Brightens the background image samples to reflect the source image samples. Source image sample values that specify black do not produce a change.
- [kCGBlendModeColorBurn](colorburn.md) — Darkens the background image samples to reflect the source image samples. Source image sample values that specify white do not produce a change.
- [kCGBlendModeHardLight](hardlight.md)
- [kCGBlendModeDifference](difference.md)
- [kCGBlendModeExclusion](exclusion.md) — Produces an effect similar to that produced by [kCGBlendModeDifference](difference.md), but with lower contrast. Source image sample values that are black don’t produce a change; white inverts the background color values.
- [kCGBlendModeHue](hue.md) — Uses the luminance and saturation values of the background with the hue of the source image.
- [kCGBlendModeSaturation](saturation.md) — Uses the luminance and hue values of the background with the saturation of the source image. Areas of the background that have no saturation (that is, pure gray areas) don’t produce a change.
- [kCGBlendModeColor](color.md) — Uses the luminance values of the background with the hue and saturation values of the source image. This mode preserves the gray levels in the image. You can use this mode to color monochrome images or to tint color images.
- [kCGBlendModeLuminosity](luminosity.md) — Uses the hue and saturation of the background with the luminance of the source image. This mode creates an effect that is inverse to the effect created by [kCGBlendModeColor](color.md).
