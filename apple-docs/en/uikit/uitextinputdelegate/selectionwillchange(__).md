---
title: 'selectionWillChange(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinputdelegate/selectionwillchange(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputdelegate/selectionwillchange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputdelegate/selectionwillchange%28_%3A%29.json'
content_hash: 'sha256:aea3c21ffc24e79d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputDelegate](../uitextinputdelegate.md)

# selectionWillChange(_:)

<sub>Instance Method</sub>

Tells the input delegate when the selection is about to change in the document.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func selectionWillChange(_ textInput: (any UITextInput)?)
```

## Parameters

- `textInput` — The document instance whose class adopts the UITextInput protocol.

## See Also

### Related Documentation

- [- textWillChange:](<textwillchange(__).md>) — Tells the input delegate when text is about to change in the document.

### Notifying the delegate of selection changes

- [- selectionDidChange:](<selectiondidchange(__).md>) — Tells the input delegate when the selection has changed in the document.
