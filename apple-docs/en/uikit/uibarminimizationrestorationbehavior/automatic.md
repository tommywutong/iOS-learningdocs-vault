---
title: UIBarMinimizationRestorationBehavior.automatic
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uibarminimizationrestorationbehavior/automatic
source_url: 'https://developer.apple.com/documentation/uikit/uibarminimizationrestorationbehavior/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarminimizationrestorationbehavior/automatic.json'
content_hash: 'sha256:9bb1c729c40d10d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarMinimizationRestorationBehavior](../uibarminimizationrestorationbehavior.md)

# UIBarMinimizationRestorationBehavior.automatic

<sub>Case</sub>

The system determines the restoration behavior.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case automatic
```

## Discussion

By default, the bar restores when the user reverses scroll direction. The system selects [UIBarMinimizationRestorationBehaviorAtScrollEdge](atscrolledge.md) automatically for navigation items whose `preferredSearchBarPlacement` is `.integratedCentered`.

## See Also

### Restoring the bar

- [UIBarMinimizationRestorationBehaviorAtScrollEdge](atscrolledge.md) — The bar restores only when the observed scroll view’s content reaches the scroll edge. _(beta)_
