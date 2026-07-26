---
title: 'textField(_:editMenuForCharactersInRanges:suggestedActions:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextfielddelegate/textfield(_:editmenuforcharactersinranges:suggestedactions:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfield(_:editmenuforcharactersinranges:suggestedactions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfielddelegate/textfield%28_%3Aeditmenuforcharactersinranges%3Asuggestedactions%3A%29.json'
content_hash: 'sha256:8924aef2b7c3404e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextFieldDelegate](../uitextfielddelegate.md)

# textField(_:editMenuForCharactersInRanges:suggestedActions:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textField(_ textField: UITextField, editMenuForCharactersInRanges ranges: [NSValue], suggestedActions: [UIMenuElement]) -> UIMenu?
```

## Parameters

- `textField` — The text field requesting the menu.

- `ranges` — The text ranges for which the menu is presented for.

- `suggestedActions` — The actions and commands that the system suggests.

## Return Value

Return a UIMenu describing the desired menu hierarchy. Return @c nil to present the default system menu.

## Discussion

Asks the delegate for the menu to be shown for the specified `ranges`.
