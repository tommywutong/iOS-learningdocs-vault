---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextviewportlayoutcontroller/delegate
source_url: 'https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontroller/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextviewportlayoutcontroller/delegate.json'
content_hash: 'sha256:3f86f1a096e28a4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextViewportLayoutController](../nstextviewportlayoutcontroller.md)

# delegate

<sub>Instance Property</sub>

The delegate for the text layout manager object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var delegate: (any NSTextViewportLayoutControllerDelegate)? { get set }
```

## See Also

### Responding to changes in viewport layout

- [NSTextViewportLayoutControllerDelegate](../nstextviewportlayoutcontrollerdelegate.md) — Optional methods that delegates implement to respond to viewport layout changes.
