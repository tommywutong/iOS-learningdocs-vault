---
title: 'textViewDidChangeSelection(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextviewdelegate/textviewdidchangeselection(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextviewdelegate/textviewdidchangeselection(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextviewdelegate/textviewdidchangeselection%28_%3A%29.json'
content_hash: 'sha256:19621e17e9c091b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextViewDelegate](../uitextviewdelegate.md)

# textViewDidChangeSelection(_:)

<sub>Instance Method</sub>

Tells the delegate when the text selection changes in the specified text view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textViewDidChangeSelection(_ textView: UITextView)
```

## Parameters

- `textView` — The text view whose selection changed.

## Discussion

Implementation of this method is optional. You can use the [selectedRange](../uitextview/selectedrange.md) property of the text view to get the new selection.
