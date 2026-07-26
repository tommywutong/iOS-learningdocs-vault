---
title: itur_2020_PQ_EOTF
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 12.6+（13.4 起废弃）, iPadOS 12.6+（13.4 起废弃）, Mac Catalyst 13.1+（13.4 起废弃）, macOS 10.14.6+（10.15.4 起废弃）, tvOS 12.0+（13.4 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 5.0+（6.2 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/coregraphics/cgcolorspace/itur_2020_pq_eotf
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorspace/itur_2020_pq_eotf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorspace/itur_2020_pq_eotf.json'
content_hash: 'sha256:b60cb0e2faba6927'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGColorSpace](../cgcolorspace.md)

# itur_2020_PQ_EOTF

<sub>Type Property</sub>

The recommendation of the International Telecommunication Union (ITU) Radiocommunication sector for the BT.2020 color space, with the PQ transfer function.

> [!warning] Deprecated
> No longer supported

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let itur_2020_PQ_EOTF: CFString
```

## Discussion

This color space has the same colorimetry as [kCGColorSpaceITUR_2020](itur_2020.md), but uses the Perceptual Quantizer (PQ) transfer function. A pixel value of `1.0` is assumed to be `100` nits. See the current active version of the BT.2100 recommendation on the ITU website ([https://www.itu.int/](https://www.itu.int/)).

## See Also

### Accessing System-Defined Color Spaces

- [kCGColorSpaceDisplayP3](displayp3.md) — The Display P3 color space, created by Apple.
- [kCGColorSpaceDisplayP3_HLG](displayp3_hlg.md) — The Display P3 color space, using the HLG transfer function.
- [kCGColorSpaceDisplayP3_PQ_EOTF](displayp3_pq_eotf.md) — The Display P3 color space, using the PQ transfer function. _(deprecated)_
- [kCGColorSpaceExtendedLinearDisplayP3](extendedlineardisplayp3.md) — The Display P3 color space with a linear transfer function and extended-range values.
- [kCGColorSpaceSRGB](srgb.md) — The standard Red Green Blue (sRGB) color space.
- [kCGColorSpaceLinearSRGB](linearsrgb.md) — The sRGB color space with a linear transfer function.
- [kCGColorSpaceExtendedSRGB](extendedsrgb.md) — The extended sRGB color space.
- [kCGColorSpaceExtendedLinearSRGB](extendedlinearsrgb.md) — The sRGB color space with a linear transfer function and extended-range values.
- [kCGColorSpaceGenericGrayGamma2_2](genericgraygamma2_2.md) — The generic gray color space that has an exponential transfer function with a power of 2.2.
- [kCGColorSpaceExtendedGray](extendedgray.md) — The extended gray color space.
- [kCGColorSpaceLinearGray](lineargray.md) — The gray color space using a linear transfer function.
- [kCGColorSpaceExtendedLinearGray](extendedlineargray.md) — The extended gray color space with a linear transfer function.
- [kCGColorSpaceGenericCMYK](genericcmyk.md) — The generic CMYK color space.
- [kCGColorSpaceGenericRGBLinear](genericrgblinear.md) — The generic RGB color space with a linear transfer function.
- [kCGColorSpaceGenericXYZ](genericxyz.md) — The XYZ color space, as defined by the CIE 1931 standard.
