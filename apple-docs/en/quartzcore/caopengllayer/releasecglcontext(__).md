---
title: 'releaseCGLContext(_:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.5+（10.14 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/quartzcore/caopengllayer/releasecglcontext(_:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/caopengllayer/releasecglcontext(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caopengllayer/releasecglcontext%28_%3A%29.json'
content_hash: 'sha256:0768dc9649d67dae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAOpenGLLayer](../caopengllayer.md)

# releaseCGLContext(_:)

<sub>Instance Method</sub>

Releases the specified rendering context.

> [!warning] Deprecated
> OpenGL is deprecated. (Define GL_SILENCE_DEPRECATION to silence these warnings)

<sub>Mac Catalyst, macOS</sub>

```swift
func releaseCGLContext(_ ctx: CGLContextObj)
```

## Parameters

- `ctx` — The rendering context to release.

## Discussion

This method is called when the OpenGL context that was previously returned by [- copyCGLContextForPixelFormat:](<copycglcontext(forpixelformat_).md>) is no longer needed.

You should not call this method directly, it is intended to be overridden by subclasses.

## See Also

### Managing the Rendering Context

- [- copyCGLContextForPixelFormat:](<copycglcontext(forpixelformat_).md>) — Returns the rendering context the receiver requires for the specified pixel format. _(deprecated)_
