---
title: UITextDropProposal.Action
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextdropproposal/action
source_url: 'https://developer.apple.com/documentation/uikit/uitextdropproposal/action'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdropproposal/action.json'
content_hash: 'sha256:a3d61b91e6742f46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextDropProposal](../uitextdropproposal.md)

# UITextDropProposal.Action

<sub>Enumeration</sub>

The text drop action styles for text views.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum Action
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Text drop actions

- [UITextDropActionInsert](action/insert.md) — A text drop action style specifying that text is inserted at the provided location, without altering the surrounding text.
- [UITextDropActionReplaceAll](action/replaceall.md) — A text drop action style specifying that the dropped text replaces all text in the target text view.
- [UITextDropActionReplaceSelection](action/replaceselection.md) — A text drop action style specifying that if the target text view contains a selection, dropped text replaces it.

### Initializers

- [init(rawValue:)](<action/init(rawvalue_).md>)

## See Also

### Drop management

- [UITextDropRequest](../uitextdroprequest.md) — The interface for specifying the attributes of a drop request for a text view.
- [UITextDropProposal](../uitextdropproposal.md) — A proposed configuration for the behavior of a text drop interaction.
- [Performer](performer.md) — The performers that are responsible for handling the drop operation.
- [ProgressMode](progressmode.md) — The text drop progress styles for user-visible progress indication.
