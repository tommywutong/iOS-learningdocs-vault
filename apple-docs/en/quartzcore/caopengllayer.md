---
title: CAOpenGLLayer
framework: Core Animation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.5+（10.14 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/quartzcore/caopengllayer
source_url: 'https://developer.apple.com/documentation/quartzcore/caopengllayer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caopengllayer.json'
content_hash: 'sha256:2538eb77fbca1f92'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CAOpenGLLayer

<sub>Class</sub>

A layer that provides a layer suitable for rendering OpenGL content.

> [!warning] Deprecated
> OpenGL is deprecated. (Define GL_SILENCE_DEPRECATION to silence these warnings)

<sub>Mac Catalyst, macOS</sub>

```swift
class CAOpenGLLayer
```

## Overview

To provide OpenGL content you subclass `CAOpenGLLayer` and override [- drawInCGLContext:pixelFormat:forLayerTime:displayTime:](<caopengllayer/draw(incglcontext_pixelformat_forlayertime_displaytime_).md>). You can specify that the OpenGL content is static by setting the [asynchronous](caopengllayer/isasynchronous.md) property to [false](../swift/false.md).

## Relationships

- **Inherits From**: [CALayer](calayer.md)

- **Conforms To**: [CAMediaTiming](camediatiming.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Determining Layer Properties

- [colorspace](caopengllayer/colorspace.md) — The layer’s colorspace in Core Graphics. _(deprecated)_
- [wantsExtendedDynamicRangeContent](caopengllayer/wantsextendeddynamicrangecontent.md) — Tells whether or not the layer supports content with extended dynamic range. _(deprecated)_

### Drawing Layer Content

- [asynchronous](caopengllayer/isasynchronous.md) — Determines when the contents of the layer are updated. _(deprecated)_
- [- canDrawInCGLContext:pixelFormat:forLayerTime:displayTime:](<caopengllayer/candraw(incglcontext_pixelformat_forlayertime_displaytime_).md>) — Returns whether the receiver should draw OpenGL content for the specified time. _(deprecated)_
- [- drawInCGLContext:pixelFormat:forLayerTime:displayTime:](<caopengllayer/draw(incglcontext_pixelformat_forlayertime_displaytime_).md>) — Draws the OpenGL content for the specified time. _(deprecated)_

### Managing Pixel Format

- [- copyCGLPixelFormatForDisplayMask:](<caopengllayer/copycglpixelformat(fordisplaymask_).md>) — Returns the OpenGL pixel format suitable for rendering to the set of displays specified by the display mask. _(deprecated)_
- [- releaseCGLPixelFormat:](<caopengllayer/releasecglpixelformat(__).md>) — Releases the specified OpenGL pixel format object. _(deprecated)_

### Managing the Rendering Context

- [- copyCGLContextForPixelFormat:](<caopengllayer/copycglcontext(forpixelformat_).md>) — Returns the rendering context the receiver requires for the specified pixel format. _(deprecated)_
- [- releaseCGLContext:](<caopengllayer/releasecglcontext(__).md>) — Releases the specified rendering context. _(deprecated)_

## See Also

### Metal and OpenGL

- [CAMetalLayer](cametallayer.md) — A Core Animation layer that Metal can render into, typically displayed onscreen.
- [CAMetalDrawable](cametaldrawable.md) — A Metal drawable associated with a Core Animation layer.
- [CAEAGLLayer](caeagllayer.md) — A layer that supports drawing OpenGL content in iOS and tvOS applications. _(deprecated)_
- [CAEDRMetadata](caedrmetadata.md) — Metadata describing how extended dynamic range (EDR) values should be tone mapped.
- [CARenderer](carenderer.md) — A layer that allows an application to render a layer tree into a Core OpenGL context.
