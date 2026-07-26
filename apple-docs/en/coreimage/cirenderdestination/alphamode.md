---
title: alphaMode
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cirenderdestination/alphamode
source_url: 'https://developer.apple.com/documentation/coreimage/cirenderdestination/alphamode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirenderdestination/alphamode.json'
content_hash: 'sha256:cfad7128afceab03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIRenderDestination](../cirenderdestination.md)

# alphaMode

<sub>Instance Property</sub>

The render destination’s representation of alpha (transparency) values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var alphaMode: CIRenderDestinationAlphaMode { get set }
```

## Discussion

This property defaults to an appropriate value given the object with which you initialized the [CIRenderDestination](../cirenderdestination.md).

## See Also

### Customizing Rendering

- [CIRenderDestinationAlphaMode](../cirenderdestinationalphamode.md) — Different ways of representing alpha.
- [blendKernel](blendkernel.md) — The destination’s blend kernel.
- [blendsInDestinationColorSpace](blendsindestinationcolorspace.md) — Indicator of whether to blend in the destination’s color space.
- [colorSpace](colorspace.md) — The destination’s color space.
- [width](width.md) — The render destination’s row width.
- [height](height.md) — The render destination’s buffer height.
- [clamped](isclamped.md) — Indicator of whether or not the destination clamps.
- [dithered](isdithered.md) — Indicator of whether or not the destination dithers.
- [flipped](isflipped.md) — Indicator of whether the destination is flipped.
