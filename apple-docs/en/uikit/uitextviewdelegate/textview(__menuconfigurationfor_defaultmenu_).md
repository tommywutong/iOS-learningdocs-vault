---
title: 'textView(_:menuConfigurationFor:defaultMenu:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextviewdelegate/textview(_:menuconfigurationfor:defaultmenu:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:menuconfigurationfor:defaultmenu:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextviewdelegate/textview%28_%3Amenuconfigurationfor%3Adefaultmenu%3A%29.json'
content_hash: 'sha256:84fe747a1220327e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextViewDelegate](../uitextviewdelegate.md)

# textView(_:menuConfigurationFor:defaultMenu:)

<sub>Instance Method</sub>

Asks the delegate for the menu configuration to be performed when interacting with a text item.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func textView(_ textView: UITextView, menuConfigurationFor textItem: UITextItem, defaultMenu: UIMenu) -> UITextItem.MenuConfiguration?
```

## Parameters

- `textView` — The text view requesting the menu.

- `textItem` — The text item for performing said action.

- `defaultMenu` — The default menu for the specified text item.

## Return Value

Return a menu configuration to be presented when the text item is interacted with. Return @c nil to prevent the menu from being presented.

## See Also

### Interacting with text data

- [- textView:primaryActionForTextItem:defaultAction:](<textview(__primaryactionfor_defaultaction_).md>) — Asks the delegate for the action to be performed when interacting with a text item. If a nil action is provided, the text view will request a menu to be presented on primary action if possible.
- [- textView:textItemMenuWillDisplayForTextItem:animator:](<textview(__textitemmenuwilldisplayfor_animator_).md>) — Informs the delegate that a text item menu is about to be presented with the specified animator.
- [- textView:textItemMenuWillEndForTextItem:animator:](<textview(__textitemmenuwillendfor_animator_).md>) — Informs the delegate that a text item menu is about to be dismissed with the specified animator.
