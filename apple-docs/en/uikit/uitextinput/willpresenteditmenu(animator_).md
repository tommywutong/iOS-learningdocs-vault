---
title: 'willPresentEditMenu(animator:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/willpresenteditmenu(animator:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/willpresenteditmenu(animator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/willpresenteditmenu%28animator%3A%29.json'
content_hash: 'sha256:24fbabf62fe520b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# willPresentEditMenu(animator:)

<sub>Instance Method</sub>

Tells the object when the system is about to present an edit menu with an animator.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func willPresentEditMenu(animator: any UIEditMenuInteractionAnimating)
```

## Parameters

- `animator` — The appearance animator to add animations to, so that the animations will run alongside the appearance transition.

## See Also

### Managing the edit menu

- [- editMenuForTextRange:suggestedActions:](<editmenu(for_suggestedactions_).md>) — Asks for the menu to display for the given text range and actions the system provides.
- [- willDismissEditMenuWithAnimator:](<willdismisseditmenu(animator_).md>) — Tells the object when the system is about to dismiss an edit menu with an animator.
