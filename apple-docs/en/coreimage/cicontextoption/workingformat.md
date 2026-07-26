---
title: workingFormat
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicontextoption/workingformat
source_url: 'https://developer.apple.com/documentation/coreimage/cicontextoption/workingformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontextoption/workingformat.json'
content_hash: 'sha256:1d397ab4c81a07d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContextOption](../cicontextoption.md)

# workingFormat

<sub>Type Property</sub>

A Core Image context option key to specify the pixel format to for intermediate results when rendering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let workingFormat: CIContextOption
```

## Discussion

The value for this key is an `NSNumber` instance containing a [CIFormat](../ciformat.md) value.

The supported values for the working pixel format are:

| [CIFormat](../ciformat.md) | Notes |
|---|---|
| [kCIFormatRGBA8](../ciformat/rgba8.md) | Uses 4 bytes per pixel. Only supporrts SDR and has less precision. |
| [kCIFormatRGBAh](../ciformat/rgbah.md) | Uses 8 bytes per pixel. Supports HDR. |
| [kCIFormatRGBAf](../ciformat/rgbaf.md) | Uses 16 bytes per pixel. Only available on macOS |

If this option is not specified, then the default is [kCIFormatRGBAh](../ciformat/rgbah.md).

(The default is [kCIFormatRGBA8](../ciformat/rgba8.md) if your if app is linked against iOS 12 SDK or earlier.)

## See Also

### Type Properties

- [kCIContextAllowLowPower](allowlowpower.md) — A Boolean value to control the power level of Core Image context renders.
- [kCIContextCacheIntermediates](cacheintermediates.md) — A Boolean value to control how a Core Image context caches the contents of any intermediate image buffers it uses during rendering.
- [kCIContextHighQualityDownsample](highqualitydownsample.md) — A Boolean value to control the quality of image downsampling operations performed by the Core Image context.
- [kCIContextMemoryLimit](memorytarget.md) — A number value to control the maximum memory in megabytes that the context allocates for render tasks.
- [kCIContextName](name.md) — A Boolean value to specify a client-provided name for a context.
- [kCIContextOutputColorSpace](outputcolorspace.md) — A Core Image context option key to specify the default destination color space for rendering.
- [kCIContextOutputPremultiplied](outputpremultiplied.md) — A Boolean value to control how a Core Image context render produces alpha-premultiplied pixels.
- [kCIContextPriorityRequestLow](priorityrequestlow.md) — A Boolean value to control the priority Core Image context renders.
- [kCIContextUseSoftwareRenderer](usesoftwarerenderer.md) — A Boolean value to control if a Core Image context will use a software renderer.
- [kCIContextWorkingColorSpace](workingcolorspace.md) — A Core Image context option key to specify the working color space for rendering.
