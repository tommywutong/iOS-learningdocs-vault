---
title: unobscuredContentRect
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, tvOS 26.4+, visionOS 26.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinput/unobscuredcontentrect
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/unobscuredcontentrect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/unobscuredcontentrect.json'
content_hash: 'sha256:24e55e0fa3e38e58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# unobscuredContentRect

<sub>Instance Property</sub>

The visible content region, excluding parts covered by view-specific UI.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional var unobscuredContentRect: CGRect { get }
```

## Return Value

The visible content rectangle, or CGRectNull if there is no specific constraint.

## Discussion

Account for scroll position, insets, and any custom UI elements (toolbars, accessories, etc.) that obscure content. The system automatically accounts for keyboard obscuring when editing.

The rectangle is in the `textInputView` coordinate space.
