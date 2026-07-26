---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.1+, iPadOS 12.1+, Mac Catalyst 13.1+, visionOS 26.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipencilinteraction/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uipencilinteraction/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipencilinteraction/delegate.json'
content_hash: 'sha256:4e982989525fcbd6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPencilInteraction](../uipencilinteraction.md)

# delegate

<sub>Instance Property</sub>

The object that handles the double-tap or squeeze interactions a person makes on Apple Pencil.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var delegate: (any UIPencilInteractionDelegate)? { get set }
```

## See Also

### Handling interactions

- [UIPencilInteractionDelegate](../uipencilinteractiondelegate.md) — The interface an object implements to handle double taps or squeezes a person makes on Apple Pencil.
