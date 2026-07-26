---
title: CIContextOption
framework: Core Image
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicontextoption
source_url: 'https://developer.apple.com/documentation/coreimage/cicontextoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontextoption.json'
content_hash: 'sha256:95431d6c44e4c15e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIContextOption

<sub>Structure</sub>

An enum string type that your code can use to select different options when creating a Core Image context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct CIContextOption
```

## Overview

These option keys can be passed to `CIContext` creation APIs such as:

- `/CIContext/contextWithOptions:`
- `/CIContext/contextWithMTLDevice:options:`

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [kCIContextAllowLowPower](cicontextoption/allowlowpower.md) — A Boolean value to control the power level of Core Image context renders.
- [kCIContextCacheIntermediates](cicontextoption/cacheintermediates.md) — A Boolean value to control how a Core Image context caches the contents of any intermediate image buffers it uses during rendering.
- [kCIContextHighQualityDownsample](cicontextoption/highqualitydownsample.md) — A Boolean value to control the quality of image downsampling operations performed by the Core Image context.
- [kCIContextMemoryLimit](cicontextoption/memorytarget.md) — A number value to control the maximum memory in megabytes that the context allocates for render tasks.
- [kCIContextName](cicontextoption/name.md) — A Boolean value to specify a client-provided name for a context.
- [kCIContextOutputColorSpace](cicontextoption/outputcolorspace.md) — A Core Image context option key to specify the default destination color space for rendering.
- [kCIContextOutputPremultiplied](cicontextoption/outputpremultiplied.md) — A Boolean value to control how a Core Image context render produces alpha-premultiplied pixels.
- [kCIContextPriorityRequestLow](cicontextoption/priorityrequestlow.md) — A Boolean value to control the priority Core Image context renders.
- [kCIContextUseSoftwareRenderer](cicontextoption/usesoftwarerenderer.md) — A Boolean value to control if a Core Image context will use a software renderer.
- [kCIContextWorkingColorSpace](cicontextoption/workingcolorspace.md) — A Core Image context option key to specify the working color space for rendering.
- [kCIContextWorkingFormat](cicontextoption/workingformat.md) — A Core Image context option key to specify the pixel format to for intermediate results when rendering.
- [kCIContextCVMetalTextureCache](cicontextoption/cvmetaltexturecache.md) — A Core Video Metal texture cache object to improve the performance of Core Image context renders that use Core Video pixel buffers.

### Initializers

- [init(rawValue:)](<cicontextoption/init(rawvalue_).md>)
