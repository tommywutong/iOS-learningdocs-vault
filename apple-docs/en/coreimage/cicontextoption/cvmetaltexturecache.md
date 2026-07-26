---
title: cvMetalTextureCache
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicontextoption/cvmetaltexturecache
source_url: 'https://developer.apple.com/documentation/coreimage/cicontextoption/cvmetaltexturecache'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontextoption/cvmetaltexturecache.json'
content_hash: 'sha256:860d698700c111f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContextOption](../cicontextoption.md)

# cvMetalTextureCache

<sub>Type Property</sub>

A Core Video Metal texture cache object to improve the performance of Core Image context renders that use Core Video pixel buffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let cvMetalTextureCache: CIContextOption
```

## Discussion

Creating a Core Image context with this optional `CVMetalTextureCache` can improve the performance of creating a Metal texture from a `CVPixelBuffer`. It is recommended to specify this option if the context renders to or from pixel buffers that come from a `CVPixelBufferPool`.

It is the client’s responsibility to flush the cache when appropriate.
