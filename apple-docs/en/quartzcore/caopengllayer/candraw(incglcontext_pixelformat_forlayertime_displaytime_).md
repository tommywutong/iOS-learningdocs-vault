---
title: 'canDraw(inCGLContext:pixelFormat:forLayerTime:displayTime:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.5+（10.14 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/quartzcore/caopengllayer/candraw(incglcontext:pixelformat:forlayertime:displaytime:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/caopengllayer/candraw(incglcontext:pixelformat:forlayertime:displaytime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caopengllayer/candraw%28incglcontext%3Apixelformat%3Aforlayertime%3Adisplaytime%3A%29.json'
content_hash: 'sha256:a0a9636307e29d17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAOpenGLLayer](../caopengllayer.md)

# canDraw(inCGLContext:pixelFormat:forLayerTime:displayTime:)

<sub>Instance Method</sub>

Returns whether the receiver should draw OpenGL content for the specified time.

> [!warning] Deprecated
> OpenGL is deprecated. (Define GL_SILENCE_DEPRECATION to silence these warnings)

<sub>Mac Catalyst, macOS</sub>

```swift
func canDraw(inCGLContext ctx: CGLContextObj, pixelFormat pf: CGLPixelFormatObj, forLayerTime t: CFTimeInterval, displayTime ts: UnsafePointer<CVTimeStamp>?) -> Bool
```

## Parameters

- `ctx` — The `CGLContextObj` in to which the OpenGL content would be drawn.

- `pf` — The pixel format used when the `glContext` was created.

- `t` — The current layer time.

- `ts` — The display timestamp associated with `timeInterval`. Can be `null`.

## Return Value

[true](../../swift/true.md) if the receiver should render OpenGL content, [false](../../swift/false.md) otherwise.

## Discussion

This method is called before attempting to render the frame for the layer time specified by `timeInterval`. If the method returns [false](../../swift/false.md), the frame is skipped. The default implementation always returns [true](../../swift/true.md).

## See Also

### Drawing Layer Content

- [asynchronous](isasynchronous.md) — Determines when the contents of the layer are updated. _(deprecated)_
- [- drawInCGLContext:pixelFormat:forLayerTime:displayTime:](<draw(incglcontext_pixelformat_forlayertime_displaytime_).md>) — Draws the OpenGL content for the specified time. _(deprecated)_
