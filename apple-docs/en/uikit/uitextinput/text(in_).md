---
title: 'text(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/text(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/text(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/text%28in%3A%29.json'
content_hash: 'sha256:35cafb4c8950c204'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# text(in:)

<sub>Instance Method</sub>

Returns the text in the specified range.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func text(in range: UITextRange) -> String?
```

## Parameters

- `range` — A range of text in a document.

## Return Value

A substring of a document that falls within the specified range.

## See Also

### Replacing and returning text

- [- replaceRange:withText:](<replace(__withtext_).md>) — Replaces the text in a document that is in the specified range.
- [- shouldChangeTextInRange:replacementText:](<shouldchangetext(in_replacementtext_).md>) — Asks whether to replace the text in the specified range.
