---
title: 'scrollRectToVisible(_:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayer/scrollrecttovisible(_:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/scrollrecttovisible(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/scrollrecttovisible%28_%3A%29.json'
content_hash: 'sha256:8f551cb203cfa466'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# scrollRectToVisible(_:)

<sub>Instance Method</sub>

Initiates a scroll in the layer’s closest ancestor scroll layer so that the specified rectangle becomes visible.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func scrollRectToVisible(_ r: CGRect)
```

## Parameters

- `r` — The rectangle to be made visible.

## Discussion

If the layer is not contained by a [CAScrollLayer](../cascrolllayer.md) object, this method does nothing.

## See Also

### Scrolling

- [visibleRect](visiblerect.md) — The visible region of the layer in its own coordinate space.
- [- scrollPoint:](<scroll(__).md>) — Initiates a scroll in the layer’s closest ancestor scroll layer so that the specified point lies at the origin of the scroll layer.
