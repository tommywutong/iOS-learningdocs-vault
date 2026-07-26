---
title: contentsRect
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/contentsrect
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/contentsrect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/contentsrect.json'
content_hash: 'sha256:b1716c59603fa323'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# contentsRect

<sub>Instance Property</sub>

The rectangle, in the unit coordinate space, that defines the portion of the layer’s contents that should be used. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var contentsRect: CGRect { get set }
```

## Discussion

Defaults to the unit rectangle (0.0, 0.0, 1.0, 1.0).

If pixels outside the unit rectangle are requested, the edge pixels of the contents image will be extended outwards.

If an empty rectangle is provided, the results are undefined.

## See Also

### Providing the layer’s content

- [contents](contents.md) — An object that provides the contents of the layer. Animatable.
- [contentsCenter](contentscenter.md) — The rectangle that defines how the layer contents are scaled if the layer’s contents are resized. Animatable.
- [- display](<display().md>) — Reloads the content of this layer.
- [- drawInContext:](<draw(in_).md>) — Draws the layer’s content using the specified graphics context.
