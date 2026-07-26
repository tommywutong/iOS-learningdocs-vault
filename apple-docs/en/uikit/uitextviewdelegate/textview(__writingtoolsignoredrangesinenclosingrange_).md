---
title: 'textView(_:writingToolsIgnoredRangesInEnclosingRange:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.4+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextviewdelegate/textview(_:writingtoolsignoredrangesinenclosingrange:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:writingtoolsignoredrangesinenclosingrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextviewdelegate/textview%28_%3Awritingtoolsignoredrangesinenclosingrange%3A%29.json'
content_hash: 'sha256:143986e56fd65bca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextViewDelegate](../uitextviewdelegate.md)

# textView(_:writingToolsIgnoredRangesInEnclosingRange:)

<sub>Instance Method</sub>

Asks the delegate to specify any ranges of text you want the writing tools to ignore.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func textView(_ textView: UITextView, writingToolsIgnoredRangesInEnclosingRange enclosingRange: NSRange) -> [NSValue]
```

## Parameters

- `textView` — The text view with the active writing tools session.

- `enclosingRange` — The text range that the writing tools are examining. When computing the text ranges to ignore, skip any text that falls outside of this boundary.

## Return Value

One or more ranges of text you want the writing tools to ignore. Return an empty array to allow the modification of all the proposed text.

## Discussion

Use this method to prevent the writing tools session from modifying portions of the current text. For example, you might prevent the writing tools session from modifying code or read-only text. The text view provides you with the overall range of text to consider, and you return one or more subranges you want the writing tools to ignore.

## See Also

### Responding to writing tools interactions

- [- textViewWritingToolsWillBegin:](<textviewwritingtoolswillbegin(__).md>) — Tells the delegate that an interaction with the writing tools interface is about to begin.
- [- textViewWritingToolsDidEnd:](<textviewwritingtoolsdidend(__).md>) — Tells the delegate that the current writing tools session ended.
