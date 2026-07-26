---
title: yCbCrMatrix_ITU_R_601_4
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdisplaystream/ycbcrmatrix_itu_r_601_4
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdisplaystream/ycbcrmatrix_itu_r_601_4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdisplaystream/ycbcrmatrix_itu_r_601_4.json'
content_hash: 'sha256:59e924fb5269d168'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGDisplayStream](../cgdisplaystream.md)

# yCbCrMatrix_ITU_R_601_4

<sub>Type Property</sub>

Specifies the YCbCr to RGB conversion matrix for standard digital television (ITU R 601) images.

<sub>Mac Catalyst, macOS</sub>

```swift
class let yCbCrMatrix_ITU_R_601_4: CFString
```

## See Also

### Constants

- [kCGColorConversionBlackPointCompensation](../cgcolor/conversionblackpointcompensation.md) — An option for whether to apply black point compensation when converting between color profiles.
- [kCGDisplayBitsPerPixel](../kcgdisplaybitsperpixel.md) — Specifies a CFNumber integer value that represents the number of bits in a pixel.
- [kCGDisplayBitsPerSample](../kcgdisplaybitspersample.md) — Specifies a CFNumber integer value that represents the number of bits in an individual sample (for example, a color value in an RGB pixel).
- [kCGDisplayBlendNormal](../kcgdisplayblendnormal.md) — The blend color is not applied at the start or end of a fade operation.
- [kCGDisplayBlendSolidColor](../kcgdisplayblendsolidcolor.md) — The user sees only the blend color at the start or end of a fade operation.
- [kCGDisplayBytesPerRow](../kcgdisplaybytesperrow.md) — Specifies a CFNumber integer value that represents the number of bytes in a row on the display.
- [kCGDisplayFadeReservationInvalidToken](../kcgdisplayfadereservationinvalidtoken.md)
- [kCGDisplayHeight](../kcgdisplayheight.md) — Specifies a CFNumber integer value that represents the height of the display in pixels.
- [kCGDisplayIOFlags](../kcgdisplayioflags.md) — Specifies a CFNumber integer value that contains the I/O Kit display mode flags. For more information, see the header file `IOKit/IOGraphicsTypes.h`.
- [kCGDisplayMode](../kcgdisplaymode.md) — Specifies a `CFNumber` integer value that represents the I/O Kit display mode number.
- [kCGDisplayModeIsInterlaced](../kcgdisplaymodeisinterlaced.md) — Specifies a CFBoolean value indicating that the I/O Kit interlace mode flag is set.
- [kCGDisplayModeIsSafeForHardware](../kcgdisplaymodeissafeforhardware.md) — Specifies a CFBoolean value indicating that the display mode doesn’t need a confirmation dialog to be set. _(deprecated)_
- [kCGDisplayModeIsStretched](../kcgdisplaymodeisstretched.md) — Specifies a CFBoolean value indicating that the I/O Kit stretched mode flag is set.
- [kCGDisplayModeIsTelevisionOutput](../kcgdisplaymodeistelevisionoutput.md) — Specifies a CFBoolean value indicating that the I/O Kit television output mode flag is set.
- [kCGDisplayModeUsableForDesktopGUI](../kcgdisplaymodeusablefordesktopgui.md) — Specifies a CFBoolean value that indicates whether the display is suitable for use with the macOS graphical user interface. The criteria include factors such as sufficient width and height and adequate pixel depth.
