---
title: name
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicontextoption/name
source_url: 'https://developer.apple.com/documentation/coreimage/cicontextoption/name'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontextoption/name.json'
content_hash: 'sha256:29eba818a555da67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContextOption](../cicontextoption.md)

# name

<sub>Type Property</sub>

A Boolean value to specify a client-provided name for a context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let name: CIContextOption
```

## Discussion

This name will be used in QuickLook graphs and the output of CI_PRINT_TREE.

## See Also

### Type Properties

- [kCIContextAllowLowPower](allowlowpower.md) — A Boolean value to control the power level of Core Image context renders.
- [kCIContextCacheIntermediates](cacheintermediates.md) — A Boolean value to control how a Core Image context caches the contents of any intermediate image buffers it uses during rendering.
- [kCIContextHighQualityDownsample](highqualitydownsample.md) — A Boolean value to control the quality of image downsampling operations performed by the Core Image context.
- [kCIContextMemoryLimit](memorytarget.md) — A number value to control the maximum memory in megabytes that the context allocates for render tasks.
- [kCIContextOutputColorSpace](outputcolorspace.md) — A Core Image context option key to specify the default destination color space for rendering.
- [kCIContextOutputPremultiplied](outputpremultiplied.md) — A Boolean value to control how a Core Image context render produces alpha-premultiplied pixels.
- [kCIContextPriorityRequestLow](priorityrequestlow.md) — A Boolean value to control the priority Core Image context renders.
- [kCIContextUseSoftwareRenderer](usesoftwarerenderer.md) — A Boolean value to control if a Core Image context will use a software renderer.
- [kCIContextWorkingColorSpace](workingcolorspace.md) — A Core Image context option key to specify the working color space for rendering.
- [kCIContextWorkingFormat](workingformat.md) — A Core Image context option key to specify the pixel format to for intermediate results when rendering.
