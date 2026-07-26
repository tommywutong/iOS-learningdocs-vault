---
title: 'scroll(_:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayer/scroll(_:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/scroll(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/scroll%28_%3A%29.json'
content_hash: 'sha256:7b55880f16e952de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# scroll(_:)

<sub>Instance Method</sub>

Initiates a scroll in the layer’s closest ancestor scroll layer so that the specified point lies at the origin of the scroll layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func scroll(_ p: CGPoint)
```

## Parameters

- `p` — The point in the current layer that should be scrolled into position.

## Discussion

If the layer is not contained by a [CAScrollLayer](../cascrolllayer.md) object, this method does nothing.

## See Also

### Scrolling

- [visibleRect](visiblerect.md) — The visible region of the layer in its own coordinate space.
- [- scrollRectToVisible:](<scrollrecttovisible(__).md>) — Initiates a scroll in the layer’s closest ancestor scroll layer so that the specified rectangle becomes visible.
