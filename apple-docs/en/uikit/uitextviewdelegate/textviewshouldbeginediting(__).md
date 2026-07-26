---
title: 'textViewShouldBeginEditing(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextviewdelegate/textviewshouldbeginediting(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextviewdelegate/textviewshouldbeginediting(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextviewdelegate/textviewshouldbeginediting%28_%3A%29.json'
content_hash: 'sha256:311dae1be80fd99e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextViewDelegate](../uitextviewdelegate.md)

# textViewShouldBeginEditing(_:)

<sub>Instance Method</sub>

Asks the delegate whether to begin editing in the specified text view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textViewShouldBeginEditing(_ textView: UITextView) -> Bool
```

## Parameters

- `textView` — The text view for which editing is about to begin.

## Return Value

[true](../../swift/true.md) if an editing session should be initiated; otherwise, [false](../../swift/false.md) to disallow editing.

## Discussion

When the user performs an action that would normally initiate an editing session, the text view calls this method first to see if editing should actually proceed. In most circumstances, you would simply return [true](../../swift/true.md) from this method to allow editing to proceed.

Implementation of this method by the delegate is optional. If it is not present, editing proceeds as if this method had returned [true](../../swift/true.md).

## See Also

### Responding to editing notifications

- [- textViewDidBeginEditing:](<textviewdidbeginediting(__).md>) — Tells the delegate when editing of the specified text view begins.
- [- textViewShouldEndEditing:](<textviewshouldendediting(__).md>) — Asks the delegate whether to stop editing in the specified text view.
- [- textViewDidEndEditing:](<textviewdidendediting(__).md>) — Tells the delegate when editing of the specified text view ends.
