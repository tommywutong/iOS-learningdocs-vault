---
title: selectionAffinity
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinput/selectionaffinity
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/selectionaffinity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/selectionaffinity.json'
content_hash: 'sha256:92cbe4599478c1ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# selectionAffinity

<sub>Instance Property</sub>

The desired location for the insertion point.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional var selectionAffinity: UITextStorageDirection { get set }
```

## Discussion

For text selections that wrap across line boundaries, this property determines whether the insertion point appears after the last character on the line or before the first character on the following line. The selection affinity is set in response to the user navigating via the keyboard (for example, command-right-arrow). The text input system checks this property when it moves the insertion point around in a document.

In the default implementation, if the selection is not at the end of the line, or if the selection is at the start of a paragraph for an empty line, a forward direction is assumed ([UITextStorageDirectionForward](../uitextstoragedirection/forward.md)); otherwise, a backward direction [UITextStorageDirectionBackward](../uitextstoragedirection/backward.md) is assumed.

## See Also

### Working with marked and selected text

- [selectedTextRange](selectedtextrange.md) — The range of selected text in a document.
- [markedTextRange](markedtextrange.md) — The range of currently marked text in a document.
- [markedTextStyle](markedtextstyle.md) — A dictionary of attributes that describes how to draw marked text.
- [- setMarkedText:selectedRange:](<setmarkedtext(__selectedrange_).md>) — Inserts the provided text and marks it to indicate that it is part of an active input session.
- [- setAttributedMarkedText:selectedRange:](<setattributedmarkedtext(__selectedrange_).md>) — Inserts the provided styled text and marks it to indicate that it is part of an active input session.
- [- unmarkText](<unmarktext().md>) — Unmarks the currently marked text.
