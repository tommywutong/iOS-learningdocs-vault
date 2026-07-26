---
title: 'textField(_:editMenuForCharactersIn:suggestedActions:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+（27.0 起废弃）, iPadOS 16.0+（27.0 起废弃）, Mac Catalyst 16.0+（27.0 起废弃）, tvOS 16.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uitextfielddelegate/textfield(_:editmenuforcharactersin:suggestedactions:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfield(_:editmenuforcharactersin:suggestedactions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfielddelegate/textfield%28_%3Aeditmenuforcharactersin%3Asuggestedactions%3A%29.json'
content_hash: 'sha256:1833787192a9fd65'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextFieldDelegate](../uitextfielddelegate.md)

# textField(_:editMenuForCharactersIn:suggestedActions:)

<sub>Instance Method</sub>

Asks the delegate for the menu to display in the text field, based on the text range and actions the system provides.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textField(_ textField: UITextField, editMenuForCharactersIn range: NSRange, suggestedActions: [UIMenuElement]) -> UIMenu?
```

## Parameters

- `textField` — The text field requesting the menu.

- `range` — The character range the menu is presenting for.

- `suggestedActions` — The actions and commands the system suggests.

## Return Value

Returns a menu describing the desired menu hierarchy. Return `nil` to present the default system menu.

## Discussion

The following example returns a menu that includes a “Show in Large Type” action.

```swift
func textField(_ textField: UITextField, editMenuForCharactersIn range: NSRange, suggestedActions: [UIMenuElement]) -> UIMenu? {
    let showLargeAction = UIAction(title: "Show in Large Type", image: UIImage(systemName: "a.magnify")) { action in
            // Include "Show in Large Type" action.
    }

    var actions = suggestedActions
    actions.append(showLargeAction)
    return UIMenu(children: actions)
}
```
