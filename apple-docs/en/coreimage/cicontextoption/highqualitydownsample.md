---
title: highQualityDownsample
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicontextoption/highqualitydownsample
source_url: 'https://developer.apple.com/documentation/coreimage/cicontextoption/highqualitydownsample'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontextoption/highqualitydownsample.json'
content_hash: 'sha256:ae336826e5e67804'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContextOption](../cicontextoption.md)

# highQualityDownsample

<sub>Type Property</sub>

A Boolean value to control the quality of image downsampling operations performed by the Core Image context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let highQualityDownsample: CIContextOption
```

## Discussion

The higher quality behavior performs downsampling operations in multiple passes in order to reduce aliasing artifacts.

The lower quality behavior performs downsampling operations a single pass in order to improve performance.

If the value for this option is:

- True: The higher quality behavior will be used.
- False: The lower quality behavior will be used.
- Not specified: the default behavior is True on macOS and False on other platforms.

> [!note] Note
> - This option does affect how `/CIImage/imageByApplyingTransform:` operations are performed by the context.
> - This option does not affect how `/CIImage/imageByApplyingTransform:highQualityDownsample:` behaves.

## See Also

### Type Properties

- [kCIContextAllowLowPower](allowlowpower.md) — A Boolean value to control the power level of Core Image context renders.
- [kCIContextCacheIntermediates](cacheintermediates.md) — A Boolean value to control how a Core Image context caches the contents of any intermediate image buffers it uses during rendering.
- [kCIContextMemoryLimit](memorytarget.md) — A number value to control the maximum memory in megabytes that the context allocates for render tasks.
- [kCIContextName](name.md) — A Boolean value to specify a client-provided name for a context.
- [kCIContextOutputColorSpace](outputcolorspace.md) — A Core Image context option key to specify the default destination color space for rendering.
- [kCIContextOutputPremultiplied](outputpremultiplied.md) — A Boolean value to control how a Core Image context render produces alpha-premultiplied pixels.
- [kCIContextPriorityRequestLow](priorityrequestlow.md) — A Boolean value to control the priority Core Image context renders.
- [kCIContextUseSoftwareRenderer](usesoftwarerenderer.md) — A Boolean value to control if a Core Image context will use a software renderer.
- [kCIContextWorkingColorSpace](workingcolorspace.md) — A Core Image context option key to specify the working color space for rendering.
- [kCIContextWorkingFormat](workingformat.md) — A Core Image context option key to specify the pixel format to for intermediate results when rendering.
