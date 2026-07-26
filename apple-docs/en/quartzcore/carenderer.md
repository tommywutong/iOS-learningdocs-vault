---
title: CARenderer
framework: Core Animation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/carenderer
source_url: 'https://developer.apple.com/documentation/quartzcore/carenderer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/carenderer.json'
content_hash: 'sha256:e8706f274a22b254'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CARenderer

<sub>Class</sub>

A layer that allows an application to render a layer tree into a Core OpenGL context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CARenderer
```

## Overview

For real-time output you should use an instance of [NSView](../appkit/nsview.md) to host the layer-tree.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a Renderer

- [+ rendererWithCGLContext:options:](<carenderer/init(cglcontext_options_)-1l3m2.md>) — Creates and returns a `CARenderer` instance with the render target specified by the Core OpenGL context. _(deprecated)_
- [+ rendererWithMTLTexture:options:](<carenderer/init(mtltexture_options_)-1cr0b.md>) — Creates a layer renderer from a Metal texture.

### Getting the Rendered Layer

- [layer](carenderer/layer.md) — The root layer of the layer-tree the receiver should render.

### Determining Layer Bounds

- [bounds](carenderer/bounds.md) — The bounds of the receiver.

### Rendering a Frame

- [- beginFrameAtTime:timeStamp:](<carenderer/beginframe(attime_timestamp_).md>) — Begin rendering a frame at the specified time.
- [- updateBounds](<carenderer/updatebounds().md>) — Returns the bounds of the update region that contains all pixels that will be rendered by the current frame.
- [- addUpdateRect:](<carenderer/addupdate(__).md>) — Adds the rectangle to the update region of the current frame.
- [- render](<carenderer/render().md>) — Render the update region of the current frame to the target context.
- [- nextFrameTime](<carenderer/nextframetime().md>) — Returns the time at which the next update should happen.
- [- endFrame](<carenderer/endframe().md>) — Release any data associated with the current frame.

### Instance Methods

- [- setDestination:](<carenderer/setdestination(__).md>)

### Initializers

- [init(CGLContext:options:)](<carenderer/init(cglcontext_options_)-6ywk8.md>) _(deprecated)_
- [init(MTLTexture:options:)](<carenderer/init(mtltexture_options_)-51l7q.md>)

## See Also

### Metal and OpenGL

- [CAMetalLayer](cametallayer.md) — A Core Animation layer that Metal can render into, typically displayed onscreen.
- [CAMetalDrawable](cametaldrawable.md) — A Metal drawable associated with a Core Animation layer.
- [CAEAGLLayer](caeagllayer.md) — A layer that supports drawing OpenGL content in iOS and tvOS applications. _(deprecated)_
- [CAEDRMetadata](caedrmetadata.md) — Metadata describing how extended dynamic range (EDR) values should be tone mapped.
- [CAOpenGLLayer](caopengllayer.md) — A layer that provides a layer suitable for rendering OpenGL content. _(deprecated)_
