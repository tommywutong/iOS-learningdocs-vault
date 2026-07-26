---
title: 'textView(_:editMenuForTextIn:suggestedActions:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+（27.0 起废弃）, iPadOS 16.0+（27.0 起废弃）, Mac Catalyst 16.0+（27.0 起废弃）, tvOS 16.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uitextviewdelegate/textview(_:editmenufortextin:suggestedactions:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:editmenufortextin:suggestedactions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextviewdelegate/textview%28_%3Aeditmenufortextin%3Asuggestedactions%3A%29.json'
content_hash: 'sha256:519af2af45b76f1d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextViewDelegate](../uitextviewdelegate.md)

# textView(_:editMenuForTextIn:suggestedActions:)

<sub>Instance Method</sub>

Asks the delegate for the menu to display in the text view, based on the text range and actions the system provides.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textView(_ textView: UITextView, editMenuForTextIn range: NSRange, suggestedActions: [UIMenuElement]) -> UIMenu?
```

## Parameters

- `textView` — The text view requesting the menu.

- `range` — The character range the menu is presenting for.

- `suggestedActions` — The actions and commands the system suggests.

## Return Value

Returns a menu describing the desired menu hierarchy. Return `nil` to present the default system menu.

## Discussion

The following example returns a menu that includes an “Add Bookmark” action and also a “Highlight” action, but only if the selected text range is greater than zero.

```swift
func textView(_ textView: UITextView, editMenuForTextIn range: NSRange, suggestedActions: [UIMenuElement]) -> UIMenu? {
    var additionalActions: [UIMenuElement] = []
    if range.length > 0 {
        let highlightAction = UIAction(title: "Highlight", image: UIImage(systemName: "highlighter")) { action in
            // The highlight action.
        }
        additionalActions.append(highlightAction)
    }
    let addBookmarkAction = UIAction(title: "Add Bookmark", image: UIImage(systemName: "bookmark")) { action in
        // The bookmark action.
    }
    additionalActions.append(addBookmarkAction)
    return UIMenu(children: suggestedActions + additionalActions)
}
```
