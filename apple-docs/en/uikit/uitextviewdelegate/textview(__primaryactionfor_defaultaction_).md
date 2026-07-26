---
title: 'textView(_:primaryActionFor:defaultAction:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextviewdelegate/textview(_:primaryactionfor:defaultaction:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:primaryactionfor:defaultaction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextviewdelegate/textview%28_%3Aprimaryactionfor%3Adefaultaction%3A%29.json'
content_hash: 'sha256:b10508ffd9e39d97'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextViewDelegate](../uitextviewdelegate.md)

# textView(_:primaryActionFor:defaultAction:)

<sub>Instance Method</sub>

Asks the delegate for the action to be performed when interacting with a text item. If a nil action is provided, the text view will request a menu to be presented on primary action if possible.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func textView(_ textView: UITextView, primaryActionFor textItem: UITextItem, defaultAction: UIAction) -> UIAction?
```

## Parameters

- `textView` — The text view requesting the primary action.

- `textItem` — The text item for performing said action.

- `defaultAction` — The default action for the text item. Return this to perform the default action.

## Return Value

Return a UIAction to be performed when the text item is interacted with. Return @c nil to prevent the action from being performed.

## See Also

### Interacting with text data

- [- textView:menuConfigurationForTextItem:defaultMenu:](<textview(__menuconfigurationfor_defaultmenu_).md>) — Asks the delegate for the menu configuration to be performed when interacting with a text item.
- [- textView:textItemMenuWillDisplayForTextItem:animator:](<textview(__textitemmenuwilldisplayfor_animator_).md>) — Informs the delegate that a text item menu is about to be presented with the specified animator.
- [- textView:textItemMenuWillEndForTextItem:animator:](<textview(__textitemmenuwillendfor_animator_).md>) — Informs the delegate that a text item menu is about to be dismissed with the specified animator.
