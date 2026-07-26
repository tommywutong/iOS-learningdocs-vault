---
title: 'init(headroom:width:height:bitsPerComponent:bitsPerPixel:bytesPerRow:space:bitmapInfo:provider:decode:shouldInterpolate:intent:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgimage/init(headroom:width:height:bitspercomponent:bitsperpixel:bytesperrow:space:bitmapinfo:provider:decode:shouldinterpolate:intent:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgimage/init(headroom:width:height:bitspercomponent:bitsperpixel:bytesperrow:space:bitmapinfo:provider:decode:shouldinterpolate:intent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgimage/init%28headroom%3Awidth%3Aheight%3Abitspercomponent%3Abitsperpixel%3Abytesperrow%3Aspace%3Abitmapinfo%3Aprovider%3Adecode%3Ashouldinterpolate%3Aintent%3A%29.json'
content_hash: 'sha256:ad0778101910b222'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGImage](../cgimage.md)

# init(headroom:width:height:bitsPerComponent:bitsPerPixel:bytesPerRow:space:bitmapInfo:provider:decode:shouldInterpolate:intent:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(headroom: Float, width: Int, height: Int, bitsPerComponent: Int, bitsPerPixel: Int, bytesPerRow: Int, space: CGColorSpace, bitmapInfo: CGBitmapInfo, provider: CGDataProvider, decode: UnsafePointer<CGFloat>?, shouldInterpolate: Bool, intent: CGColorRenderingIntent)
```

## See Also

### Creating images

- [CGImageCreate](<init(width_height_bitspercomponent_bitsperpixel_bytesperrow_space_bitmapinfo_provider_decode_shouldinterpolate_intent_).md>) — Creates a bitmap image from data supplied by a data provider.
- [CGImageCreateWithJPEGDataProvider](<init(jpegdataprovidersource_decode_shouldinterpolate_intent_).md>) — Creates a bitmap image using JPEG-encoded data supplied by a data provider.
- [CGImageCreateWithPNGDataProvider](<init(pngdataprovidersource_decode_shouldinterpolate_intent_).md>) — Creates a bitmap image using PNG-encoded data supplied by a data provider.
