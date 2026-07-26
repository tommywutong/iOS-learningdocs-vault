---
title: 'releaseCGLPixelFormat(_:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.5+（10.14 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/quartzcore/caopengllayer/releasecglpixelformat(_:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/caopengllayer/releasecglpixelformat(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caopengllayer/releasecglpixelformat%28_%3A%29.json'
content_hash: 'sha256:e9dc3578465b3c3d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAOpenGLLayer](../caopengllayer.md)

# releaseCGLPixelFormat(_:)

<sub>Instance Method</sub>

Releases the specified OpenGL pixel format object.

> [!warning] Deprecated
> OpenGL is deprecated. (Define GL_SILENCE_DEPRECATION to silence these warnings)

<sub>Mac Catalyst, macOS</sub>

```swift
func releaseCGLPixelFormat(_ pf: CGLPixelFormatObj)
```

## Parameters

- `pf` — The pixel format object to release.

## Discussion

This method is called when the OpenGL pixel format that was previously returned by [- copyCGLContextForPixelFormat:](<copycglcontext(forpixelformat_).md>).

You should not call this method directly, it is intended to be overridden by subclasses.

## See Also

### Managing Pixel Format

- [- copyCGLPixelFormatForDisplayMask:](<copycglpixelformat(fordisplaymask_).md>) — Returns the OpenGL pixel format suitable for rendering to the set of displays specified by the display mask. _(deprecated)_
