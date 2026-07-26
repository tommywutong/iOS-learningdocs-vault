---
title: 'draw(in:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayer/draw(in:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/draw(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/draw%28in%3A%29.json'
content_hash: 'sha256:92f9f1b777c0cd57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# draw(in:)

<sub>Instance Method</sub>

Draws the layer’s content using the specified graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func draw(in ctx: CGContext)
```

## Parameters

- `ctx` — The graphics context in which to draw the content. The context may be clipped to protect valid layer content. Subclasses that wish to find the actual region to draw can call [boundingBoxOfClipPath](../../coregraphics/cgcontext/boundingboxofclippath.md).

## Discussion

The default implementation of this method does not do any drawing itself. If the layer’s delegate implements the  [- drawLayer:inContext:](<../calayerdelegate/draw(__in_).md>) method, that method is called to do the actual drawing.

Subclasses can override this method and use it to draw the layer’s content. When drawing, all coordinates should be specified in points in the logical coordinate space.

## See Also

### Providing the layer’s content

- [contents](contents.md) — An object that provides the contents of the layer. Animatable.
- [contentsRect](contentsrect.md) — The rectangle, in the unit coordinate space, that defines the portion of the layer’s contents that should be used. Animatable.
- [contentsCenter](contentscenter.md) — The rectangle that defines how the layer contents are scaled if the layer’s contents are resized. Animatable.
- [- display](<display().md>) — Reloads the content of this layer.
