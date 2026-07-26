---
title: allowLowPower
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicontextoption/allowlowpower
source_url: 'https://developer.apple.com/documentation/coreimage/cicontextoption/allowlowpower'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontextoption/allowlowpower.json'
content_hash: 'sha256:24a75b1e0a3e4160'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContextOption](../cicontextoption.md)

# allowLowPower

<sub>Type Property</sub>

A Boolean value to control the power level of Core Image context renders.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let allowLowPower: CIContextOption
```

## Discussion

This option only affects certain macOS devices with more than one available GPU device.

If this value is True, then rendering with the context will use a use allow power GPU device if available and the high power device is not already in use.

Otherwise, the context will use the highest power/performance GPU device.

## See Also

### Type Properties

- [kCIContextCacheIntermediates](cacheintermediates.md) — A Boolean value to control how a Core Image context caches the contents of any intermediate image buffers it uses during rendering.
- [kCIContextHighQualityDownsample](highqualitydownsample.md) — A Boolean value to control the quality of image downsampling operations performed by the Core Image context.
- [kCIContextMemoryLimit](memorytarget.md) — A number value to control the maximum memory in megabytes that the context allocates for render tasks.
- [kCIContextName](name.md) — A Boolean value to specify a client-provided name for a context.
- [kCIContextOutputColorSpace](outputcolorspace.md) — A Core Image context option key to specify the default destination color space for rendering.
- [kCIContextOutputPremultiplied](outputpremultiplied.md) — A Boolean value to control how a Core Image context render produces alpha-premultiplied pixels.
- [kCIContextPriorityRequestLow](priorityrequestlow.md) — A Boolean value to control the priority Core Image context renders.
- [kCIContextUseSoftwareRenderer](usesoftwarerenderer.md) — A Boolean value to control if a Core Image context will use a software renderer.
- [kCIContextWorkingColorSpace](workingcolorspace.md) — A Core Image context option key to specify the working color space for rendering.
- [kCIContextWorkingFormat](workingformat.md) — A Core Image context option key to specify the pixel format to for intermediate results when rendering.
