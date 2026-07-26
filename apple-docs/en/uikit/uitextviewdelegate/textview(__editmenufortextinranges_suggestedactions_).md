---
title: 'textView(_:editMenuForTextInRanges:suggestedActions:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextviewdelegate/textview(_:editmenufortextinranges:suggestedactions:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:editmenufortextinranges:suggestedactions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextviewdelegate/textview%28_%3Aeditmenufortextinranges%3Asuggestedactions%3A%29.json'
content_hash: 'sha256:2f7d63cec8f5ad20'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextViewDelegate](../uitextviewdelegate.md)

# textView(_:editMenuForTextInRanges:suggestedActions:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textView(_ textView: UITextView, editMenuForTextInRanges ranges: [NSValue], suggestedActions: [UIMenuElement]) -> UIMenu?
```

## Parameters

- `textView` — The text view requesting the menu.

- `ranges` — The text ranges for which the menu is presented for.

- `suggestedActions` — The actions and commands that the system suggests.

## Return Value

Return a UIMenu describing the desired menu hierarchy. Return @c nil to present the default system menu.

## Discussion

Asks the delegate for the menu to be shown for the specified text ranges.

If the delegate does not implement this method then the `textView:editMenuForTextInRange:suggestedActions:` method will be called and passed the union range instead. If the delegate also does not implement that method then `nil` is assumed.
