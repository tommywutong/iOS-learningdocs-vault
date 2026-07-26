---
title: supportsWideColorSourceFrames
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositing/supportswidecolorsourceframes
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositing/supportswidecolorsourceframes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositing/supportswidecolorsourceframes.json'
content_hash: 'sha256:b0389902106b418b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositing](../avvideocompositing.md)

# supportsWideColorSourceFrames

<sub>Instance Property</sub>

A Boolean value that indicates whether the compositor handles source frames that contains wide color properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional var supportsWideColorSourceFrames: Bool { get }
```

## See Also

### Inspecting processing requirements

- [sourcePixelBufferAttributes](sourcepixelbufferattributes.md) — The pixel buffer attributes that the compositor accepts for source frames.
- [requiredPixelBufferAttributesForRenderContext](requiredpixelbufferattributesforrendercontext.md) — The pixel buffer attributes that the compositor requires for pixel buffers that it creates.
- [supportsHDRSourceFrames](supportshdrsourceframes.md) — A Boolean value that indicates whether the compositor handles source frames that contain high dynamic range (HDR) properties.
- [canConformColorOfSourceFrames](canconformcolorofsourceframes.md) — A Boolean value that indicates whether the compositor conforms the color space of source frames to the composition color space.
- [supportsSourceTaggedBuffers](supportssourcetaggedbuffers.md)
