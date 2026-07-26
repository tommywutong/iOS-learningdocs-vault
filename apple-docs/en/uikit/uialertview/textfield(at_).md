---
title: 'textField(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+（9.0 起废弃）, iPadOS 5.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uialertview/textfield(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uialertview/textfield(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertview/textfield%28at%3A%29.json'
content_hash: 'sha256:c7cb9b6859a1c3fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAlertView](../uialertview.md)

# textField(at:)

<sub>Instance Method</sub>

Returns the text field at the given index

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func textField(at textFieldIndex: Int) -> UITextField?
```

## Parameters

- `textFieldIndex` — The index of the text field. The text field indices start at `0`.

## Return Value

The text field specified by index `textFieldIndex`.

## Discussion

The number of text fields present in an alert is dependent on the style of the alert.

| Alert Style | Text Fields |
|---|---|
| [UIAlertViewStyleDefault](../uialertviewstyle/default.md) | No user-editable text fields. |
| [UIAlertViewStyleSecureTextInput](../uialertviewstyle/securetextinput.md) | A single text field at index `0`. |
| [UIAlertViewStylePlainTextInput](../uialertviewstyle/plaintextinput.md) | A single text field at index `0`. |
| [UIAlertViewStyleLoginAndPasswordInput](../uialertviewstyle/loginandpasswordinput.md) | The login field is at index `0`. The password field is at index `1`. |

If your application attempts to retrieve a text field with an index that is out of bounds, the alert raises an [rangeException](../../foundation/nsexceptionname/rangeexception.md).

## See Also

### Configuring buttons

- [- addButtonWithTitle:](<addbutton(withtitle_).md>) — Adds a button to the receiver with the given title. _(deprecated)_
- [numberOfButtons](numberofbuttons.md) — The number of buttons on the alert view. _(deprecated)_
- [- buttonTitleAtIndex:](<buttontitle(at_).md>) — Returns the title of the button at the given index. _(deprecated)_
- [cancelButtonIndex](cancelbuttonindex.md) — The index number of the cancel button. _(deprecated)_
- [firstOtherButtonIndex](firstotherbuttonindex.md) — The index of the first other button. _(deprecated)_
