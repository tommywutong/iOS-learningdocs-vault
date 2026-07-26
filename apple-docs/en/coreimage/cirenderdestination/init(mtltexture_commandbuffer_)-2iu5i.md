---
title: 'init(mtlTexture:commandBuffer:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cirenderdestination/init(mtltexture:commandbuffer:)-2iu5i'
source_url: 'https://developer.apple.com/documentation/coreimage/cirenderdestination/init(mtltexture:commandbuffer:)-2iu5i'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirenderdestination/init%28mtltexture%3Acommandbuffer%3A%29-2iu5i.json'
content_hash: 'sha256:bb5cf86c1270f7e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIRenderDestination](../cirenderdestination.md)

# init(mtlTexture:commandBuffer:)

<sub>Initializer</sub>

Creates a render destination based on a Metal texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(mtlTexture texture: any MTLTexture, commandBuffer: (any MTLCommandBuffer)?)
```

## Parameters

- `texture` — The [MTLTexture](../../metal/mtltexture.md) object for rendering with [MTLTextureType](../../metal/mtltexturetype.md) of [MTLTextureType.type2D](../../metal/mtltexturetype/type2d.md).

- `commandBuffer` — An optional [MTLCommandBuffer](../../metal/mtlcommandbuffer.md) to use for rendering to the [MTLTexture](../../metal/mtltexture.md) destination.

## Return Value

A [CIRenderDestination](../cirenderdestination.md) object for rendering to a Metal buffer.

## Discussion

Rendering to a [MTLTexture](../../metal/mtltexture.md)-backed [CIRenderDestination](../cirenderdestination.md) is supported by only [MTLTexture](../../metal/mtltexture.md)-backed [CIContext](../cicontext.md) objects.  The texture must have [MTLTextureType](../../metal/mtltexturetype.md) of [MTLTextureType.type2D](../../metal/mtltexturetype/type2d.md).

The destination’s [colorSpace](colorspace.md) property will default to a [CGColorSpace](../../coregraphics/cgcolorspace.md) created with [sRGB](../../coregraphics/cgcolorspace/srgb.md), [extendedSRGB](../../coregraphics/cgcolorspace/extendedsrgb.md), or [genericGrayGamma2_2](../../coregraphics/cgcolorspace/genericgraygamma2_2.md).

## See Also

### Creating a Render Destination

- [- initWithPixelBuffer:](<init(pixelbuffer_).md>) — Creates a render destination based on a Core Video pixel buffer.
- [- initWithIOSurface:](<init(iosurface_)-1hfcq.md>) — Creates a render destination based on an `IOSurface` object.
- [- initWithWidth:height:pixelFormat:commandBuffer:mtlTextureProvider:](<init(width_height_pixelformat_commandbuffer_mtltextureprovider_).md>) — Creates a render destination based on a Metal texture with specified pixel format.
- [- initWithGLTexture:target:width:height:](<init(gltexture_target_width_height_)-9ci8e.md>) — Creates a render destination based on an OpenGL texture.
- [- initWithBitmapData:width:height:bytesPerRow:format:](<init(bitmapdata_width_height_bytesperrow_format_).md>) — Creates a render destination based on a client-managed buffer.
