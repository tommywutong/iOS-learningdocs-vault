---
title: UIDragPreviewTarget
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidragpreviewtarget
source_url: 'https://developer.apple.com/documentation/uikit/uidragpreviewtarget'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidragpreviewtarget.json'
content_hash: 'sha256:64e5eb95f20afe62'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDragPreviewTarget

<sub>Class</sub>

A geometric specification for the source or destination of a drag item preview, used by the system when a user drops items or cancels a drag activity.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIDragPreviewTarget
```

## Relationships

- **Inherits From**: [UIPreviewTarget](uipreviewtarget.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## See Also

### Custom drag item previews

- [UIDragPreviewParameters](uidragpreviewparameters.md) — A set of parameters for adjusting the appearance of a drag item preview or a targeted drag item preview.
- [UIDragPreview](uidragpreview.md) — A graphical preview for a single drag item, used by the system after a drag has started and when no related animation is running.
- [UITargetedDragPreview](uitargeteddragpreview.md) — A drag item preview used by the system during lift, drop, or cancellation animation.
