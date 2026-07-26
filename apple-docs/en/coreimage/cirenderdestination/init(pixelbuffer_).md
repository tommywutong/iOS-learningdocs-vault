---
title: 'init(pixelBuffer:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cirenderdestination/init(pixelbuffer:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cirenderdestination/init(pixelbuffer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirenderdestination/init%28pixelbuffer%3A%29.json'
content_hash: 'sha256:298805fcbed4ce09'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIRenderDestination](../cirenderdestination.md)

# init(pixelBuffer:)

<sub>Initializer</sub>

Creates a render destination based on a Core Video pixel buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(pixelBuffer: CVPixelBuffer)
```

## Parameters

- `pixelBuffer` — The [CVPixelBuffer](../../corevideo/cvpixelbuffer.md) render target.

## Return Value

A [CIRenderDestination](../cirenderdestination.md) object for rendering to a [CVPixelBuffer](../../corevideo/cvpixelbuffer.md).

## Discussion

The destination’s [colorSpace](colorspace.md) property will default to a [CGColorSpace](../../coregraphics/cgcolorspace.md) created by querying the [CVPixelBuffer](../../corevideo/cvpixelbuffer.md) object’s attributes.

## See Also

### Creating a Render Destination

- [- initWithIOSurface:](<init(iosurface_)-1hfcq.md>) — Creates a render destination based on an `IOSurface` object.
- [- initWithMTLTexture:commandBuffer:](<init(mtltexture_commandbuffer_)-2iu5i.md>) — Creates a render destination based on a Metal texture.
- [- initWithWidth:height:pixelFormat:commandBuffer:mtlTextureProvider:](<init(width_height_pixelformat_commandbuffer_mtltextureprovider_).md>) — Creates a render destination based on a Metal texture with specified pixel format.
- [- initWithGLTexture:target:width:height:](<init(gltexture_target_width_height_)-9ci8e.md>) — Creates a render destination based on an OpenGL texture.
- [- initWithBitmapData:width:height:bytesPerRow:format:](<init(bitmapdata_width_height_bytesperrow_format_).md>) — Creates a render destination based on a client-managed buffer.
