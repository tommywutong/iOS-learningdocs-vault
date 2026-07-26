---
title: 'textField(_:shouldChangeCharactersIn:replacementString:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uitextfielddelegate/textfield(_:shouldchangecharactersin:replacementstring:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfield(_:shouldchangecharactersin:replacementstring:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfielddelegate/textfield%28_%3Ashouldchangecharactersin%3Areplacementstring%3A%29.json'
content_hash: 'sha256:70131c1a16d43db6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextFieldDelegate](../uitextfielddelegate.md)

# textField(_:shouldChangeCharactersIn:replacementString:)

<sub>Instance Method</sub>

Asks the delegate whether to change the specified text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool
```

## Parameters

- `textField` — The text field containing the text.

- `range` — The range of characters to be replaced.

- `string` — The replacement string for the specified range. During typing, this parameter normally contains only the single new character that was typed, but it may contain more characters if the user is pasting text. When the user deletes one or more characters, the replacement string is empty.

## Return Value

[true](../../swift/true.md) if the specified text range should be replaced; otherwise, [false](../../swift/false.md) to keep the old text.

## Discussion

The text field calls this method whenever user actions cause its text to change. Use this method to validate text as it is typed by the user. For example, you could use this method to prevent the user from entering anything but numerical values.

## See Also

### Editing the text field’s text

- [- textFieldShouldClear:](<textfieldshouldclear(__).md>) — Asks the delegate whether to remove the text field’s current contents.
- [- textFieldShouldReturn:](<textfieldshouldreturn(__).md>) — Asks the delegate whether to process the pressing of the Return button for the text field.
