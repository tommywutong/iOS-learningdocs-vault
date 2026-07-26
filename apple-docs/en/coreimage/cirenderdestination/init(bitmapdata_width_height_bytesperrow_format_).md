---
title: 'init(bitmapData:width:height:bytesPerRow:format:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cirenderdestination/init(bitmapdata:width:height:bytesperrow:format:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cirenderdestination/init(bitmapdata:width:height:bytesperrow:format:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirenderdestination/init%28bitmapdata%3Awidth%3Aheight%3Abytesperrow%3Aformat%3A%29.json'
content_hash: 'sha256:3c8f6cb7a85dee69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIRenderDestination](../cirenderdestination.md)

# init(bitmapData:width:height:bytesPerRow:format:)

<sub>Initializer</sub>

Creates a render destination based on a client-managed buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(bitmapData data: UnsafeMutableRawPointer, width: Int, height: Int, bytesPerRow: Int, format: CIFormat)
```

## Parameters

- `data` — Pointer to raw bits of a client-managed buffer that is at least (`bytesPerRow` * `height`) bytes in size.

- `width` — Width of the bitmap image in pixels.

- `height` — Height of the bitmap image in pixels.

- `bytesPerRow` — Number of bytes per row of data.

- `format` — Color format specifying how the colors are laid out in memory (for example, [kCIFormatRGBA8](../ciformat/rgba8.md)).

## Return Value

A [CIRenderDestination](../cirenderdestination.md) object for rendering to a client-managed buffer.

## Discussion

The destination’s [colorSpace](../ciimage/colorspace.md) property will default to a [CGColorSpace](../../coregraphics/cgcolorspace.md) created with [sRGB](../../coregraphics/cgcolorspace/srgb.md), [extendedSRGB](../../coregraphics/cgcolorspace/extendedsrgb.md), or [genericGrayGamma2_2](../../coregraphics/cgcolorspace/genericgraygamma2_2.md).

## See Also

### Creating a Render Destination

- [- initWithPixelBuffer:](<init(pixelbuffer_).md>) — Creates a render destination based on a Core Video pixel buffer.
- [- initWithIOSurface:](<init(iosurface_)-1hfcq.md>) — Creates a render destination based on an `IOSurface` object.
- [- initWithMTLTexture:commandBuffer:](<init(mtltexture_commandbuffer_)-2iu5i.md>) — Creates a render destination based on a Metal texture.
- [- initWithWidth:height:pixelFormat:commandBuffer:mtlTextureProvider:](<init(width_height_pixelformat_commandbuffer_mtltextureprovider_).md>) — Creates a render destination based on a Metal texture with specified pixel format.
- [- initWithGLTexture:target:width:height:](<init(gltexture_target_width_height_)-9ci8e.md>) — Creates a render destination based on an OpenGL texture.
