---
title: UITargetedPreview
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitargetedpreview
source_url: 'https://developer.apple.com/documentation/uikit/uitargetedpreview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitargetedpreview.json'
content_hash: 'sha256:295e79673a6f55fb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITargetedPreview

<sub>Class</sub>

An object describing the view to use during preview-related animations.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UITargetedPreview
```

## Overview

Use a [UITargetedPreview](uitargetedpreview.md) to specify the view to use during an animated transition.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UITargetedDragPreview](uitargeteddragpreview.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a targeted preview object

- [Adding context menus in your app](adding-context-menus-in-your-app.md) — Provide quick access to useful actions by adding context menus to your iOS app.
- [- initWithView:parameters:target:](<uitargetedpreview/init(view_parameters_target_).md>) — Creates a targeted preview with the specified view, parameters, and target container.
- [- initWithView:parameters:](<uitargetedpreview/init(view_parameters_).md>) — Creates a targeted preview for a view in the current window and including the specified parameters.
- [- initWithView:](<uitargetedpreview/init(view_).md>) — Creates a targeted preview for a view in the current window.

### Getting the preview attributes

- [view](uitargetedpreview/view.md) — The view that’s the target of the animation.
- [target](uitargetedpreview/target.md) — The container for the target view.
- [size](uitargetedpreview/size.md) — The size of the view.
- [parameters](uitargetedpreview/parameters.md) — Additional parameters to use when configuring the animations.

### Changing the target’s container

- [- retargetedPreviewWithTarget:](<uitargetedpreview/retargetedpreview(with_).md>) — Returns a targeted preview object with the same view and parameters, but with a different target container.

## See Also

### Contextual menus

- [UIContextMenuSystem](uicontextmenusystem.md) — The context menu system.
- [UIContextMenuInteraction](uicontextmenuinteraction.md) — An interaction object that you use to display relevant actions for your content.
- [UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md) — The methods for providing the set of actions to perform on your content, and for customizing the preview of that content.
- [UIPreviewTarget](uipreviewtarget.md) — An object that specifies the container view to use for animations.
- [UIPreviewParameters](uipreviewparameters.md) — Additional parameters to use when animating a preview interface.
