---
title: 'textFieldShouldClear(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextfielddelegate/textfieldshouldclear(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfieldshouldclear(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfielddelegate/textfieldshouldclear%28_%3A%29.json'
content_hash: 'sha256:169ed202c59b359a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextFieldDelegate](../uitextfielddelegate.md)

# textFieldShouldClear(_:)

<sub>Instance Method</sub>

Asks the delegate whether to remove the text field’s current contents.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textFieldShouldClear(_ textField: UITextField) -> Bool
```

## Parameters

- `textField` — The text field containing the text.

## Return Value

[true](../../swift/true.md) if the text field’s contents should be cleared; otherwise, [false](../../swift/false.md).

## Discussion

The text field calls this method in response to the user pressing the built-in clear button. (This button is not shown by default but can be enabled by changing the value in the [clearButtonMode](../uitextfield/clearbuttonmode.md) property of the text field.) This method is also called when editing begins and the [clearsOnBeginEditing](../uitextfield/clearsonbeginediting.md) property of the text field is set to [true](../../swift/true.md).

If you do not implement this method, the text field clears the text as if the method had returned [true](../../swift/true.md).

## See Also

### Editing the text field’s text

- [- textField:shouldChangeCharactersInRange:replacementString:](<textfield(__shouldchangecharactersin_replacementstring_).md>) — Asks the delegate whether to change the specified text. _(deprecated)_
- [- textFieldShouldReturn:](<textfieldshouldreturn(__).md>) — Asks the delegate whether to process the pressing of the Return button for the text field.
