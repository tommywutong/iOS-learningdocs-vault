---
title: 'init(width:height:pixelFormat:commandBuffer:mtlTextureProvider:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cirenderdestination/init(width:height:pixelformat:commandbuffer:mtltextureprovider:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cirenderdestination/init(width:height:pixelformat:commandbuffer:mtltextureprovider:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirenderdestination/init%28width%3Aheight%3Apixelformat%3Acommandbuffer%3Amtltextureprovider%3A%29.json'
content_hash: 'sha256:95aaa875307cd9ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIRenderDestination](../cirenderdestination.md)

# init(width:height:pixelFormat:commandBuffer:mtlTextureProvider:)

<sub>Initializer</sub>

Creates a render destination based on a Metal texture with specified pixel format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(width: Int, height: Int, pixelFormat: MTLPixelFormat, commandBuffer: (any MTLCommandBuffer)?, mtlTextureProvider block: (() -> any MTLTexture)? = nil)
```

## Parameters

- `width` — Width of the [MTLTexture](../../metal/mtltexture.md) that will be returned by block.

- `height` — Height of the [MTLTexture](../../metal/mtltexture.md) that will be returned by block.

- `pixelFormat` — Pixel format of the [MTLTexture](../../metal/mtltexture.md) that will be returned by block.

- `commandBuffer` — An optional [MTLCommandBuffer](../../metal/mtlcommandbuffer.md) used for rendering to the [MTLTexture](../../metal/mtltexture.md).

- `block` — [MTLTexture](../../metal/mtltexture.md)-rendering provider block to be called lazily when the destination is rendered to.  The block must return a texture of [MTLTextureType](../../metal/mtltexturetype.md) of [MTLTextureType.type2D](../../metal/mtltexturetype/type2d.md).

## Return Value

A [CIRenderDestination](../cirenderdestination.md) object for rendering to a Metal texture.

## Discussion

The destination’s [colorSpace](colorspace.md) property will default to a [CGColorSpace](../../coregraphics/cgcolorspace.md) created with [sRGB](../../coregraphics/cgcolorspace/srgb.md), [extendedSRGB](../../coregraphics/cgcolorspace/extendedsrgb.md), or [genericGrayGamma2_2](../../coregraphics/cgcolorspace/genericgraygamma2_2.md).

## See Also

### Creating a Render Destination

- [- initWithPixelBuffer:](<init(pixelbuffer_).md>) — Creates a render destination based on a Core Video pixel buffer.
- [- initWithIOSurface:](<init(iosurface_)-1hfcq.md>) — Creates a render destination based on an `IOSurface` object.
- [- initWithMTLTexture:commandBuffer:](<init(mtltexture_commandbuffer_)-2iu5i.md>) — Creates a render destination based on a Metal texture.
- [- initWithGLTexture:target:width:height:](<init(gltexture_target_width_height_)-9ci8e.md>) — Creates a render destination based on an OpenGL texture.
- [- initWithBitmapData:width:height:bytesPerRow:format:](<init(bitmapdata_width_height_bytesperrow_format_).md>) — Creates a render destination based on a client-managed buffer.
