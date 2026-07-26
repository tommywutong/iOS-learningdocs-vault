---
title: 'pointerInteraction(_:willExit:animator:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipointerinteractiondelegate/pointerinteraction(_:willexit:animator:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipointerinteractiondelegate/pointerinteraction(_:willexit:animator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointerinteractiondelegate/pointerinteraction%28_%3Awillexit%3Aanimator%3A%29.json'
content_hash: 'sha256:862feef37dc7d8d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPointerInteractionDelegate](../uipointerinteractiondelegate.md)

# pointerInteraction(_:willExit:animator:)

<sub>Instance Method</sub>

Informs the delegate when the pointer exits a given region.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func pointerInteraction(_ interaction: UIPointerInteraction, willExit region: UIPointerRegion, animator: any UIPointerInteractionAnimating)
```

## Parameters

- `interaction` — This [UIPointerInteraction](../uipointerinteraction.md).

- `region` — The [UIPointerRegion](../uipointerregion.md) that represents the entire surface of the interaction’s view.

- `animator` — The animator the framework runs when the pointer exists the region. Add animations to run them alongside the pointer’s exit animation.

## See Also

### Handling animations for pointer regions

- [- pointerInteraction:willEnterRegion:animator:](<pointerinteraction(__willenter_animator_).md>) — Informs the delegate when the pointer enters a given region.
