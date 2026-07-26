---
title: kCIInputPerceptualKey
framework: Core Image
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/kciinputperceptualkey
source_url: 'https://developer.apple.com/documentation/coreimage/kciinputperceptualkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/kciinputperceptualkey.json'
content_hash: 'sha256:e8b8c87446c44ad7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# kCIInputPerceptualKey

<sub>Global Variable</sub>

A key to get or set the boolean behavior of a Core Image filter that specifies if the filter should operate in linear or perceptual colors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let kCIInputPerceptualKey: String
```

## Discussion

The value for this key needs to be an `NSNumber` instance.

## See Also

### Constants

- [kCIDynamicRangeConstrainedHigh](cidynamicrangeoption/constrainedhigh.md) — Use extended dynamic range, but brightness is modulated to optimize for co-existence with other composited content.
- [kCIDynamicRangeHigh](cidynamicrangeoption/high.md) — Use High dynamic range.
- [kCIDynamicRangeStandard](cidynamicrangeoption/standard.md) — Use Standard dynamic range.
- [kCIInputAmountKey](kciinputamountkey.md)
- [kCIInputAngleKey](kciinputanglekey.md) — The angle.
- [kCIInputAspectRatioKey](kciinputaspectratiokey.md) — Aspect Ratio.
- [kCIInputBackgroundImageKey](kciinputbackgroundimagekey.md) — A key for the [CIImage](ciimage.md) object to use as a background image.
- [kCIInputBacksideImageKey](kciinputbacksideimagekey.md) — A key to get or set the backside image for a transition Core Image filter.
- [kCIInputBiasVectorKey](kciinputbiasvectorkey.md) — A key to get or set the vector bias value of a Core Image filter.
- [kCIInputBrightnessKey](kciinputbrightnesskey.md) — Brightness level.
- [kCIInputCenterKey](kciinputcenterkey.md) — A key for a [CIVector](civector.md) object that specifies the center of the area, as _x_  and  _y_- coordinates, to be filtered.
- [kCIInputColorKey](kciinputcolorkey.md) — A key for a [CIColor](cicolor.md) object that specifies a color value.
- [kCIInputColor0Key](kciinputcolor0key.md) — A key to get or set a color value of a Core Image filter.
- [kCIInputColor1Key](kciinputcolor1key.md) — A key to get or set a color value of a Core Image filter.
- [kCIInputColorSpaceKey](kciinputcolorspacekey.md) — A key to get or set a color space value of a Core Image filter.
