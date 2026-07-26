---
title: visibleRect
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/visiblerect
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/visiblerect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/visiblerect.json'
content_hash: 'sha256:2a47fd78e27d26c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# visibleRect

<sub>Instance Property</sub>

The visible region of the layer in its own coordinate space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var visibleRect: CGRect { get }
```

## Discussion

The visible region is the area not clipped by the containing scroll layer.

## See Also

### Scrolling

- [- scrollPoint:](<scroll(__).md>) — Initiates a scroll in the layer’s closest ancestor scroll layer so that the specified point lies at the origin of the scroll layer.
- [- scrollRectToVisible:](<scrollrecttovisible(__).md>) — Initiates a scroll in the layer’s closest ancestor scroll layer so that the specified rectangle becomes visible.
