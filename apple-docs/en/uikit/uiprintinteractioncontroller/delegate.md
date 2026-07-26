---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintinteractioncontroller/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinteractioncontroller/delegate.json'
content_hash: 'sha256:82c53fa158397714'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInteractionController](../uiprintinteractioncontroller.md)

# delegate

<sub>Instance Property</sub>

The delegate of the print-interaction controller.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var delegate: (any UIPrintInteractionControllerDelegate)? { get set }
```

## Discussion

The delegate must adopt the [UIPrintInteractionControllerDelegate](../uiprintinteractioncontrollerdelegate.md) protocol and implement one or more of its methods. It is not retained.

## See Also

### Assigning the delegate

- [UIPrintInteractionControllerDelegate](../uiprintinteractioncontrollerdelegate.md) — An optional set of methods that the delegate of the shared print-interaction controller implements.
