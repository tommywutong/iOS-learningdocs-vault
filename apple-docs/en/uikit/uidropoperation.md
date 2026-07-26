---
title: UIDropOperation
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidropoperation
source_url: 'https://developer.apple.com/documentation/uikit/uidropoperation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidropoperation.json'
content_hash: 'sha256:8bbafad943fddbb9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDropOperation

<sub>Enumeration</sub>

Operation types that determine how a drag and drop activity resolves when the user drops a drag item.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum UIDropOperation
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Drop operation types

- [UIDropOperationCancel](uidropoperation/cancel.md) — A drop operation type specifying that no data should be transferred, thereby canceling the drag.
- [UIDropOperationForbidden](uidropoperation/forbidden.md) — A drop operation type specifying that, although a move or copy operation is typically legitimate in this scenario, the drop activity isn’t allowed.
- [UIDropOperationCopy](uidropoperation/copy.md) — A drop operation type specifying that the data represented by the drag items should be copied to the destination view.
- [UIDropOperationMove](uidropoperation/move.md) — A drop operation type specifying that the data represented by the drag items should be moved, not copied.

### Initializers

- [init(rawValue:)](<uidropoperation/init(rawvalue_).md>)

## See Also

### Drop destinations

- [UIDropSession](uidropsession.md) — The interface for querying a drop session about its state and associated drag items.
- [UIDropProposal](uidropproposal.md) — A configuration for the behavior of a drop interaction, required if a view accepts drop activities.
- [UIDropSessionProgressIndicatorStyle](uidropsessionprogressindicatorstyle.md) — The drop-progress indicator styles for the drop session, used while data is moving from the source to the destination.
