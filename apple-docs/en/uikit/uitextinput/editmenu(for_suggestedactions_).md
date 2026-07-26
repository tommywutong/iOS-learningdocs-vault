---
title: 'editMenu(for:suggestedActions:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/editmenu(for:suggestedactions:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/editmenu(for:suggestedactions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/editmenu%28for%3Asuggestedactions%3A%29.json'
content_hash: 'sha256:ba58a1e82151f3a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# editMenu(for:suggestedActions:)

<sub>Instance Method</sub>

Asks for the menu to display for the given text range and actions the system provides.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func editMenu(for textRange: UITextRange, suggestedActions: [UIMenuElement]) -> UIMenu?
```

## Parameters

- `textRange` — The text range the menu is presenting for.

- `suggestedActions` — The actions and commands the system suggests.

## Return Value

Returns a menu describing the desired menu hierarchy. Return `nil` to present the default system menu.

## Discussion

The following example returns a menu with additional actions in a submenu.

```swift
func editMenu(for textRange: UITextRange, suggestedActions: [UIMenuElement]) -> UIMenu? {
    let indentationMenu = UIMenu(title: "Indentation", image: UIImage(systemName: "list.bullet.indent"), children: [
        UIAction(title: "Increase", image: UIImage(systemName: "increase.indent")) { (action) in
            // Increase indentation action.
        },
        UIAction(title: "Decrease", image: UIImage(systemName: "decrease.indent")) { (action) in
            // Decrease indentation action.
        }
    ])

    var actions = suggestedActions
    actions.append(indentationMenu)
    return UIMenu(children: actions)
}
```

## See Also

### Managing the edit menu

- [- willPresentEditMenuWithAnimator:](<willpresenteditmenu(animator_).md>) — Tells the object when the system is about to present an edit menu with an animator.
- [- willDismissEditMenuWithAnimator:](<willdismisseditmenu(animator_).md>) — Tells the object when the system is about to dismiss an edit menu with an animator.
