---
title: 'textView(_:willBeginFormattingWith:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, visionOS 26.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextviewdelegate/textview(_:willbeginformattingwith:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:willbeginformattingwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextviewdelegate/textview%28_%3Awillbeginformattingwith%3A%29.json'
content_hash: 'sha256:41d42c2a40c521a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextViewDelegate](../uitextviewdelegate.md)

# textView(_:willBeginFormattingWith:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func textView(_ textView: UITextView, willBeginFormattingWith viewController: UITextFormattingViewController)
```

## Parameters

- `viewController` — The text formatting controller that is being presented.

## Discussion

Informs the delegate that text formatting controller is about to be presented.
