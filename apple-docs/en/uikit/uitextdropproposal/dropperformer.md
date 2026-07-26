---
title: dropPerformer
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextdropproposal/dropperformer
source_url: 'https://developer.apple.com/documentation/uikit/uitextdropproposal/dropperformer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdropproposal/dropperformer.json'
content_hash: 'sha256:9b4e640ac3af9ce0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextDropProposal](../uitextdropproposal.md)

# dropPerformer

<sub>Instance Property</sub>

The performer that is responsible for handling the drop operation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var dropPerformer: UITextDropProposal.Performer { get set }
```

## Discussion

The performer provides a preview for the drop activity, loads the data from the item providers, and inserts the data into the text view. It can be the [UITextDropPerformerView](performer/view.md) performer (default) or the [UITextDropPerformerDelegate](performer/delegate.md) performer.

## See Also

### Configuring a text drop proposal

- [dropAction](dropaction.md) — A text drop action style that specifies how the text view receives dropped items.
- [Action](action.md) — The text drop action styles for text views.
- [Performer](performer.md) — The performers that are responsible for handling the drop operation.
- [dropProgressMode](dropprogressmode.md) — A mode that specifies how the text view indicates progress to the user when loading dropped items.
- [ProgressMode](progressmode.md) — The text drop progress styles for user-visible progress indication.
- [useFastSameViewOperations](usefastsameviewoperations.md) — A Boolean value that determines whether the text view can use fast inline dropping when the source and destination are in the same text view.
