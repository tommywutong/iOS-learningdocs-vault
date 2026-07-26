---
title: supportsHDRSourceFrames
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositing/supportshdrsourceframes
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositing/supportshdrsourceframes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositing/supportshdrsourceframes.json'
content_hash: 'sha256:968b5a7e03436f35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositing](../avvideocompositing.md)

# supportsHDRSourceFrames

<sub>Instance Property</sub>

A Boolean value that indicates whether the compositor handles source frames that contain high dynamic range (HDR) properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional var supportsHDRSourceFrames: Bool { get }
```

## See Also

### Inspecting processing requirements

- [sourcePixelBufferAttributes](sourcepixelbufferattributes.md) — The pixel buffer attributes that the compositor accepts for source frames.
- [requiredPixelBufferAttributesForRenderContext](requiredpixelbufferattributesforrendercontext.md) — The pixel buffer attributes that the compositor requires for pixel buffers that it creates.
- [supportsWideColorSourceFrames](supportswidecolorsourceframes.md) — A Boolean value that indicates whether the compositor handles source frames that contains wide color properties.
- [canConformColorOfSourceFrames](canconformcolorofsourceframes.md) — A Boolean value that indicates whether the compositor conforms the color space of source frames to the composition color space.
- [supportsSourceTaggedBuffers](supportssourcetaggedbuffers.md)
