---
title: selectedTextRange
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinput/selectedtextrange
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/selectedtextrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/selectedtextrange.json'
content_hash: 'sha256:d3906cc7f3b15493'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# selectedTextRange

<sub>Instance Property</sub>

The range of selected text in a document.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var selectedTextRange: UITextRange? { get set }
```

## Discussion

If the text range has a length, it indicates the currently selected text. If it has zero length, it indicates the caret (insertion point). If the text-range object is `nil`, it indicates that there is no current selection.

## See Also

### Related Documentation

- [empty](../uitextrange/isempty.md) — A Boolean value that indicates whether the range of text represented by the receiver is zero-length.

### Working with marked and selected text

- [markedTextRange](markedtextrange.md) — The range of currently marked text in a document.
- [markedTextStyle](markedtextstyle.md) — A dictionary of attributes that describes how to draw marked text.
- [- setMarkedText:selectedRange:](<setmarkedtext(__selectedrange_).md>) — Inserts the provided text and marks it to indicate that it is part of an active input session.
- [- setAttributedMarkedText:selectedRange:](<setattributedmarkedtext(__selectedrange_).md>) — Inserts the provided styled text and marks it to indicate that it is part of an active input session.
- [- unmarkText](<unmarktext().md>) — Unmarks the currently marked text.
- [selectionAffinity](selectionaffinity.md) — The desired location for the insertion point.
