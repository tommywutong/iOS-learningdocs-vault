---
title: UITargetedDragPreview
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitargeteddragpreview
source_url: 'https://developer.apple.com/documentation/uikit/uitargeteddragpreview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitargeteddragpreview.json'
content_hash: 'sha256:379123d7bb7b1297'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITargetedDragPreview

<sub>Class</sub>

A drag item preview used by the system during lift, drop, or cancellation animation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UITargetedDragPreview
```

## Relationships

- **Inherits From**: [UITargetedPreview](uitargetedpreview.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing a targeted drag item preview

- [init(forURL:target:)](<uitargeteddragpreview/init(forurl_target_).md>) — Initializes a new targeted drag item preview with a URL and a drag item preview.
- [init(forURL:title:target:)](<uitargeteddragpreview/init(forurl_title_target_).md>) — Initializes a new targeted drag item preview with a URL, a title, and a drag item preview.

### Replacing the preview

- [- retargetedPreviewWithTarget:](<uitargeteddragpreview/retargetedpreview(with_).md>) — Returns a new targeted drag item preview based on an existing one, but with a new geometric target.

### Initializers

- [+ previewForURL:target:](<uitargeteddragpreview/init(for_target_).md>)
- [+ previewForURL:title:target:](<uitargeteddragpreview/init(for_title_target_).md>)

### Default Implementations

- [UITargetedDragPreview Implementations](uitargeteddragpreview/uitargeteddragpreview-implementations.md)

## See Also

### Custom drag item previews

- [UIDragPreviewParameters](uidragpreviewparameters.md) — A set of parameters for adjusting the appearance of a drag item preview or a targeted drag item preview.
- [UIDragPreview](uidragpreview.md) — A graphical preview for a single drag item, used by the system after a drag has started and when no related animation is running.
- [UIDragPreviewTarget](uidragpreviewtarget.md) — A geometric specification for the source or destination of a drag item preview, used by the system when a user drops items or cancels a drag activity.
