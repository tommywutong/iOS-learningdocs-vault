---
title: linearSRGB
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolorspace/linearsrgb
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorspace/linearsrgb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorspace/linearsrgb.json'
content_hash: 'sha256:cb92273241140809'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGColorSpace](../cgcolorspace.md)

# linearSRGB

<sub>Type Property</sub>

The sRGB color space with a linear transfer function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let linearSRGB: CFString
```

## Discussion

This color space has the same colorimetry as [kCGColorSpaceSRGB](srgb.md), but uses a linear transfer function.

## See Also

### Accessing System-Defined Color Spaces

- [kCGColorSpaceDisplayP3](displayp3.md) — The Display P3 color space, created by Apple.
- [kCGColorSpaceDisplayP3_HLG](displayp3_hlg.md) — The Display P3 color space, using the HLG transfer function.
- [kCGColorSpaceDisplayP3_PQ_EOTF](displayp3_pq_eotf.md) — The Display P3 color space, using the PQ transfer function. _(deprecated)_
- [kCGColorSpaceExtendedLinearDisplayP3](extendedlineardisplayp3.md) — The Display P3 color space with a linear transfer function and extended-range values.
- [kCGColorSpaceSRGB](srgb.md) — The standard Red Green Blue (sRGB) color space.
- [kCGColorSpaceExtendedSRGB](extendedsrgb.md) — The extended sRGB color space.
- [kCGColorSpaceExtendedLinearSRGB](extendedlinearsrgb.md) — The sRGB color space with a linear transfer function and extended-range values.
- [kCGColorSpaceGenericGrayGamma2_2](genericgraygamma2_2.md) — The generic gray color space that has an exponential transfer function with a power of 2.2.
- [kCGColorSpaceExtendedGray](extendedgray.md) — The extended gray color space.
- [kCGColorSpaceLinearGray](lineargray.md) — The gray color space using a linear transfer function.
- [kCGColorSpaceExtendedLinearGray](extendedlineargray.md) — The extended gray color space with a linear transfer function.
- [kCGColorSpaceGenericCMYK](genericcmyk.md) — The generic CMYK color space.
- [kCGColorSpaceGenericRGBLinear](genericrgblinear.md) — The generic RGB color space with a linear transfer function.
- [kCGColorSpaceGenericXYZ](genericxyz.md) — The XYZ color space, as defined by the CIE 1931 standard.
- [kCGColorSpaceGenericLab](genericlab.md) — The generic LAB color space.
