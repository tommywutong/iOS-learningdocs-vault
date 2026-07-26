---
title: workingColorSpace
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicontextoption/workingcolorspace
source_url: 'https://developer.apple.com/documentation/coreimage/cicontextoption/workingcolorspace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontextoption/workingcolorspace.json'
content_hash: 'sha256:101dddb3dd80084a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContextOption](../cicontextoption.md)

# workingColorSpace

<sub>Type Property</sub>

A Core Image context option key to specify the working color space for rendering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let workingColorSpace: CIContextOption
```

## Discussion

Contexts support automatic color management by performing all processing operations in a working color space. This means that unless told otherwise:

- All input images are color matched from the input’s color space to the working space.
- All renders are color matched from the working space to the destination’s color space.

The default working space is the extended sRGB color space with linear gamma. On macOS before 10.10, the default is extended Generic RGB with linear gamma.

The value of this option can be either:

- A `CGColorSpace` instance with an RGB color model that supports output.
- An `NSNull` instance to request that Core Image perform no color management.

If this option is not specified, then the default working space is used.

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
- [kCIContextWorkingFormat](workingformat.md) — A Core Image context option key to specify the pixel format to for intermediate results when rendering.
