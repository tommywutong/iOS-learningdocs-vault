---
title: 'init(pngDataProviderSource:decode:shouldInterpolate:intent:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgimage/init(pngdataprovidersource:decode:shouldinterpolate:intent:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgimage/init(pngdataprovidersource:decode:shouldinterpolate:intent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgimage/init%28pngdataprovidersource%3Adecode%3Ashouldinterpolate%3Aintent%3A%29.json'
content_hash: 'sha256:e546210370410cb5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGImage](../cgimage.md)

# init(pngDataProviderSource:decode:shouldInterpolate:intent:)

<sub>Initializer</sub>

Creates a bitmap image using PNG-encoded data supplied by a data provider.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(pngDataProviderSource source: CGDataProvider, decode: UnsafePointer<CGFloat>?, shouldInterpolate: Bool, intent: CGColorRenderingIntent)
```

## Parameters

- `source` — A data provider supplying PNG-encoded data.

- `decode` — The decode array for the image. Typically a decode array is unnecessary, and you should pass `NULL`.

- `shouldInterpolate` — A Boolean value that specifies whether interpolation should occur. The interpolation setting specifies whether a pixel-smoothing algorithm should be applied to the image.

- `intent` — A CGColorRenderingIntent constant that specifies how to handle colors that are not located within the gamut of the destination color space of a graphics context.

## Return Value

A new CGImage. In Objective-C, you’re responsible for releasing this object by calling [CGImageRelease](../cgimagerelease.md).

## See Also

### Creating images

- [CGImageCreate](<init(width_height_bitspercomponent_bitsperpixel_bytesperrow_space_bitmapinfo_provider_decode_shouldinterpolate_intent_).md>) — Creates a bitmap image from data supplied by a data provider.
- [CGImageCreateWithJPEGDataProvider](<init(jpegdataprovidersource_decode_shouldinterpolate_intent_).md>) — Creates a bitmap image using JPEG-encoded data supplied by a data provider.
- [CGImageCreateWithContentHeadroom](<init(headroom_width_height_bitspercomponent_bitsperpixel_bytesperrow_space_bitmapinfo_provider_decode_shouldinterpolate_intent_).md>)
