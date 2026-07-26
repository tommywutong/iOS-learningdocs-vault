---
title: extendedGray
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolorspace/extendedgray
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorspace/extendedgray'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorspace/extendedgray.json'
content_hash: 'sha256:bc50ae4bb66c1b32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGColorSpace](../cgcolorspace.md)

# extendedGray

<sub>Type Property</sub>

The extended gray color space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let extendedGray: CFString
```

## Discussion

This color space has the same colorimetry as [kCGColorSpaceGenericGrayGamma2_2](genericgraygamma2_2.md); in addition, you may encode component values below `0.0` and above `1.0`. Negative values are encoded as the signed reflection of the original encoding function, as shown below

```swift
extendedGrayTransferFunction(x) = sign(x) ✖️ gamma22Function(abs(x))
```

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
- [kCGColorSpaceLinearGray](lineargray.md) — The gray color space using a linear transfer function.
- [kCGColorSpaceExtendedLinearGray](extendedlineargray.md) — The extended gray color space with a linear transfer function.
- [kCGColorSpaceGenericCMYK](genericcmyk.md) — The generic CMYK color space.
- [kCGColorSpaceGenericRGBLinear](genericrgblinear.md) — The generic RGB color space with a linear transfer function.
- [kCGColorSpaceGenericXYZ](genericxyz.md) — The XYZ color space, as defined by the CIE 1931 standard.
- [kCGColorSpaceGenericLab](genericlab.md) — The generic LAB color space.
