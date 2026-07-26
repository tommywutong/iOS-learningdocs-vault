---
title: 'textView(_:shouldInteractWith:in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+（10.0 起废弃）, iPadOS 7.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（10.0 起废弃）]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uitextviewdelegate/textview(_:shouldinteractwith:in:)-98tho'
source_url: 'https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:shouldinteractwith:in:)-98tho'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextviewdelegate/textview%28_%3Ashouldinteractwith%3Ain%3A%29-98tho.json'
content_hash: 'sha256:d0c1ee85305abc03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextViewDelegate](../uitextviewdelegate.md)

# textView(_:shouldInteractWith:in:)

<sub>Instance Method</sub>

Asks the delegate whether the specified text view allows user interaction with the specified URL in the specified range of text.

> [!warning] Deprecated
> Use [- textView:shouldInteractWithURL:inRange:interaction:](<textview(__shouldinteractwith_in_interaction_)-622ub.md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
optional func textView(_ textView: UITextView, shouldInteractWith URL: URL, in characterRange: NSRange) -> Bool
```

## Parameters

- `textView` — The text view containing the text attachment.

- `URL` — The URL to be processed.

- `characterRange` — The character range containing the URL.

## Return Value

[true](../../swift/true.md) if interaction with the URL should be allowed; [false](../../swift/false.md) if interaction should not be allowed.

## Discussion

The text view calls this method if the user taps or long-presses the URL link. Implementation of this method is optional. By default, the text view opens the application responsible for handling the URL type and passes it the URL. You can use this method to trigger an alternative action, such as displaying the web content at the URL in a web view within the current application.

> [!important] Important
> Links in text views are interactive only if the text view is selectable but noneditable. That is, if the value of the `UITextView` [selectable](../uitextview/isselectable.md) property is [true](../../swift/true.md) and the [editable](../uitextview/iseditable.md) property is [false](../../swift/false.md).

## See Also

### Deprecated

- [- textView:shouldInteractWithTextAttachment:inRange:interaction:](<textview(__shouldinteractwith_in_interaction_)-5qha9.md>) — Asks the delegate whether the specified text view allows the specified type of user interaction with the provided text attachment in the specified range of text. _(deprecated)_
- [- textView:shouldInteractWithURL:inRange:interaction:](<textview(__shouldinteractwith_in_interaction_)-622ub.md>) — Asks the delegate whether the specified text view allows the specified type of user interaction with the specified URL in the specified range of text. _(deprecated)_
- [- textView:shouldInteractWithTextAttachment:inRange:](<textview(__shouldinteractwith_in_)-97zx6.md>) — Asks the delegate whether the specified text view allows user interaction with the provided text attachment in the specified range of text. _(deprecated)_
- [UITextItemInteraction](../uitextiteminteraction.md) — Constants that indicate the type of interaction the user expects to have with a URL or text attachment. _(deprecated)_
