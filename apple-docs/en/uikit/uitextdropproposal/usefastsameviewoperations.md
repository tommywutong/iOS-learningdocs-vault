---
title: useFastSameViewOperations
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextdropproposal/usefastsameviewoperations
source_url: 'https://developer.apple.com/documentation/uikit/uitextdropproposal/usefastsameviewoperations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdropproposal/usefastsameviewoperations.json'
content_hash: 'sha256:4f6556c1b63bfaea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextDropProposal](../uitextdropproposal.md)

# useFastSameViewOperations

<sub>Instance Property</sub>

A Boolean value that determines whether the text view can use fast inline dropping when the source and destination are in the same text view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var useFastSameViewOperations: Bool { get set }
```

## Discussion

If this property is [true](../../swift/true.md), the drag item data isn’t used. Instead, the drop operation moves or copies the text from its original position to the dropped position within the text view. The default value is [true](../../swift/true.md).

## See Also

### Configuring a text drop proposal

- [dropAction](dropaction.md) — A text drop action style that specifies how the text view receives dropped items.
- [Action](action.md) — The text drop action styles for text views.
- [dropPerformer](dropperformer.md) — The performer that is responsible for handling the drop operation.
- [Performer](performer.md) — The performers that are responsible for handling the drop operation.
- [dropProgressMode](dropprogressmode.md) — A mode that specifies how the text view indicates progress to the user when loading dropped items.
- [ProgressMode](progressmode.md) — The text drop progress styles for user-visible progress indication.
