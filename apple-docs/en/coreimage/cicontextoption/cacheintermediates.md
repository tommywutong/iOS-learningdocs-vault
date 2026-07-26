---
title: cacheIntermediates
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicontextoption/cacheintermediates
source_url: 'https://developer.apple.com/documentation/coreimage/cicontextoption/cacheintermediates'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontextoption/cacheintermediates.json'
content_hash: 'sha256:e2c55ee04dc60e42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContextOption](../cicontextoption.md)

# cacheIntermediates

<sub>Type Property</sub>

A Boolean value to control how a Core Image context caches the contents of any intermediate image buffers it uses during rendering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let cacheIntermediates: CIContextOption
```

## Discussion

If a context caches intermediate buffers, then subsequent renders of a similar image using the same context may be able to render faster. If a context does not cache intermediate buffers, then it may use less memory.

If the value for this option is:

- True: The context will cache intermediate results for future renders using the same context.
- False: The context will not cache intermediate results.
- Not specified: the default behavior True.

> [!note] Note
> - This option does affect how `/CIImage/imageByInsertingIntermediate` behaves.
> - This option does not affect how `/CIImage/imageByInsertingIntermediate:` behaves.

## See Also

### Type Properties

- [kCIContextAllowLowPower](allowlowpower.md) — A Boolean value to control the power level of Core Image context renders.
- [kCIContextHighQualityDownsample](highqualitydownsample.md) — A Boolean value to control the quality of image downsampling operations performed by the Core Image context.
- [kCIContextMemoryLimit](memorytarget.md) — A number value to control the maximum memory in megabytes that the context allocates for render tasks.
- [kCIContextName](name.md) — A Boolean value to specify a client-provided name for a context.
- [kCIContextOutputColorSpace](outputcolorspace.md) — A Core Image context option key to specify the default destination color space for rendering.
- [kCIContextOutputPremultiplied](outputpremultiplied.md) — A Boolean value to control how a Core Image context render produces alpha-premultiplied pixels.
- [kCIContextPriorityRequestLow](priorityrequestlow.md) — A Boolean value to control the priority Core Image context renders.
- [kCIContextUseSoftwareRenderer](usesoftwarerenderer.md) — A Boolean value to control if a Core Image context will use a software renderer.
- [kCIContextWorkingColorSpace](workingcolorspace.md) — A Core Image context option key to specify the working color space for rendering.
- [kCIContextWorkingFormat](workingformat.md) — A Core Image context option key to specify the pixel format to for intermediate results when rendering.
