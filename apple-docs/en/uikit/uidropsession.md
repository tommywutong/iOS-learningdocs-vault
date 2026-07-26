---
title: UIDropSession
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidropsession
source_url: 'https://developer.apple.com/documentation/uikit/uidropsession'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidropsession.json'
content_hash: 'sha256:f826f1e155bdd61f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDropSession

<sub>Protocol</sub>

The interface for querying a drop session about its state and associated drag items.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UIDropSession : ProgressReporting, UIDragDropSession
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [ProgressReporting](../foundation/progressreporting.md), [UIDragDropSession](uidragdropsession.md)

## Topics

### Getting the drag session

- [localDragSession](uidropsession/localdragsession.md) — The drag session that corresponds to this drop session, for in-app drag activities.

### Loading objects

- [- loadObjectsOfClass:completion:](<uidropsession/loadobjects(ofclass_completion_).md>) — Creates and loads a new instance of the specified class for each drag item in the session.

### Showing a progress indicator

- [progressIndicatorStyle](uidropsession/progressindicatorstyle.md) — The drop-progress indicator style associated with the drop session.

## See Also

### Drop destinations

- [UIDropProposal](uidropproposal.md) — A configuration for the behavior of a drop interaction, required if a view accepts drop activities.
- [UIDropOperation](uidropoperation.md) — Operation types that determine how a drag and drop activity resolves when the user drops a drag item.
- [UIDropSessionProgressIndicatorStyle](uidropsessionprogressindicatorstyle.md) — The drop-progress indicator styles for the drop session, used while data is moving from the source to the destination.
