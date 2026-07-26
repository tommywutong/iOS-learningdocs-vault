---
title: 'textViewWritingToolsWillBegin(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.4+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextviewdelegate/textviewwritingtoolswillbegin(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextviewdelegate/textviewwritingtoolswillbegin(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextviewdelegate/textviewwritingtoolswillbegin%28_%3A%29.json'
content_hash: 'sha256:12bb4decb5481858'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextViewDelegate](../uitextviewdelegate.md)

# textViewWritingToolsWillBegin(_:)

<sub>Instance Method</sub>

Tells the delegate that an interaction with the writing tools interface is about to begin.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func textViewWritingToolsWillBegin(_ textView: UITextView)
```

## Parameters

- `textView` — The text view that is about to begin a writing tools session.

## Discussion

Use this method to take any necessary steps to prepare your app for writing tools interactions. During the course of a writing tools session, the writing tools UI suggests changes to the text view’s text. It also allows the person to toggle between the original and replacement text before choosing one. To avoid issues while these changes occur, save any current data to disk and and disable features that might modify your view’s text storage while the session is active. For example, disable iCloud synchronization until the session ends. Reenable those features when the session ends.

The text view calls this method when the person requests the writing tools interface, but before the interface makes any changes to your content. Because the session isn’t active yet, the [writingToolsActive](../uitextview/iswritingtoolsactive.md) property of the text view is [false](../../swift/false.md) while this method executes. The value of that property resolves to [true](../../swift/true.md) only after the method returns.

## See Also

### Responding to writing tools interactions

- [- textViewWritingToolsDidEnd:](<textviewwritingtoolsdidend(__).md>) — Tells the delegate that the current writing tools session ended.
- [- textView:writingToolsIgnoredRangesInEnclosingRange:](<textview(__writingtoolsignoredrangesinenclosingrange_).md>) — Asks the delegate to specify any ranges of text you want the writing tools to ignore.
