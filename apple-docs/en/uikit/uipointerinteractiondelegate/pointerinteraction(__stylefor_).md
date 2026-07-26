---
title: 'pointerInteraction(_:styleFor:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipointerinteractiondelegate/pointerinteraction(_:stylefor:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipointerinteractiondelegate/pointerinteraction(_:stylefor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointerinteractiondelegate/pointerinteraction%28_%3Astylefor%3A%29.json'
content_hash: 'sha256:52f8b3c8e7f5219c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPointerInteractionDelegate](../uipointerinteractiondelegate.md)

# pointerInteraction(_:styleFor:)

<sub>Instance Method</sub>

Asks the delegate for a pointer style after an interaction receives a new region.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func pointerInteraction(_ interaction: UIPointerInteraction, styleFor region: UIPointerRegion) -> UIPointerStyle?
```

## Parameters

- `interaction` — This [UIPointerInteraction](../uipointerinteraction.md).

- `region` — The [UIPointerRegion](../uipointerregion.md) that represents the entire surface of the interaction’s view.

## Return Value

A `UIPointerStyle` describing the desired hover effect or pointer appearance for the given `UIPointerRegion`.

## See Also

### Defining pointer styles for regions

- [- pointerInteraction:regionForRequest:defaultRegion:](<pointerinteraction(__regionfor_defaultregion_).md>) — Asks the delegate for a region as the pointer moves within the interaction’s view.
