---
title: 'draw(inCGLContext:pixelFormat:forLayerTime:displayTime:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.5+（10.14 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/quartzcore/caopengllayer/draw(incglcontext:pixelformat:forlayertime:displaytime:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/caopengllayer/draw(incglcontext:pixelformat:forlayertime:displaytime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caopengllayer/draw%28incglcontext%3Apixelformat%3Aforlayertime%3Adisplaytime%3A%29.json'
content_hash: 'sha256:6470724b05e71439'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAOpenGLLayer](../caopengllayer.md)

# draw(inCGLContext:pixelFormat:forLayerTime:displayTime:)

<sub>Instance Method</sub>

Draws the OpenGL content for the specified time.

> [!warning] Deprecated
> OpenGL is deprecated. (Define GL_SILENCE_DEPRECATION to silence these warnings)

<sub>Mac Catalyst, macOS</sub>

```swift
func draw(inCGLContext ctx: CGLContextObj, pixelFormat pf: CGLPixelFormatObj, forLayerTime t: CFTimeInterval, displayTime ts: UnsafePointer<CVTimeStamp>?)
```

## Parameters

- `ctx` — The rendering context in to which the OpenGL content should be rendered.

- `pf` — The pixel format used when the `glContext` was created.

- `t` — The current layer time.

- `ts` — The display timestamp associated with `timeInterval`. Can be `null`.

## Discussion

This method is called when a new frame needs to be generated for the layer time specified by `timeInterval`. The viewport of `glContext` is set correctly for the size of the layer. No other state is defined. If the method enables OpenGL features, it should disable them before returning.

The default implementation of the method flushes the context.

## See Also

### Drawing Layer Content

- [asynchronous](isasynchronous.md) — Determines when the contents of the layer are updated. _(deprecated)_
- [- canDrawInCGLContext:pixelFormat:forLayerTime:displayTime:](<candraw(incglcontext_pixelformat_forlayertime_displaytime_).md>) — Returns whether the receiver should draw OpenGL content for the specified time. _(deprecated)_
