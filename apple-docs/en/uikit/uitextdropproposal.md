---
title: UITextDropProposal
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextdropproposal
source_url: 'https://developer.apple.com/documentation/uikit/uitextdropproposal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdropproposal.json'
content_hash: 'sha256:70235f9058ae1612'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextDropProposal

<sub>Class</sub>

A proposed configuration for the behavior of a text drop interaction.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UITextDropProposal
```

## Relationships

- **Inherits From**: [UIDropProposal](uidropproposal.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Configuring a text drop proposal

- [dropAction](uitextdropproposal/dropaction.md) — A text drop action style that specifies how the text view receives dropped items.
- [Action](uitextdropproposal/action.md) — The text drop action styles for text views.
- [dropPerformer](uitextdropproposal/dropperformer.md) — The performer that is responsible for handling the drop operation.
- [Performer](uitextdropproposal/performer.md) — The performers that are responsible for handling the drop operation.
- [dropProgressMode](uitextdropproposal/dropprogressmode.md) — A mode that specifies how the text view indicates progress to the user when loading dropped items.
- [ProgressMode](uitextdropproposal/progressmode.md) — The text drop progress styles for user-visible progress indication.
- [useFastSameViewOperations](uitextdropproposal/usefastsameviewoperations.md) — A Boolean value that determines whether the text view can use fast inline dropping when the source and destination are in the same text view.

## See Also

### Drop management

- [UITextDropRequest](uitextdroprequest.md) — The interface for specifying the attributes of a drop request for a text view.
- [Action](uitextdropproposal/action.md) — The text drop action styles for text views.
- [Performer](uitextdropproposal/performer.md) — The performers that are responsible for handling the drop operation.
- [ProgressMode](uitextdropproposal/progressmode.md) — The text drop progress styles for user-visible progress indication.
