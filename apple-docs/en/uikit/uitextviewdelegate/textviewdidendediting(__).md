---
title: 'textViewDidEndEditing(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextviewdelegate/textviewdidendediting(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextviewdelegate/textviewdidendediting(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextviewdelegate/textviewdidendediting%28_%3A%29.json'
content_hash: 'sha256:b5b63c851c2ed2c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextViewDelegate](../uitextviewdelegate.md)

# textViewDidEndEditing(_:)

<sub>Instance Method</sub>

Tells the delegate when editing of the specified text view ends.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textViewDidEndEditing(_ textView: UITextView)
```

## Parameters

- `textView` — The text view in which editing ended.

## Discussion

Implementation of this method is optional. A text view sends this message to its delegate after it closes out any pending edits and resigns its first responder status. You can use this method to tear down any data structures or change any state information that you set when editing began.

## See Also

### Responding to editing notifications

- [- textViewShouldBeginEditing:](<textviewshouldbeginediting(__).md>) — Asks the delegate whether to begin editing in the specified text view.
- [- textViewDidBeginEditing:](<textviewdidbeginediting(__).md>) — Tells the delegate when editing of the specified text view begins.
- [- textViewShouldEndEditing:](<textviewshouldendediting(__).md>) — Asks the delegate whether to stop editing in the specified text view.
