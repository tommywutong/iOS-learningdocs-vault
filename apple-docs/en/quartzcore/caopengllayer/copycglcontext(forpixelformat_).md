---
title: 'copyCGLContext(forPixelFormat:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.5+（10.14 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/quartzcore/caopengllayer/copycglcontext(forpixelformat:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/caopengllayer/copycglcontext(forpixelformat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caopengllayer/copycglcontext%28forpixelformat%3A%29.json'
content_hash: 'sha256:51e5bf0c9c87ba18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAOpenGLLayer](../caopengllayer.md)

# copyCGLContext(forPixelFormat:)

<sub>Instance Method</sub>

Returns the rendering context the receiver requires for the specified pixel format.

> [!warning] Deprecated
> OpenGL is deprecated. (Define GL_SILENCE_DEPRECATION to silence these warnings)

<sub>Mac Catalyst, macOS</sub>

```swift
func copyCGLContext(forPixelFormat pf: CGLPixelFormatObj) -> CGLContextObj
```

## Parameters

- `pf` — The pixel format for the rendering context.

## Return Value

A new `CGLContext` with renderers for `pixelFormat`.

## Discussion

This method is called when a rendering context is needed by the receiver. The default implementation allocates a new context with a null share context.

You should not call this method directly, it is intended to be overridden by subclasses.

## See Also

### Managing the Rendering Context

- [- releaseCGLContext:](<releasecglcontext(__).md>) — Releases the specified rendering context. _(deprecated)_
