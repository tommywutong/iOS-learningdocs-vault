---
title: 'shouldChangeText(in:replacementText:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/shouldchangetext(in:replacementtext:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/shouldchangetext(in:replacementtext:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/shouldchangetext%28in%3Areplacementtext%3A%29.json'
content_hash: 'sha256:688e0d9954e3004b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# shouldChangeText(in:replacementText:)

<sub>Instance Method</sub>

Asks whether to replace the text in the specified range.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func shouldChangeText(in range: UITextRange, replacementText text: String) -> Bool
```

## Parameters

- `range` — A range of text in a document.

- `text` — The proposed text to replace the text in `range`.

## Return Value

[true](../../swift/true.md) if the text should be changed or [false](../../swift/false.md) if it should not.

## Discussion

Prior to replacing text, this method is called to give your delegate a chance to accept or reject the edits. If you do not implement this method, the return value defaults to [true](../../swift/true.md).

## See Also

### Replacing and returning text

- [- textInRange:](<text(in_).md>) — Returns the text in the specified range.
- [- replaceRange:withText:](<replace(__withtext_).md>) — Replaces the text in a document that is in the specified range.
