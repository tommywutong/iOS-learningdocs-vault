---
title: portraitEffectsMatte
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimage/portraiteffectsmatte
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/portraiteffectsmatte'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/portraiteffectsmatte.json'
content_hash: 'sha256:2cf450fe7baf745e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# portraitEffectsMatte

<sub>Instance Property</sub>

The portrait effects matte associated with the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var portraitEffectsMatte: AVPortraitEffectsMatte? { get }
```

## Discussion

[AVPortraitEffectsMatte](../../avfoundation/avportraiteffectsmatte.md) representation of portrait effects.

## See Also

### Accessing Original Image Content

- [CGImage](cgimage.md) — The CoreGraphics image object this image was created from, if applicable.
- [pixelBuffer](pixelbuffer.md) — The CoreVideo pixel buffer this image was created from, if applicable.
- [depthData](depthdata.md) — Depth data associated with the image.
- [semanticSegmentationMatte](semanticsegmentationmatte.md)
