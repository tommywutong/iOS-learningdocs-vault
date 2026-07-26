---
title: 'textView(_:shouldChangeTextIn:replacementText:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uitextviewdelegate/textview(_:shouldchangetextin:replacementtext:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextviewdelegate/textview(_:shouldchangetextin:replacementtext:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextviewdelegate/textview%28_%3Ashouldchangetextin%3Areplacementtext%3A%29.json'
content_hash: 'sha256:5aaeba3ab782793c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextViewDelegate](../uitextviewdelegate.md)

# textView(_:shouldChangeTextIn:replacementText:)

<sub>Instance Method</sub>

Asks the delegate whether to replace the specified text in the text view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textView(_ textView: UITextView, shouldChangeTextIn range: NSRange, replacementText text: String) -> Bool
```

## Parameters

- `textView` — The text view containing the changes.

- `range` — The current selection range. If the length of the range is 0, `range` reflects the current insertion point. If the user presses the Delete key, the length of the range is 1 and an empty string object replaces that single character.

- `text` — The text to insert.

## Return Value

[true](../../swift/true.md) if the old text should be replaced by the new text; [false](../../swift/false.md) if the replacement operation should be aborted.

## Discussion

The text view calls this method whenever the user types a new character or deletes an existing character. Implementation of this method is optional. You can use this method to replace text before it is committed to the text view storage. For example, a spell checker might use this method to replace a misspelled word with the correct spelling.

## See Also

### Responding to text changes

- [- textViewDidChange:](<textviewdidchange(__).md>) — Tells the delegate when the user changes the text or attributes in the specified text view.
