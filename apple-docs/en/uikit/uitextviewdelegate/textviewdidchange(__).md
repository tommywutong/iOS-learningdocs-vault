---
title: 'textViewDidChange(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextviewdelegate/textviewdidchange(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextviewdelegate/textviewdidchange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextviewdelegate/textviewdidchange%28_%3A%29.json'
content_hash: 'sha256:6d1cf88b597cd859'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextViewDelegate](../uitextviewdelegate.md)

# textViewDidChange(_:)

<sub>Instance Method</sub>

Tells the delegate when the user changes the text or attributes in the specified text view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textViewDidChange(_ textView: UITextView)
```

## Parameters

- `textView` — The text view containing the changes.

## Discussion

The text view calls this method in response to user-initiated changes to the text. This method is not called in response to programmatically initiated changes.

Implementation of this method is optional.

## See Also

### Responding to text changes

- [- textView:shouldChangeTextInRange:replacementText:](<textview(__shouldchangetextin_replacementtext_).md>) — Asks the delegate whether to replace the specified text in the text view. _(deprecated)_
