---
title: UITextDropProposal.ProgressMode
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextdropproposal/progressmode
source_url: 'https://developer.apple.com/documentation/uikit/uitextdropproposal/progressmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdropproposal/progressmode.json'
content_hash: 'sha256:3a3f1166a258973e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextDropProposal](../uitextdropproposal.md)

# UITextDropProposal.ProgressMode

<sub>Enumeration</sub>

The text drop progress styles for user-visible progress indication.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum ProgressMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Progress modes

- [UITextDropProgressModeCustom](progressmode/custom.md) — A text drop progress mode that indicates that you will provide custom progress indicator during the loading of dropped items.
- [UITextDropProgressModeSystem](progressmode/system.md) — A text drop progress mode indicating that the system will show the progress indicator.

### Initializers

- [init(rawValue:)](<progressmode/init(rawvalue_).md>)

## See Also

### Drop management

- [UITextDropRequest](../uitextdroprequest.md) — The interface for specifying the attributes of a drop request for a text view.
- [UITextDropProposal](../uitextdropproposal.md) — A proposed configuration for the behavior of a text drop interaction.
- [Action](action.md) — The text drop action styles for text views.
- [Performer](performer.md) — The performers that are responsible for handling the drop operation.
