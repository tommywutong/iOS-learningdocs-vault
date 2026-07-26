---
title: 'replace(_:withText:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/replace(_:withtext:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/replace(_:withtext:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/replace%28_%3Awithtext%3A%29.json'
content_hash: 'sha256:157246f7f2a9ec50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# replace(_:withText:)

<sub>Instance Method</sub>

Replaces the text in a document that is in the specified range.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func replace(_ range: UITextRange, withText text: String)
```

## Parameters

- `range` — A range of text in a document.

- `text` — A string to replace the text in `range`.

## See Also

### Replacing and returning text

- [- textInRange:](<text(in_).md>) — Returns the text in the specified range.
- [- shouldChangeTextInRange:replacementText:](<shouldchangetext(in_replacementtext_).md>) — Asks whether to replace the text in the specified range.
