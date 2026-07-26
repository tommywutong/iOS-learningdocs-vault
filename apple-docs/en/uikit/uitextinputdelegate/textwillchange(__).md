---
title: 'textWillChange(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinputdelegate/textwillchange(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputdelegate/textwillchange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputdelegate/textwillchange%28_%3A%29.json'
content_hash: 'sha256:e55db95ae699e1c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputDelegate](../uitextinputdelegate.md)

# textWillChange(_:)

<sub>Instance Method</sub>

Tells the input delegate when text is about to change in the document.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func textWillChange(_ textInput: (any UITextInput)?)
```

## Parameters

- `textInput` — The document instance whose class adopts the UITextInput protocol.

## See Also

### Related Documentation

- [- selectionWillChange:](<selectionwillchange(__).md>) — Tells the input delegate when the selection is about to change in the document.

### Notifying the delegate of textual changes

- [- textDidChange:](<textdidchange(__).md>) — Tells the input delegate when text has changed in the document.
