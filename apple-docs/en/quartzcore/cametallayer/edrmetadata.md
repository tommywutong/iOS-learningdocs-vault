---
title: edrMetadata
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 10.15+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cametallayer/edrmetadata
source_url: 'https://developer.apple.com/documentation/quartzcore/cametallayer/edrmetadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cametallayer/edrmetadata.json'
content_hash: 'sha256:1ab83323919433a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMetalLayer](../cametallayer.md)

# edrMetadata

<sub>Instance Property</sub>

Metadata describing the tone mapping to apply to the extended dynamic range (EDR) values in the layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var edrMetadata: CAEDRMetadata? { get set }
```

## Discussion

You must set this property before calling [- nextDrawable](<nextdrawable().md>).

The default value is `nil`, which means that the system doesn’t perform any tone mapping of data prior to passing it on to the display. Values above the maximum ([maximumExtendedDynamicRangeColorComponentValue](../../appkit/nsscreen/maximumextendeddynamicrangecolorcomponentvalue.md)) may be clipped.

If non-`nil`, the system uses the metadata provided to tone map values to the display, based on the display’s current characteristics. You must also set [pixelFormat](pixelformat.md) to a pixel format that supports pixel values greater than `1.0` (such as [MTLPixelFormat.rgba16Float](../../metal/mtlpixelformat/rgba16float.md)) and [colorspace](../caopengllayer/colorspace.md) to a color space that supports a linear transfer function.

The tone mapping process requires significant amounts of memory and GPU processing.

## See Also

### Configuring Extended Dynamic Range Behavior

- [wantsExtendedDynamicRangeContent](wantsextendeddynamicrangecontent.md) — Enables extended dynamic range values onscreen.
