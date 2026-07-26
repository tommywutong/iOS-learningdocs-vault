---
title: dropProgressMode
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextdropproposal/dropprogressmode
source_url: 'https://developer.apple.com/documentation/uikit/uitextdropproposal/dropprogressmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdropproposal/dropprogressmode.json'
content_hash: 'sha256:fb7042ff057142f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextDropProposal](../uitextdropproposal.md)

# dropProgressMode

<sub>Instance Property</sub>

A mode that specifies how the text view indicates progress to the user when loading dropped items.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var dropProgressMode: UITextDropProposal.ProgressMode { get set }
```

## Discussion

The default value is [UITextDropProgressModeSystem](progressmode/system.md).

## See Also

### Configuring a text drop proposal

- [dropAction](dropaction.md) — A text drop action style that specifies how the text view receives dropped items.
- [Action](action.md) — The text drop action styles for text views.
- [dropPerformer](dropperformer.md) — The performer that is responsible for handling the drop operation.
- [Performer](performer.md) — The performers that are responsible for handling the drop operation.
- [ProgressMode](progressmode.md) — The text drop progress styles for user-visible progress indication.
- [useFastSameViewOperations](usefastsameviewoperations.md) — A Boolean value that determines whether the text view can use fast inline dropping when the source and destination are in the same text view.
