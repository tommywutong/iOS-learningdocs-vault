---
title: priorityRequestLow
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicontextoption/priorityrequestlow
source_url: 'https://developer.apple.com/documentation/coreimage/cicontextoption/priorityrequestlow'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontextoption/priorityrequestlow.json'
content_hash: 'sha256:77f2343080729bbb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContextOption](../cicontextoption.md)

# priorityRequestLow

<sub>Type Property</sub>

A Boolean value to control the priority Core Image context renders.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let priorityRequestLow: CIContextOption
```

## Discussion

If this value is True, then rendering with the context from a background thread takes lower priority than other GPU usage from the main thread. This allows your app to perform Core Image rendering without disturbing the frame rate of UI animations.

## See Also

### Type Properties

- [kCIContextAllowLowPower](allowlowpower.md) — A Boolean value to control the power level of Core Image context renders.
- [kCIContextCacheIntermediates](cacheintermediates.md) — A Boolean value to control how a Core Image context caches the contents of any intermediate image buffers it uses during rendering.
- [kCIContextHighQualityDownsample](highqualitydownsample.md) — A Boolean value to control the quality of image downsampling operations performed by the Core Image context.
- [kCIContextMemoryLimit](memorytarget.md) — A number value to control the maximum memory in megabytes that the context allocates for render tasks.
- [kCIContextName](name.md) — A Boolean value to specify a client-provided name for a context.
- [kCIContextOutputColorSpace](outputcolorspace.md) — A Core Image context option key to specify the default destination color space for rendering.
- [kCIContextOutputPremultiplied](outputpremultiplied.md) — A Boolean value to control how a Core Image context render produces alpha-premultiplied pixels.
- [kCIContextUseSoftwareRenderer](usesoftwarerenderer.md) — A Boolean value to control if a Core Image context will use a software renderer.
- [kCIContextWorkingColorSpace](workingcolorspace.md) — A Core Image context option key to specify the working color space for rendering.
- [kCIContextWorkingFormat](workingformat.md) — A Core Image context option key to specify the pixel format to for intermediate results when rendering.
