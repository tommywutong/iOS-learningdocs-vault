---
title: 'textView(_:textItemMenuWillEndFor:animator:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextviewdelegate/textview(_:textitemmenuwillendfor:animator:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:textitemmenuwillendfor:animator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextviewdelegate/textview%28_%3Atextitemmenuwillendfor%3Aanimator%3A%29.json'
content_hash: 'sha256:a1a85b2c35b60986'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextViewDelegate](../uitextviewdelegate.md)

# textView(_:textItemMenuWillEndFor:animator:)

<sub>Instance Method</sub>

Informs the delegate that a text item menu is about to be dismissed with the specified animator.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func textView(_ textView: UITextView, textItemMenuWillEndFor textItem: UITextItem, animator: any UIContextMenuInteractionAnimating)
```

## Parameters

- `textView` — The text view showing the menu.

- `textItem` — The text item for performing said action.

- `animator` — Dismissal animator. Add animations to this object to run them alongside the dismissal transition.

## See Also

### Interacting with text data

- [- textView:menuConfigurationForTextItem:defaultMenu:](<textview(__menuconfigurationfor_defaultmenu_).md>) — Asks the delegate for the menu configuration to be performed when interacting with a text item.
- [- textView:primaryActionForTextItem:defaultAction:](<textview(__primaryactionfor_defaultaction_).md>) — Asks the delegate for the action to be performed when interacting with a text item. If a nil action is provided, the text view will request a menu to be presented on primary action if possible.
- [- textView:textItemMenuWillDisplayForTextItem:animator:](<textview(__textitemmenuwilldisplayfor_animator_).md>) — Informs the delegate that a text item menu is about to be presented with the specified animator.
