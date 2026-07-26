---
title: isAsynchronous
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.5+（10.14 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/quartzcore/caopengllayer/isasynchronous
source_url: 'https://developer.apple.com/documentation/quartzcore/caopengllayer/isasynchronous'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caopengllayer/isasynchronous.json'
content_hash: 'sha256:d1cc5c862149a433'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAOpenGLLayer](../caopengllayer.md)

# isAsynchronous

<sub>Instance Property</sub>

Determines when the contents of the layer are updated.

> [!warning] Deprecated
> OpenGL is deprecated. (Define GL_SILENCE_DEPRECATION to silence these warnings)

<sub>Mac Catalyst, macOS</sub>

```swift
var isAsynchronous: Bool { get set }
```

## Discussion

If [false](../../swift/false.md), the contents of the layer are updated only in response to receiving a [- setNeedsDisplay](<../calayer/setneedsdisplay().md>) message. When [true](../../swift/true.md), the receiver’s [- canDrawInCGLContext:pixelFormat:forLayerTime:displayTime:](<candraw(incglcontext_pixelformat_forlayertime_displaytime_).md>) is called periodically to determine if the OpenGL content should be updated.

## See Also

### Related Documentation

- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)

### Drawing Layer Content

- [- canDrawInCGLContext:pixelFormat:forLayerTime:displayTime:](<candraw(incglcontext_pixelformat_forlayertime_displaytime_).md>) — Returns whether the receiver should draw OpenGL content for the specified time. _(deprecated)_
- [- drawInCGLContext:pixelFormat:forLayerTime:displayTime:](<draw(incglcontext_pixelformat_forlayertime_displaytime_).md>) — Draws the OpenGL content for the specified time. _(deprecated)_
