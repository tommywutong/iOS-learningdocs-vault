---
title: 'textView(_:shouldChangeTextInRanges:replacementText:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextviewdelegate/textview(_:shouldchangetextinranges:replacementtext:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:shouldchangetextinranges:replacementtext:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextviewdelegate/textview%28_%3Ashouldchangetextinranges%3Areplacementtext%3A%29.json'
content_hash: 'sha256:6fc7382a914bfd06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextViewDelegate](../uitextviewdelegate.md)

# textView(_:shouldChangeTextInRanges:replacementText:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textView(_ textView: UITextView, shouldChangeTextInRanges ranges: [NSValue], replacementText text: String) -> Bool
```

## Parameters

- `textView` — The text view asking the delegate

- `ranges` — The ranges of the text that should be deleted before replacing

## Return Value

Returns true if the text at the `ranges` should be replaced.

## Discussion

Asks the delegate if the text at the specified `ranges` should be replaced with `text`.

If this method returns YES then the text view will, at its own discretion, choose any one of the specified `ranges` of text and replace it with the specified `replacementText` before deleting the text at the other ranges. If the delegate does not implement this method then the `textView:shouldChangeTextInRange:replacementText:` method will be called and passed the union range instead. If the delegate also does not implement that method then YES is assumed.
