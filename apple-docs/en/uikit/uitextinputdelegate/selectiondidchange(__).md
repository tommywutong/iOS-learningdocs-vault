---
title: 'selectionDidChange(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinputdelegate/selectiondidchange(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputdelegate/selectiondidchange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputdelegate/selectiondidchange%28_%3A%29.json'
content_hash: 'sha256:21bae2561620d00a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputDelegate](../uitextinputdelegate.md)

# selectionDidChange(_:)

<sub>Instance Method</sub>

Tells the input delegate when the selection has changed in the document.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func selectionDidChange(_ textInput: (any UITextInput)?)
```

## Parameters

- `textInput` — The document instance whose class adopts the UITextInput protocol.

## See Also

### Related Documentation

- [- textDidChange:](<textdidchange(__).md>) — Tells the input delegate when text has changed in the document.

### Notifying the delegate of selection changes

- [- selectionWillChange:](<selectionwillchange(__).md>) — Tells the input delegate when the selection is about to change in the document.
