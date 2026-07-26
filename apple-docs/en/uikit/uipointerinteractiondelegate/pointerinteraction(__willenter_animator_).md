---
title: 'pointerInteraction(_:willEnter:animator:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipointerinteractiondelegate/pointerinteraction(_:willenter:animator:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipointerinteractiondelegate/pointerinteraction(_:willenter:animator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointerinteractiondelegate/pointerinteraction%28_%3Awillenter%3Aanimator%3A%29.json'
content_hash: 'sha256:f0f68af65d751111'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPointerInteractionDelegate](../uipointerinteractiondelegate.md)

# pointerInteraction(_:willEnter:animator:)

<sub>Instance Method</sub>

Informs the delegate when the pointer enters a given region.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func pointerInteraction(_ interaction: UIPointerInteraction, willEnter region: UIPointerRegion, animator: any UIPointerInteractionAnimating)
```

## Parameters

- `interaction` — This [UIPointerInteraction](../uipointerinteraction.md).

- `region` — The [UIPointerRegion](../uipointerregion.md) that represents the entire surface of the interaction’s view.

- `animator` — The animator the framework runs when the pointer enters the region. Add animations to run them alongside the pointer’s entrance animation.

## See Also

### Handling animations for pointer regions

- [- pointerInteraction:willExitRegion:animator:](<pointerinteraction(__willexit_animator_).md>) — Informs the delegate when the pointer exits a given region.
