---
title: 'copyCGLPixelFormat(forDisplayMask:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.5+（10.14 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/quartzcore/caopengllayer/copycglpixelformat(fordisplaymask:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/caopengllayer/copycglpixelformat(fordisplaymask:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caopengllayer/copycglpixelformat%28fordisplaymask%3A%29.json'
content_hash: 'sha256:785294668652c3c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAOpenGLLayer](../caopengllayer.md)

# copyCGLPixelFormat(forDisplayMask:)

<sub>Instance Method</sub>

Returns the OpenGL pixel format suitable for rendering to the set of displays specified by the display mask.

> [!warning] Deprecated
> OpenGL is deprecated. (Define GL_SILENCE_DEPRECATION to silence these warnings)

<sub>Mac Catalyst, macOS</sub>

```swift
func copyCGLPixelFormat(forDisplayMask mask: UInt32) -> CGLPixelFormatObj
```

## Parameters

- `mask` — The display mask the OpenGL content will be rendered on.

## Discussion

This method is called when a pixel format object is needed for the receiver.  The default implementation returns a 32bpp fixed point pixelf format, with the `NoRecovery` and `Accelerated` flags set.

You should not call this method directly, it is intended to be overridden by subclasses.

## See Also

### Managing Pixel Format

- [- releaseCGLPixelFormat:](<releasecglpixelformat(__).md>) — Releases the specified OpenGL pixel format object. _(deprecated)_
