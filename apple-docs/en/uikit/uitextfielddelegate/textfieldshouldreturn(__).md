---
title: 'textFieldShouldReturn(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextfielddelegate/textfieldshouldreturn(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfieldshouldreturn(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfielddelegate/textfieldshouldreturn%28_%3A%29.json'
content_hash: 'sha256:54bc48ba93cd6685'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextFieldDelegate](../uitextfielddelegate.md)

# textFieldShouldReturn(_:)

<sub>Instance Method</sub>

Asks the delegate whether to process the pressing of the Return button for the text field.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textFieldShouldReturn(_ textField: UITextField) -> Bool
```

## Parameters

- `textField` — The text field whose return button was pressed.

## Return Value

[true](../../swift/true.md) if the text field should implement its default behavior for the return button; otherwise, [false](../../swift/false.md).

## Discussion

The text field calls this method whenever the user taps the return button. You can use this method to implement any custom behavior when the button is tapped. For example, if you want to dismiss the keyboard when the user taps the return button, your implementation can call the [- resignFirstResponder](<../uiresponder/resignfirstresponder().md>) method.

## See Also

### Editing the text field’s text

- [- textField:shouldChangeCharactersInRange:replacementString:](<textfield(__shouldchangecharactersin_replacementstring_).md>) — Asks the delegate whether to change the specified text. _(deprecated)_
- [- textFieldShouldClear:](<textfieldshouldclear(__).md>) — Asks the delegate whether to remove the text field’s current contents.
