---
title: UIBarMinimizationRestorationBehavior.atScrollEdge
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uibarminimizationrestorationbehavior/atscrolledge
source_url: 'https://developer.apple.com/documentation/uikit/uibarminimizationrestorationbehavior/atscrolledge'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarminimizationrestorationbehavior/atscrolledge.json'
content_hash: 'sha256:0a0e9bcb0149d77b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarMinimizationRestorationBehavior](../uibarminimizationrestorationbehavior.md)

# UIBarMinimizationRestorationBehavior.atScrollEdge

<sub>Case</sub>

The bar restores only when the observed scroll view’s content reaches the scroll edge.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
case atScrollEdge
```

## Discussion

Currently this is only honored alongside `UIBarMinimizationBehaviorOnScrollDown`. With other minimization behaviors, the system falls back to [UIBarMinimizationRestorationBehaviorAutomatic](automatic.md).

## See Also

### Restoring the bar

- [UIBarMinimizationRestorationBehaviorAutomatic](automatic.md) — The system determines the restoration behavior. _(beta)_
