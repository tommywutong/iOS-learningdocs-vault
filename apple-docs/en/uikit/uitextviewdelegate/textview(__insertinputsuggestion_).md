---
title: 'textView(_:insertInputSuggestion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.4+, iPadOS 18.4+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextviewdelegate/textview(_:insertinputsuggestion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:insertinputsuggestion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextviewdelegate/textview%28_%3Ainsertinputsuggestion%3A%29.json'
content_hash: 'sha256:c743ebbe4e6ce283'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextViewDelegate](../uitextviewdelegate.md)

# textView(_:insertInputSuggestion:)

<sub>Instance Method</sub>

Tells the delegate when the keyboard delivers an input suggestion.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func textView(_ textView: UITextView, insertInputSuggestion inputSuggestion: UIInputSuggestion)
```

## Parameters

- `textView` — The text view that is currently the first responder.

- `inputSuggestion` — The input suggestion that the user or system selected.
