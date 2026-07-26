---
title: 'init(glTexture:target:width:height:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cirenderdestination/init(gltexture:target:width:height:)-9ci8e'
source_url: 'https://developer.apple.com/documentation/coreimage/cirenderdestination/init(gltexture:target:width:height:)-9ci8e'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirenderdestination/init%28gltexture%3Atarget%3Awidth%3Aheight%3A%29-9ci8e.json'
content_hash: 'sha256:371f59773d5dad28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIRenderDestination](../cirenderdestination.md)

# init(glTexture:target:width:height:)

<sub>Initializer</sub>

Creates a render destination based on an OpenGL texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(glTexture texture: UInt32, target: UInt32, width: Int, height: Int)
```

## Parameters

- `texture` — `GLTexture`-backed texture data.

- `target` — A value denoting the type of destination.  Use `GL_TEXTURE_2D` if your texture dimensions are a power of two, or `GL_TEXTURE_RECTANGLE_EXT` otherwise.

- `width` — Width of the texture in texels.

- `height` — Height of the texture in texels.

## Return Value

A [CIRenderDestination](../cirenderdestination.md) object for rendering to a `GLTexture` supported by `GLContext`-backed [CIContext](../cicontext.md).

## Discussion

Rendering to a `GLTexture`-backed [CIRenderDestination](../cirenderdestination.md) is supported by only `GLContext`-backed [CIContext](../cicontext.md).

The destination’s [colorSpace](colorspace.md) property will default to a [CGColorSpace](../../coregraphics/cgcolorspace.md) created with [sRGB](../../coregraphics/cgcolorspace/srgb.md), [extendedSRGB](../../coregraphics/cgcolorspace/extendedsrgb.md), or [genericGrayGamma2_2](../../coregraphics/cgcolorspace/genericgraygamma2_2.md).

## See Also

### Creating a Render Destination

- [- initWithPixelBuffer:](<init(pixelbuffer_).md>) — Creates a render destination based on a Core Video pixel buffer.
- [- initWithIOSurface:](<init(iosurface_)-1hfcq.md>) — Creates a render destination based on an `IOSurface` object.
- [- initWithMTLTexture:commandBuffer:](<init(mtltexture_commandbuffer_)-2iu5i.md>) — Creates a render destination based on a Metal texture.
- [- initWithWidth:height:pixelFormat:commandBuffer:mtlTextureProvider:](<init(width_height_pixelformat_commandbuffer_mtltextureprovider_).md>) — Creates a render destination based on a Metal texture with specified pixel format.
- [- initWithBitmapData:width:height:bytesPerRow:format:](<init(bitmapdata_width_height_bytesperrow_format_).md>) — Creates a render destination based on a client-managed buffer.
