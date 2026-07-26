---
title: UIDragPreview
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidragpreview
source_url: 'https://developer.apple.com/documentation/uikit/uidragpreview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidragpreview.json'
content_hash: 'sha256:3f794731341f2af4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDragPreview

<sub>Class</sub>

A graphical preview for a single drag item, used by the system after a drag has started and when no related animation is running.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIDragPreview
```

## Overview

A [UIDragPreview](uidragpreview.md) object is a visual representation of the drag item. The preview is displayed while the user moves the item across the screen with their finger (after the lift animation completes). The preview disappears when the user lifts their finger, triggering the start of the drop or cancellation animation.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Initializing a drag item preview

- [- initWithView:](<uidragpreview/init(view_).md>) — Initializes a new drag item preview with a view, using the default appearance parameters.
- [- initWithView:parameters:](<uidragpreview/init(view_parameters_).md>) — Initializes a new drag item preview with a view and with a set of appearance parameters.
- [init(forURL:)](<uidragpreview/init(forurl_).md>) — Initializes a new drag item preview with a URL.
- [init(forURL:title:)](<uidragpreview/init(forurl_title_).md>) — Initializes a drag item preview with a URL and title.

### Getting the visual appearance parameters

- [parameters](uidragpreview/parameters.md) — The appearance parameters associated with the drag item preview.

### Accessing the view

- [view](uidragpreview/view.md) — The view associated with the drag item preview.

### Initializers

- [+ previewForURL:](<uidragpreview/init(for_).md>)
- [+ previewForURL:title:](<uidragpreview/init(for_title_).md>)

### Default Implementations

- [UIDragPreview Implementations](uidragpreview/uidragpreview-implementations.md)

## See Also

### Custom drag item previews

- [UIDragPreviewParameters](uidragpreviewparameters.md) — A set of parameters for adjusting the appearance of a drag item preview or a targeted drag item preview.
- [UIDragPreviewTarget](uidragpreviewtarget.md) — A geometric specification for the source or destination of a drag item preview, used by the system when a user drops items or cancels a drag activity.
- [UITargetedDragPreview](uitargeteddragpreview.md) — A drag item preview used by the system during lift, drop, or cancellation animation.
