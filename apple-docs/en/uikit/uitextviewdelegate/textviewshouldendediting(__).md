---
title: 'textViewShouldEndEditing(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextviewdelegate/textviewshouldendediting(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextviewdelegate/textviewshouldendediting(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextviewdelegate/textviewshouldendediting%28_%3A%29.json'
content_hash: 'sha256:4218b493ce004dca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextViewDelegate](../uitextviewdelegate.md)

# textViewShouldEndEditing(_:)

<sub>Instance Method</sub>

Asks the delegate whether to stop editing in the specified text view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textViewShouldEndEditing(_ textView: UITextView) -> Bool
```

## Parameters

- `textView` — The text view for which editing is about to end.

## Return Value

[true](../../swift/true.md) if editing should stop; otherwise, [false](../../swift/false.md) if the editing session should continue

## Discussion

This method is called when the text view is asked to resign the first responder status. This might occur when the user tries to change the editing focus to another control. Before the focus actually changes, however, the text view calls this method to give your delegate a chance to decide whether it should.

Normally, you would return [true](../../swift/true.md) from this method to allow the text view to resign the first responder status. You might return [false](../../swift/false.md), however, in cases where your delegate wants to validate the contents of the text view. By returning [false](../../swift/false.md), you could prevent the user from switching to another control until the text view contained a valid value.

Be aware that this method provides only a recommendation about whether editing should end. Even if you return [false](../../swift/false.md) from this method, it is possible that editing might still end. For example, this might happen when the text view is forced to resign the first responder status by being removed from its parent view or window.

Implementation of this method by the delegate is optional. If it is not present, the first responder status is resigned as if this method had returned [true](../../swift/true.md).

## See Also

### Responding to editing notifications

- [- textViewShouldBeginEditing:](<textviewshouldbeginediting(__).md>) — Asks the delegate whether to begin editing in the specified text view.
- [- textViewDidBeginEditing:](<textviewdidbeginediting(__).md>) — Tells the delegate when editing of the specified text view begins.
- [- textViewDidEndEditing:](<textviewdidendediting(__).md>) — Tells the delegate when editing of the specified text view ends.
