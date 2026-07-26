---
title: UITextDropProposal.Performer
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextdropproposal/performer
source_url: 'https://developer.apple.com/documentation/uikit/uitextdropproposal/performer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdropproposal/performer.json'
content_hash: 'sha256:f9359606bc366c12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextDropProposal](../uitextdropproposal.md)

# UITextDropProposal.Performer

<sub>Enumeration</sub>

The performers that are responsible for handling the drop operation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum Performer
```

## Overview

A performer is responsible for:

- Proving a preview for the drop activity.
- Loading data from the item providers.
- Inserting the data into the text view.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Performers

- [UITextDropPerformerView](performer/view.md) — A performer type that indicates that the text view is responsible for doing the drop operation.
- [UITextDropPerformerDelegate](performer/delegate.md) — A performer type that indicates the delegate object is responsible for doing the drop operation.

### Initializers

- [init(rawValue:)](<performer/init(rawvalue_).md>)

## See Also

### Drop management

- [UITextDropRequest](../uitextdroprequest.md) — The interface for specifying the attributes of a drop request for a text view.
- [UITextDropProposal](../uitextdropproposal.md) — A proposed configuration for the behavior of a text drop interaction.
- [Action](action.md) — The text drop action styles for text views.
- [ProgressMode](progressmode.md) — The text drop progress styles for user-visible progress indication.
