---
title: supportsSourceTaggedBuffers
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositing/supportssourcetaggedbuffers
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositing/supportssourcetaggedbuffers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositing/supportssourcetaggedbuffers.json'
content_hash: 'sha256:a6601c760cc1a0df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositing](../avvideocompositing.md)

# supportsSourceTaggedBuffers

<sub>Instance Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional var supportsSourceTaggedBuffers: Bool { get }
```

## See Also

### Inspecting processing requirements

- [sourcePixelBufferAttributes](sourcepixelbufferattributes.md) — The pixel buffer attributes that the compositor accepts for source frames.
- [requiredPixelBufferAttributesForRenderContext](requiredpixelbufferattributesforrendercontext.md) — The pixel buffer attributes that the compositor requires for pixel buffers that it creates.
- [supportsHDRSourceFrames](supportshdrsourceframes.md) — A Boolean value that indicates whether the compositor handles source frames that contain high dynamic range (HDR) properties.
- [supportsWideColorSourceFrames](supportswidecolorsourceframes.md) — A Boolean value that indicates whether the compositor handles source frames that contains wide color properties.
- [canConformColorOfSourceFrames](canconformcolorofsourceframes.md) — A Boolean value that indicates whether the compositor conforms the color space of source frames to the composition color space.
