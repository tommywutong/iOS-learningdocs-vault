---
title: 'textView(_:shouldInteractWith:in:interaction:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+（17.0 起废弃）, iPadOS 10.0+（17.0 起废弃）, Mac Catalyst 13.1+（17.0 起废弃）, tvOS 10.0+（17.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uitextviewdelegate/textview(_:shouldinteractwith:in:interaction:)-5qha9'
source_url: 'https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:shouldinteractwith:in:interaction:)-5qha9'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextviewdelegate/textview%28_%3Ashouldinteractwith%3Ain%3Ainteraction%3A%29-5qha9.json'
content_hash: 'sha256:a3665f68fa26ba9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextViewDelegate](../uitextviewdelegate.md)

# textView(_:shouldInteractWith:in:interaction:)

<sub>Instance Method</sub>

Asks the delegate whether the specified text view allows the specified type of user interaction with the provided text attachment in the specified range of text.

> [!warning] Deprecated
> Use text item methods in [UITextViewDelegate](../uitextviewdelegate.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textView(_ textView: UITextView, shouldInteractWith textAttachment: NSTextAttachment, in characterRange: NSRange, interaction: UITextItemInteraction) -> Bool
```

## Parameters

- `textView` — The text view containing the text attachment.

- `textAttachment` — The text attachment.

- `characterRange` — The character range containing the text attachment.

- `interaction` — The type of interaction that is occurring (for possible values, see [UITextItemInteraction](../uitextiteminteraction.md)).

## Return Value

[true](../../swift/true.md) if interaction with the text attachment should be allowed; [false](../../swift/false.md) if interaction should not be allowed.

## Discussion

A text view calls this method if the user taps or long-presses the text attachment and its [image](../nstextattachment/image.md) property is not `nil`. You can use this method to trigger an action in addition to displaying the text attachment inline with the text.

## See Also

### Deprecated

- [- textView:shouldInteractWithURL:inRange:interaction:](<textview(__shouldinteractwith_in_interaction_)-622ub.md>) — Asks the delegate whether the specified text view allows the specified type of user interaction with the specified URL in the specified range of text. _(deprecated)_
- [- textView:shouldInteractWithTextAttachment:inRange:](<textview(__shouldinteractwith_in_)-97zx6.md>) — Asks the delegate whether the specified text view allows user interaction with the provided text attachment in the specified range of text. _(deprecated)_
- [- textView:shouldInteractWithURL:inRange:](<textview(__shouldinteractwith_in_)-98tho.md>) — Asks the delegate whether the specified text view allows user interaction with the specified URL in the specified range of text. _(deprecated)_
- [UITextItemInteraction](../uitextiteminteraction.md) — Constants that indicate the type of interaction the user expects to have with a URL or text attachment. _(deprecated)_
