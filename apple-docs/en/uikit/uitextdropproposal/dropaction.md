---
title: dropAction
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextdropproposal/dropaction
source_url: 'https://developer.apple.com/documentation/uikit/uitextdropproposal/dropaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdropproposal/dropaction.json'
content_hash: 'sha256:d794545c1012af3d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextDropProposal](../uitextdropproposal.md)

# dropAction

<sub>Instance Property</sub>

A text drop action style that specifies how the text view receives dropped items.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var dropAction: UITextDropProposal.Action { get set }
```

## Discussion

The property’s default value is [UITextDropActionInsert](action/insert.md).

## See Also

### Configuring a text drop proposal

- [Action](action.md) — The text drop action styles for text views.
- [dropPerformer](dropperformer.md) — The performer that is responsible for handling the drop operation.
- [Performer](performer.md) — The performers that are responsible for handling the drop operation.
- [dropProgressMode](dropprogressmode.md) — A mode that specifies how the text view indicates progress to the user when loading dropped items.
- [ProgressMode](progressmode.md) — The text drop progress styles for user-visible progress indication.
- [useFastSameViewOperations](usefastsameviewoperations.md) — A Boolean value that determines whether the text view can use fast inline dropping when the source and destination are in the same text view.
