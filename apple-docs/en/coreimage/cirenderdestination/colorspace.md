---
title: colorSpace
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cirenderdestination/colorspace
source_url: 'https://developer.apple.com/documentation/coreimage/cirenderdestination/colorspace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirenderdestination/colorspace.json'
content_hash: 'sha256:69163ee5e165a0d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIRenderDestination](../cirenderdestination.md)

# colorSpace

<sub>Instance Property</sub>

The destination’s color space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var colorSpace: CGColorSpace? { get set }
```

## See Also

### Customizing Rendering

- [alphaMode](alphamode.md) — The render destination’s representation of alpha (transparency) values.
- [CIRenderDestinationAlphaMode](../cirenderdestinationalphamode.md) — Different ways of representing alpha.
- [blendKernel](blendkernel.md) — The destination’s blend kernel.
- [blendsInDestinationColorSpace](blendsindestinationcolorspace.md) — Indicator of whether to blend in the destination’s color space.
- [width](width.md) — The render destination’s row width.
- [height](height.md) — The render destination’s buffer height.
- [clamped](isclamped.md) — Indicator of whether or not the destination clamps.
- [dithered](isdithered.md) — Indicator of whether or not the destination dithers.
- [flipped](isflipped.md) — Indicator of whether the destination is flipped.
