---
title: 'textFieldDidEndEditing(_:reason:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextfielddelegate/textfielddidendediting(_:reason:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfielddidendediting(_:reason:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfielddelegate/textfielddidendediting%28_%3Areason%3A%29.json'
content_hash: 'sha256:ed5a181964043078'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextFieldDelegate](../uitextfielddelegate.md)

# textFieldDidEndEditing(_:reason:)

<sub>Instance Method</sub>

Tells the delegate when editing stops for the specified text field, and the reason it stopped.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textFieldDidEndEditing(_ textField: UITextField, reason: UITextField.DidEndEditingReason)
```

## Parameters

- `textField` — The text field for which editing ended.

- `reason` — The reason why editing ended. Use this field to determine whether to incorporate the text editing changes or abandon them.

## Discussion

This method is called after the text field resigns its first responder status. You can use this method to update your delegate’s state information. For example, you might use this method to hide overlay views that should be visible only while editing.

Implementation of this method by the delegate is optional. UIKit calls this method in preference to the [- textFieldDidEndEditing:](<textfielddidendediting(__).md>) method.

## See Also

### Managing editing

- [- textFieldShouldBeginEditing:](<textfieldshouldbeginediting(__).md>) — Asks the delegate whether to begin editing in the specified text field.
- [- textFieldDidBeginEditing:](<textfielddidbeginediting(__).md>) — Tells the delegate when editing begins in the specified text field.
- [- textFieldShouldEndEditing:](<textfieldshouldendediting(__).md>) — Asks the delegate whether to stop editing in the specified text field.
- [- textFieldDidEndEditing:](<textfielddidendediting(__).md>) — Tells the delegate when editing stops for the specified text field.
- [DidEndEditingReason](../uitextfield/didendeditingreason.md) — Constants that indicate the reason for ending editing in a text field.
