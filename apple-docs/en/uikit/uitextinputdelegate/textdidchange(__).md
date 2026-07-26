---
title: 'textDidChange(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinputdelegate/textdidchange(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputdelegate/textdidchange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputdelegate/textdidchange%28_%3A%29.json'
content_hash: 'sha256:3808be5bac5dc755'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputDelegate](../uitextinputdelegate.md)

# textDidChange(_:)

<sub>Instance Method</sub>

Tells the input delegate when text has changed in the document.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func textDidChange(_ textInput: (any UITextInput)?)
```

## Parameters

- `textInput` — The document instance whose class adopts the UITextInput protocol.

## See Also

### Related Documentation

- [- selectionDidChange:](<selectiondidchange(__).md>) — Tells the input delegate when the selection has changed in the document.

### Notifying the delegate of textual changes

- [- textWillChange:](<textwillchange(__).md>) — Tells the input delegate when text is about to change in the document.
