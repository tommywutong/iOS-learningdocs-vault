---
title: 'pointerInteraction(_:regionFor:defaultRegion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipointerinteractiondelegate/pointerinteraction(_:regionfor:defaultregion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipointerinteractiondelegate/pointerinteraction(_:regionfor:defaultregion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointerinteractiondelegate/pointerinteraction%28_%3Aregionfor%3Adefaultregion%3A%29.json'
content_hash: 'sha256:6a99cf1dec6b0302'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPointerInteractionDelegate](../uipointerinteractiondelegate.md)

# pointerInteraction(_:regionFor:defaultRegion:)

<sub>Instance Method</sub>

Asks the delegate for a region as the pointer moves within the interaction’s view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func pointerInteraction(_ interaction: UIPointerInteraction, regionFor request: UIPointerRegionRequest, defaultRegion: UIPointerRegion) -> UIPointerRegion?
```

## Parameters

- `interaction` — This [UIPointerInteraction](../uipointerinteraction.md).

- `request` — The [UIPointerRegionRequest](../uipointerregionrequest.md) that describes the pointer’s location in the interaction’s view.

- `defaultRegion` — The [UIPointerRegion](../uipointerregion.md) that represents the entire surface of the interaction’s view.

## Return Value

A `UIPointerRegion` in which to apply a pointer style. Return `nil` to indicate that this interaction typically doesn’t customize the pointer for the current location.

## See Also

### Defining pointer styles for regions

- [- pointerInteraction:styleForRegion:](<pointerinteraction(__stylefor_).md>) — Asks the delegate for a pointer style after an interaction receives a new region.
