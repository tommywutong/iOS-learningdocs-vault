---
title: 'textViewWritingToolsDidEnd(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.4+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextviewdelegate/textviewwritingtoolsdidend(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextviewdelegate/textviewwritingtoolsdidend(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextviewdelegate/textviewwritingtoolsdidend%28_%3A%29.json'
content_hash: 'sha256:387e7109bea673fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextViewDelegate](../uitextviewdelegate.md)

# textViewWritingToolsDidEnd(_:)

<sub>Instance Method</sub>

Tells the delegate that the current writing tools session ended.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func textViewWritingToolsDidEnd(_ textView: UITextView)
```

## Parameters

- `textView` — The text view that ended a writing tools session.

## Discussion

Use this method to undo any actions you took at the start of a writing tools session to modify your app’s behavior.  The text view calls this method after the writing session finishes. At this point, the text view contains the final text the person chose.

## See Also

### Responding to writing tools interactions

- [- textViewWritingToolsWillBegin:](<textviewwritingtoolswillbegin(__).md>) — Tells the delegate that an interaction with the writing tools interface is about to begin.
- [- textView:writingToolsIgnoredRangesInEnclosingRange:](<textview(__writingtoolsignoredrangesinenclosingrange_).md>) — Asks the delegate to specify any ranges of text you want the writing tools to ignore.
