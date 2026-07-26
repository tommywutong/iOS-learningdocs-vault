---
title: UIDropProposal
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidropproposal
source_url: 'https://developer.apple.com/documentation/uikit/uidropproposal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidropproposal.json'
content_hash: 'sha256:091f019fe0f675c2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDropProposal

<sub>Class</sub>

A configuration for the behavior of a drop interaction, required if a view accepts drop activities.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIDropProposal
```

## Overview

If a view’s drop interaction delegate accepts dropped drag items, it must return a drop proposal in its implementation of the [- dropInteraction:sessionDidUpdate:](<uidropinteractiondelegate/dropinteraction(__sessiondidupdate_).md>) method.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UICollectionViewDropProposal](uicollectionviewdropproposal.md), [UITableViewDropProposal](uitableviewdropproposal.md), [UITextDropProposal](uitextdropproposal.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Initializing a drop proposal

- [- initWithDropOperation:](<uidropproposal/init(operation_).md>) — Initializes a new drop proposal with a drop operation type.
- [operation](uidropproposal/operation.md) — The drop operation that the drop interaction proposes to perform.

### Configuring a drop proposal

- [precise](uidropproposal/isprecise.md) — A Boolean value that proposes that the drop interaction define the drop location precisely, such as at a specific point within existing text.
- [prefersFullSizePreview](uidropproposal/prefersfullsizepreview.md) — A Boolean value that indicates that the drag item preview should be shown at its full, original size.

### Initializers

- [init(dropOperation:)](<uidropproposal/init(dropoperation_).md>)

## See Also

### Drop destinations

- [UIDropSession](uidropsession.md) — The interface for querying a drop session about its state and associated drag items.
- [UIDropOperation](uidropoperation.md) — Operation types that determine how a drag and drop activity resolves when the user drops a drag item.
- [UIDropSessionProgressIndicatorStyle](uidropsessionprogressindicatorstyle.md) — The drop-progress indicator styles for the drop session, used while data is moving from the source to the destination.
