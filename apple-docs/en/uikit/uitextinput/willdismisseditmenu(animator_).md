---
title: 'willDismissEditMenu(animator:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/willdismisseditmenu(animator:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/willdismisseditmenu(animator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/willdismisseditmenu%28animator%3A%29.json'
content_hash: 'sha256:90cd87b20e01a2f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# willDismissEditMenu(animator:)

<sub>Instance Method</sub>

Tells the object when the system is about to dismiss an edit menu with an animator.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func willDismissEditMenu(animator: any UIEditMenuInteractionAnimating)
```

## Parameters

- `animator` — The dismissal animator to add animations to, so that the animations will run alongside the dismissal transition.

## See Also

### Managing the edit menu

- [- editMenuForTextRange:suggestedActions:](<editmenu(for_suggestedactions_).md>) — Asks for the menu to display for the given text range and actions the system provides.
- [- willPresentEditMenuWithAnimator:](<willpresenteditmenu(animator_).md>) — Tells the object when the system is about to present an edit menu with an animator.
