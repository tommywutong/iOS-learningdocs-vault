---
title: 'textFieldDidEndEditing(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextfielddelegate/textfielddidendediting(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfielddidendediting(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfielddelegate/textfielddidendediting%28_%3A%29.json'
content_hash: 'sha256:3a3e3f250bf18929'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextFieldDelegate](../uitextfielddelegate.md)

# textFieldDidEndEditing(_:)

<sub>Instance Method</sub>

Tells the delegate when editing stops for the specified text field.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textFieldDidEndEditing(_ textField: UITextField)
```

## Parameters

- `textField` — The text field for which editing ended.

## Discussion

This method is called after the text field resigns its first responder status. You can use this method to update your delegate’s state information. For example, you might use this method to hide overlay views that should be visible only while editing.

Implementation of this method by the delegate is optional. If your delegate also implements the [- textFieldDidEndEditing:reason:](<textfielddidendediting(__reason_).md>) method, UIKit calls that method in preference to this one.

## See Also

### Managing editing

- [- textFieldShouldBeginEditing:](<textfieldshouldbeginediting(__).md>) — Asks the delegate whether to begin editing in the specified text field.
- [- textFieldDidBeginEditing:](<textfielddidbeginediting(__).md>) — Tells the delegate when editing begins in the specified text field.
- [- textFieldShouldEndEditing:](<textfieldshouldendediting(__).md>) — Asks the delegate whether to stop editing in the specified text field.
- [- textFieldDidEndEditing:reason:](<textfielddidendediting(__reason_).md>) — Tells the delegate when editing stops for the specified text field, and the reason it stopped.
- [DidEndEditingReason](../uitextfield/didendeditingreason.md) — Constants that indicate the reason for ending editing in a text field.
