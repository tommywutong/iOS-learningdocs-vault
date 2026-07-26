---
title: unmarkText()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinput/unmarktext()
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/unmarktext()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/unmarktext%28%29.json'
content_hash: 'sha256:ac97a49b13534473'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# unmarkText()

<sub>Instance Method</sub>

Unmarks the currently marked text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func unmarkText()
```

## Discussion

After this method is called, the value of [markedTextRange](markedtextrange.md) is `nil`.

## See Also

### Working with marked and selected text

- [selectedTextRange](selectedtextrange.md) — The range of selected text in a document.
- [markedTextRange](markedtextrange.md) — The range of currently marked text in a document.
- [markedTextStyle](markedtextstyle.md) — A dictionary of attributes that describes how to draw marked text.
- [- setMarkedText:selectedRange:](<setmarkedtext(__selectedrange_).md>) — Inserts the provided text and marks it to indicate that it is part of an active input session.
- [- setAttributedMarkedText:selectedRange:](<setattributedmarkedtext(__selectedrange_).md>) — Inserts the provided styled text and marks it to indicate that it is part of an active input session.
- [selectionAffinity](selectionaffinity.md) — The desired location for the insertion point.
