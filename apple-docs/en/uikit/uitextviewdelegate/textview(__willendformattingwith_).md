---
title: 'textView(_:willEndFormattingWith:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, visionOS 26.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextviewdelegate/textview(_:willendformattingwith:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:willendformattingwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextviewdelegate/textview%28_%3Awillendformattingwith%3A%29.json'
content_hash: 'sha256:20cb62c1b25bed6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextViewDelegate](../uitextviewdelegate.md)

# textView(_:willEndFormattingWith:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func textView(_ textView: UITextView, willEndFormattingWith viewController: UITextFormattingViewController)
```

## Parameters

- `viewController` — The text formatting controller that is being presented.

## Discussion

Informs the delegate that text formatting controller is about to be dismissed.
