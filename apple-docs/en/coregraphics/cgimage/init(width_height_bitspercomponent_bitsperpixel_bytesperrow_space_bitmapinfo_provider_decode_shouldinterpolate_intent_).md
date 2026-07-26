---
title: 'init(width:height:bitsPerComponent:bitsPerPixel:bytesPerRow:space:bitmapInfo:provider:decode:shouldInterpolate:intent:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgimage/init(width:height:bitspercomponent:bitsperpixel:bytesperrow:space:bitmapinfo:provider:decode:shouldinterpolate:intent:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgimage/init(width:height:bitspercomponent:bitsperpixel:bytesperrow:space:bitmapinfo:provider:decode:shouldinterpolate:intent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgimage/init%28width%3Aheight%3Abitspercomponent%3Abitsperpixel%3Abytesperrow%3Aspace%3Abitmapinfo%3Aprovider%3Adecode%3Ashouldinterpolate%3Aintent%3A%29.json'
content_hash: 'sha256:cd87e53268e71ad4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGImage](../cgimage.md)

# init(width:height:bitsPerComponent:bitsPerPixel:bytesPerRow:space:bitmapInfo:provider:decode:shouldInterpolate:intent:)

<sub>Initializer</sub>

Creates a bitmap image from data supplied by a data provider.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(width: Int, height: Int, bitsPerComponent: Int, bitsPerPixel: Int, bytesPerRow: Int, space: CGColorSpace, bitmapInfo: CGBitmapInfo, provider: CGDataProvider, decode: UnsafePointer<CGFloat>?, shouldInterpolate: Bool, intent: CGColorRenderingIntent)
```

## Parameters

- `width` — The width, in pixels, of the required image.

- `height` — The height, in pixels, of the required image

- `bitsPerComponent` — The number of bits for each component in a source pixel. For example, if the source image uses the RGBA-32 format, you would specify 8 bits per component.

- `bitsPerPixel` — The total number of bits in a source pixel. This value must be at least `bitsPerComponent` times the number of components per pixel.

- `bytesPerRow` — The number of bytes of memory for each horizontal row of the bitmap.

- `space` — The color space for the image. The color space is retained; on return, you may safely release it.

- `bitmapInfo` — A constant that specifies whether the bitmap should contain an alpha channel and its relative location in a pixel, along with whether the components are floating-point or integer values.

- `provider` — The source of data for the bitmap. For information about supported data formats, see the discussion below. The provider is retained; on return, you may safely release it.

- `decode` — The decode array for the image. If you do not want to allow remapping of the image’s color values, pass `NULL` for the decode array. For each color component in the image’s color space (including the alpha component), a decode array provides a pair of values denoting the upper and lower limits of a range. For example, the decode array for a source image in the RGB color space would contain six entries total, consisting of one pair each for red, green, and blue. When the image is rendered, Core Graphics uses a linear transform to map the original component value into a relative number within your designated range that is appropriate for the destination color space.

- `shouldInterpolate` — A Boolean value that specifies whether interpolation should occur. The interpolation setting specifies whether Core Graphics should apply a pixel-smoothing algorithm to the image. Without interpolation, the image may appear jagged or pixelated when drawn on an output device with higher resolution than the image data.

- `intent` — A rendering intent constant that specifies how Core Graphics should handle colors that are not located within the gamut of the destination color space of a graphics context. The rendering intent determines the exact method used to map colors from one color space to another. For descriptions of the defined rendering-intent constants, see [CGColorRenderingIntent](../cgcolorrenderingintent.md).

## Return Value

A new bitmap image. In Objective-C, you’re responsible for releasing this object by calling [CGImageRelease](../cgimagerelease.md).

## Discussion

The data provider should provide raw data that matches the format specified by the other input parameters. To use encoded data (for example, from a file specified by a URL-based data provider), see [CGImageCreateWithJPEGDataProvider](<init(jpegdataprovidersource_decode_shouldinterpolate_intent_).md>) and [CGImageCreateWithPNGDataProvider](<init(pngdataprovidersource_decode_shouldinterpolate_intent_).md>).

For information on supported pixel formats, see [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066).

## See Also

### Creating images

- [CGImageCreateWithJPEGDataProvider](<init(jpegdataprovidersource_decode_shouldinterpolate_intent_).md>) — Creates a bitmap image using JPEG-encoded data supplied by a data provider.
- [CGImageCreateWithPNGDataProvider](<init(pngdataprovidersource_decode_shouldinterpolate_intent_).md>) — Creates a bitmap image using PNG-encoded data supplied by a data provider.
- [CGImageCreateWithContentHeadroom](<init(headroom_width_height_bitspercomponent_bitsperpixel_bytesperrow_space_bitmapinfo_provider_decode_shouldinterpolate_intent_).md>)
