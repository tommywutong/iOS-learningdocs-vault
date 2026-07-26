---
title: UIDragPreviewParameters
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidragpreviewparameters
source_url: 'https://developer.apple.com/documentation/uikit/uidragpreviewparameters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidragpreviewparameters.json'
content_hash: 'sha256:4c469df1b28f78aa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDragPreviewParameters

<sub>Class</sub>

A set of parameters for adjusting the appearance of a drag item preview or a targeted drag item preview.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIDragPreviewParameters
```

## Overview

You can refine the appearance of a preview by providing additional parameters when creating a [UIDragPreview](uidragpreview.md) or [UITargetedDragPreview](uitargeteddragpreview.md) object. The parameters specify different visual aspects of the preview, including the background color and the visible area of the view associated with the preview.

## Relationships

- **Inherits From**: [UIPreviewParameters](uipreviewparameters.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## See Also

### Custom drag item previews

- [UIDragPreview](uidragpreview.md) — A graphical preview for a single drag item, used by the system after a drag has started and when no related animation is running.
- [UIDragPreviewTarget](uidragpreviewtarget.md) — A geometric specification for the source or destination of a drag item preview, used by the system when a user drops items or cancels a drag activity.
- [UITargetedDragPreview](uitargeteddragpreview.md) — A drag item preview used by the system during lift, drop, or cancellation animation.
