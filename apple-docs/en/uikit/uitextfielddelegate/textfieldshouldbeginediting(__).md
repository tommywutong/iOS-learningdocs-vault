---
title: 'textFieldShouldBeginEditing(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextfielddelegate/textfieldshouldbeginediting(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfieldshouldbeginediting(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfielddelegate/textfieldshouldbeginediting%28_%3A%29.json'
content_hash: 'sha256:487cd6dd5ebdf1e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextFieldDelegate](../uitextfielddelegate.md)

# textFieldShouldBeginEditing(_:)

<sub>Instance Method</sub>

Asks the delegate whether to begin editing in the specified text field.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textFieldShouldBeginEditing(_ textField: UITextField) -> Bool
```

## Parameters

- `textField` — The text field in which editing is about to begin.

## Return Value

[true](../../swift/true.md) if editing should begin or [false](../../swift/false.md) if it should not.

## Discussion

The text field calls this method when the user performs an action that would normally initiate the editing of the text field’s text. Implement this method if you want to prevent editing from happening in some situations. For example, you could use this method to prevent the user from editing the text field’s contents more than once. Most of the time, you should return [true](../../swift/true.md) to allow editing to proceed.

If you do not implement this method, the text field acts as if this method had returned [true](../../swift/true.md).

## See Also

### Managing editing

- [- textFieldDidBeginEditing:](<textfielddidbeginediting(__).md>) — Tells the delegate when editing begins in the specified text field.
- [- textFieldShouldEndEditing:](<textfieldshouldendediting(__).md>) — Asks the delegate whether to stop editing in the specified text field.
- [- textFieldDidEndEditing:reason:](<textfielddidendediting(__reason_).md>) — Tells the delegate when editing stops for the specified text field, and the reason it stopped.
- [- textFieldDidEndEditing:](<textfielddidendediting(__).md>) — Tells the delegate when editing stops for the specified text field.
- [DidEndEditingReason](../uitextfield/didendeditingreason.md) — Constants that indicate the reason for ending editing in a text field.
