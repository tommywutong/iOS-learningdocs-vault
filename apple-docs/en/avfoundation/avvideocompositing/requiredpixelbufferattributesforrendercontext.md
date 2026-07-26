---
title: requiredPixelBufferAttributesForRenderContext
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositing/requiredpixelbufferattributesforrendercontext
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositing/requiredpixelbufferattributesforrendercontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositing/requiredpixelbufferattributesforrendercontext.json'
content_hash: 'sha256:59f59d9c631a6e41'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositing](../avvideocompositing.md)

# requiredPixelBufferAttributesForRenderContext

<sub>Instance Property</sub>

The pixel buffer attributes that the compositor requires for pixel buffers that it creates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var requiredPixelBufferAttributesForRenderContext: [String : any Sendable] { get }
```

## Discussion

The property is required to provide a [kCVPixelBufferPixelFormatTypeKey](../../corevideo/kcvpixelbufferpixelformattypekey.md) key in the dictionary, along with attributes for which the compositor needs specific values to work properly. Omitted attributes will be supplied by the composition engine to allow for the best performance. If the attribute [kCVPixelBufferPixelFormatTypeKey](../../corevideo/kcvpixelbufferpixelformattypekey.md) key is not in the dictionary an exception will be raised. The value of the [kCVPixelBufferPixelFormatTypeKey](../../corevideo/kcvpixelbufferpixelformattypekey.md) is an array of `kCVPixelFormatType_*` constants as defined in Pixel_Format_Types.

The value of `requiredPixelBufferAttributesForRenderContext` is retrieved prior to the creation of a new render context; the combination of the attributes in the returned value and the additional attributes supplied by the composition engine will be used in the creation of subsequent render context’s pixelBuffers.

This property is queried once before any composition request is sent to the compositor. Changing required buffer attributes afterwards is not supported.

## See Also

### Inspecting processing requirements

- [sourcePixelBufferAttributes](sourcepixelbufferattributes.md) — The pixel buffer attributes that the compositor accepts for source frames.
- [supportsHDRSourceFrames](supportshdrsourceframes.md) — A Boolean value that indicates whether the compositor handles source frames that contain high dynamic range (HDR) properties.
- [supportsWideColorSourceFrames](supportswidecolorsourceframes.md) — A Boolean value that indicates whether the compositor handles source frames that contains wide color properties.
- [canConformColorOfSourceFrames](canconformcolorofsourceframes.md) — A Boolean value that indicates whether the compositor conforms the color space of source frames to the composition color space.
- [supportsSourceTaggedBuffers](supportssourcetaggedbuffers.md)
