---
title: 'textView(_:willPresentEditMenuWith:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextviewdelegate/textview(_:willpresenteditmenuwith:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:willpresenteditmenuwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextviewdelegate/textview%28_%3Awillpresenteditmenuwith%3A%29.json'
content_hash: 'sha256:23129199a0b4e407'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextViewDelegate](../uitextviewdelegate.md)

# textView(_:willPresentEditMenuWith:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func textView(_ textView: UITextView, willPresentEditMenuWith animator: any UIEditMenuInteractionAnimating)
```

## Parameters

- `textView` — The text view displaying the menu.

- `animator` — Appearance animator. Add animations to this object to run them alongside the appearance transition.

## Discussion

Called when the text view is about to present the edit menu.

## See Also

### Customizing an edit menu

- [- textView:willDismissEditMenuWithAnimator:](<textview(__willdismisseditmenuwith_).md>)
