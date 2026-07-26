---
title: canConformColorOfSourceFrames
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositing/canconformcolorofsourceframes
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositing/canconformcolorofsourceframes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositing/canconformcolorofsourceframes.json'
content_hash: 'sha256:34bf405e745b89ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositing](../avvideocompositing.md)

# canConformColorOfSourceFrames

<sub>Instance Property</sub>

A Boolean value that indicates whether the compositor conforms the color space of source frames to the composition color space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional var canConformColorOfSourceFrames: Bool { get }
```

## Discussion

A custom compositor indicates its processing requirements through the [sourcePixelBufferAttributes](sourcepixelbufferattributes.md) and [supportsWideColorSourceFrames](supportswidecolorsourceframes.md) properties. By default, the composition engine prepares source frames by converting them to meet the compositor’s configuration.

When this property value is true, the engine doesn’t convert source pixel buffers that meet the compositor’s processing requirements. However, it does convert buffers that don’t meet the processing requirements, which includes the following cases:

- The values of [supportsWideColorSourceFrames](supportswidecolorsourceframes.md) and [supportsHDRSourceFrames](supportshdrsourceframes.md) are [false](../../swift/false.md), but the source buffers contain wide color. In this case, the engine converts the color space of source pixel buffers to BT.709 color space. Note that when [supportsHDRSourceFrames](supportshdrsourceframes.md) is [true](../../swift/true.md), the engine also assumes [supportsWideColorSourceFrames](supportswidecolorsourceframes.md) is [true](../../swift/true.md).
- The value of [supportsHDRSourceFrames](supportshdrsourceframes.md) is [false](../../swift/false.md) and source buffers contain HDR color. In this case, the engine converts the color space of source pixel buffers to the composition color space.
- The pixel format of the source buffers isn’t specified in [sourcePixelBufferAttributes](sourcepixelbufferattributes.md). In this case, the engine converts the pixel format to a supported format and converts the color space to the composition color space.

## See Also

### Inspecting processing requirements

- [sourcePixelBufferAttributes](sourcepixelbufferattributes.md) — The pixel buffer attributes that the compositor accepts for source frames.
- [requiredPixelBufferAttributesForRenderContext](requiredpixelbufferattributesforrendercontext.md) — The pixel buffer attributes that the compositor requires for pixel buffers that it creates.
- [supportsHDRSourceFrames](supportshdrsourceframes.md) — A Boolean value that indicates whether the compositor handles source frames that contain high dynamic range (HDR) properties.
- [supportsWideColorSourceFrames](supportswidecolorsourceframes.md) — A Boolean value that indicates whether the compositor handles source frames that contains wide color properties.
- [supportsSourceTaggedBuffers](supportssourcetaggedbuffers.md)
