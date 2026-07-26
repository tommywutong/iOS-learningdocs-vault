---
title: 'textField(_:willPresentEditMenuWith:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextfielddelegate/textfield(_:willpresenteditmenuwith:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfield(_:willpresenteditmenuwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfielddelegate/textfield%28_%3Awillpresenteditmenuwith%3A%29.json'
content_hash: 'sha256:2be47874891d70f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextFieldDelegate](../uitextfielddelegate.md)

# textField(_:willPresentEditMenuWith:)

<sub>Instance Method</sub>

Tells the delegate that the system is about to present an edit menu with an animator.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func textField(_ textField: UITextField, willPresentEditMenuWith animator: any UIEditMenuInteractionAnimating)
```

## Parameters

- `textField` — The text field showing the menu.

- `animator` — The appearance animator to add animations to, so that the animations will run alongside the appearance transition.

## See Also

### Customizing an edit menu

- [- textField:willDismissEditMenuWithAnimator:](<textfield(__willdismisseditmenuwith_).md>) — Tells the delegate that the system is about to dismiss an edit menu with an animator.
