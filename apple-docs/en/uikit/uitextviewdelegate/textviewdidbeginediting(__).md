---
title: 'textViewDidBeginEditing(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextviewdelegate/textviewdidbeginediting(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextviewdelegate/textviewdidbeginediting(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextviewdelegate/textviewdidbeginediting%28_%3A%29.json'
content_hash: 'sha256:e03848f9285b7df7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextViewDelegate](../uitextviewdelegate.md)

# textViewDidBeginEditing(_:)

<sub>Instance Method</sub>

Tells the delegate when editing of the specified text view begins.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textViewDidBeginEditing(_ textView: UITextView)
```

## Parameters

- `textView` — The text view in which editing began.

## Discussion

Implementation of this method is optional. A text view sends this message to its delegate immediately after the user initiates editing in a text view and before any changes are actually made. You can use this method to set up any editing-related data structures and generally prepare your delegate to receive future editing messages.

## See Also

### Responding to editing notifications

- [- textViewShouldBeginEditing:](<textviewshouldbeginediting(__).md>) — Asks the delegate whether to begin editing in the specified text view.
- [- textViewShouldEndEditing:](<textviewshouldendediting(__).md>) — Asks the delegate whether to stop editing in the specified text view.
- [- textViewDidEndEditing:](<textviewdidendediting(__).md>) — Tells the delegate when editing of the specified text view ends.
