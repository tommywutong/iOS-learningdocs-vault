---
title: CIRenderDestination
framework: Core Image
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cirenderdestination
source_url: 'https://developer.apple.com/documentation/coreimage/cirenderdestination'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirenderdestination.json'
content_hash: 'sha256:6af357be1ca86d22'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIRenderDestination

<sub>Class</sub>

A specification for configuring all attributes of a render task’s destination and issuing asynchronous render tasks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CIRenderDestination
```

## Overview

The `CIRenderDestination` class provides an API for specifying a render task destination’s properties, such as buffer format, alpha mode, clamping behavior, blending, and color space, properties formerly tied to [CIContext](cicontext.md).

You can create a `CIRenderDestination` object for each surface or buffer to which you must render. You can also render multiple times to a single destination with different settings such as colorspace and blend mode by mutating a single `CIRenderDestination` object between renders.

Renders issued to a `CIRenderDestination` return to the caller as soon as the CPU has issued the task, rather than after the GPU has performed the task, so you can start render tasks on subsequent frames without waiting for previous renders to finish. If the render fails, a [CIRenderTask](cirendertask.md) will return immediately.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a Render Destination

- [- initWithPixelBuffer:](<cirenderdestination/init(pixelbuffer_).md>) — Creates a render destination based on a Core Video pixel buffer.
- [- initWithIOSurface:](<cirenderdestination/init(iosurface_)-1hfcq.md>) — Creates a render destination based on an `IOSurface` object.
- [- initWithMTLTexture:commandBuffer:](<cirenderdestination/init(mtltexture_commandbuffer_)-2iu5i.md>) — Creates a render destination based on a Metal texture.
- [- initWithWidth:height:pixelFormat:commandBuffer:mtlTextureProvider:](<cirenderdestination/init(width_height_pixelformat_commandbuffer_mtltextureprovider_).md>) — Creates a render destination based on a Metal texture with specified pixel format.
- [- initWithGLTexture:target:width:height:](<cirenderdestination/init(gltexture_target_width_height_)-9ci8e.md>) — Creates a render destination based on an OpenGL texture.
- [- initWithBitmapData:width:height:bytesPerRow:format:](<cirenderdestination/init(bitmapdata_width_height_bytesperrow_format_).md>) — Creates a render destination based on a client-managed buffer.

### Customizing Rendering

- [alphaMode](cirenderdestination/alphamode.md) — The render destination’s representation of alpha (transparency) values.
- [CIRenderDestinationAlphaMode](cirenderdestinationalphamode.md) — Different ways of representing alpha.
- [blendKernel](cirenderdestination/blendkernel.md) — The destination’s blend kernel.
- [blendsInDestinationColorSpace](cirenderdestination/blendsindestinationcolorspace.md) — Indicator of whether to blend in the destination’s color space.
- [colorSpace](cirenderdestination/colorspace.md) — The destination’s color space.
- [width](cirenderdestination/width.md) — The render destination’s row width.
- [height](cirenderdestination/height.md) — The render destination’s buffer height.
- [clamped](cirenderdestination/isclamped.md) — Indicator of whether or not the destination clamps.
- [dithered](cirenderdestination/isdithered.md) — Indicator of whether or not the destination dithers.
- [flipped](cirenderdestination/isflipped.md) — Indicator of whether the destination is flipped.

### Initializers

- [init(GLTexture:target:width:height:)](<cirenderdestination/init(gltexture_target_width_height_)-6dbtl.md>)
- [init(IOSurface:)](<cirenderdestination/init(iosurface_)-5t5jd.md>)
- [init(MTLTexture:commandBuffer:)](<cirenderdestination/init(mtltexture_commandbuffer_)-5iasd.md>)

### Instance Properties

- [captureTraceURL](cirenderdestination/capturetraceurl.md) — Tell the next render using this destination to capture a Metal trace.

## See Also

### Custom Render Destination

- [Generating an animation with a Core Image Render Destination](generating-an-animation-with-a-core-image-render-destination.md) — Animate a filtered image to a Metal view in a SwiftUI app using a Core Image Render Destination.
- [CIRenderInfo](cirenderinfo.md) — An encapsulation of a render task’s timing, passes, and pixels processed.
- [CIRenderTask](cirendertask.md) — A single render task.
- [CIRenderDestinationAlphaMode](cirenderdestinationalphamode.md) — Different ways of representing alpha.
