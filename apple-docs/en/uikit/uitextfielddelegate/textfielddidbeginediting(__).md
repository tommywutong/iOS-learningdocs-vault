---
title: 'textFieldDidBeginEditing(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextfielddelegate/textfielddidbeginediting(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfielddidbeginediting(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfielddelegate/textfielddidbeginediting%28_%3A%29.json'
content_hash: 'sha256:a61386cbfb800f8c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextFieldDelegate](../uitextfielddelegate.md)

# textFieldDidBeginEditing(_:)

<sub>Instance Method</sub>

Tells the delegate when editing begins in the specified text field.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textFieldDidBeginEditing(_ textField: UITextField)
```

## Parameters

- `textField` — The text field in which an editing session began.

## Discussion

This method notifies the delegate that the specified text field just became the first responder. Use this method to update state information or perform other tasks. For example, you might use this method to show overlay views that are visible only while editing.

Implementation of this method by the delegate is optional.

## See Also

### Managing editing

- [- textFieldShouldBeginEditing:](<textfieldshouldbeginediting(__).md>) — Asks the delegate whether to begin editing in the specified text field.
- [- textFieldShouldEndEditing:](<textfieldshouldendediting(__).md>) — Asks the delegate whether to stop editing in the specified text field.
- [- textFieldDidEndEditing:reason:](<textfielddidendediting(__reason_).md>) — Tells the delegate when editing stops for the specified text field, and the reason it stopped.
- [- textFieldDidEndEditing:](<textfielddidendediting(__).md>) — Tells the delegate when editing stops for the specified text field.
- [DidEndEditingReason](../uitextfield/didendeditingreason.md) — Constants that indicate the reason for ending editing in a text field.
