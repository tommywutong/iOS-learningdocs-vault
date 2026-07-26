---
title: 'textFieldShouldEndEditing(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextfielddelegate/textfieldshouldendediting(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfieldshouldendediting(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfielddelegate/textfieldshouldendediting%28_%3A%29.json'
content_hash: 'sha256:96cf5d97a5e97339'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextFieldDelegate](../uitextfielddelegate.md)

# textFieldShouldEndEditing(_:)

<sub>Instance Method</sub>

Asks the delegate whether to stop editing in the specified text field.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textFieldShouldEndEditing(_ textField: UITextField) -> Bool
```

## Parameters

- `textField` — The text field in which editing is about to end.

## Return Value

[true](../../swift/true.md) if editing should stop or [false](../../swift/false.md) if it should continue.

## Discussion

The text field calls this method when it is asked to resign the first responder status. This can happen when the user selects another control or when you call the text field’s [- resignFirstResponder](<../uiresponder/resignfirstresponder().md>) method. Before the focus change occurs, however, the text field calls this method and gives you a chance to prevent the change from happening.

Normally, you would return [true](../../swift/true.md) from this method to allow the text field to resign the first responder status. You might return [false](../../swift/false.md), however, in cases where your delegate detects invalid contents in the text field. Returning [false](../../swift/false.md) prevents the user from switching to another control until the text field contains a valid value.

> [!note] Note
> If you use this method to validate the contents of the text field, you might also want to use an overlay view to provide feedback to that effect. For example, you might display a small icon indicating the text is invalid. For more information about adding overlays to text fields, see the methods of [UITextField](../uitextfield.md).

Be aware that this method provides only a recommendation about whether editing should end. Even if you return [false](../../swift/false.md), UIKit might still force an end to editing. For example, text fields always resign the first responder status when they are removed from their parent view or window.

Implementation of this method by the delegate is optional. If you do not implement this method, the text field resigns the first responder status as if this method had returned [true](../../swift/true.md).

## See Also

### Managing editing

- [- textFieldShouldBeginEditing:](<textfieldshouldbeginediting(__).md>) — Asks the delegate whether to begin editing in the specified text field.
- [- textFieldDidBeginEditing:](<textfielddidbeginediting(__).md>) — Tells the delegate when editing begins in the specified text field.
- [- textFieldDidEndEditing:reason:](<textfielddidendediting(__reason_).md>) — Tells the delegate when editing stops for the specified text field, and the reason it stopped.
- [- textFieldDidEndEditing:](<textfielddidendediting(__).md>) — Tells the delegate when editing stops for the specified text field.
- [DidEndEditingReason](../uitextfield/didendeditingreason.md) — Constants that indicate the reason for ending editing in a text field.
