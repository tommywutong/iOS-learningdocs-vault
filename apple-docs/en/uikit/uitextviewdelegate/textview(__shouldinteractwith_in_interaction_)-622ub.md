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
doc_path: '/documentation/uikit/uitextviewdelegate/textview(_:shouldinteractwith:in:interaction:)-622ub'
source_url: 'https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:shouldinteractwith:in:interaction:)-622ub'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextviewdelegate/textview%28_%3Ashouldinteractwith%3Ain%3Ainteraction%3A%29-622ub.json'
content_hash: 'sha256:2c416b29c0201ef1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextViewDelegate](../uitextviewdelegate.md)

# textView(_:shouldInteractWith:in:interaction:)

<sub>Instance Method</sub>

Asks the delegate whether the specified text view allows the specified type of user interaction with the specified URL in the specified range of text.

> [!warning] Deprecated
> Use text item methods in [UITextViewDelegate](../uitextviewdelegate.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textView(_ textView: UITextView, shouldInteractWith URL: URL, in characterRange: NSRange, interaction: UITextItemInteraction) -> Bool
```

## Parameters

- `textView` — The text view containing the text attachment.

- `URL` — The URL to be processed.

- `characterRange` — The character range containing the URL.

- `interaction` — The type of interaction that is occurring (for possible values, see [UITextItemInteraction](../uitextiteminteraction.md)).

## Return Value

[true](../../swift/true.md) if interaction with the URL should be allowed; [false](../../swift/false.md) if interaction should not be allowed.

## Discussion

This method is called on only the first interaction with the URL link. For example, this method is called when the user wants their first interaction with a URL to display a list of actions they can take; if the user chooses an open action from the list, this method is not called, because “open” represents the second interaction with the same URL.

> [!important] Important
> Links in text views are interactive only if the text view is selectable but noneditable. That is, if the value of the [UITextView](../uitextview.md) [selectable](../uitextview/isselectable.md) property is [true](../../swift/true.md) and the [editable](../uitextview/iseditable.md) property is [false](../../swift/false.md).

## See Also

### Deprecated

- [- textView:shouldInteractWithTextAttachment:inRange:interaction:](<textview(__shouldinteractwith_in_interaction_)-5qha9.md>) — Asks the delegate whether the specified text view allows the specified type of user interaction with the provided text attachment in the specified range of text. _(deprecated)_
- [- textView:shouldInteractWithTextAttachment:inRange:](<textview(__shouldinteractwith_in_)-97zx6.md>) — Asks the delegate whether the specified text view allows user interaction with the provided text attachment in the specified range of text. _(deprecated)_
- [- textView:shouldInteractWithURL:inRange:](<textview(__shouldinteractwith_in_)-98tho.md>) — Asks the delegate whether the specified text view allows user interaction with the specified URL in the specified range of text. _(deprecated)_
- [UITextItemInteraction](../uitextiteminteraction.md) — Constants that indicate the type of interaction the user expects to have with a URL or text attachment. _(deprecated)_
