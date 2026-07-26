---
title: UIPreviewTarget
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipreviewtarget
source_url: 'https://developer.apple.com/documentation/uikit/uipreviewtarget'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipreviewtarget.json'
content_hash: 'sha256:4e40d34269042d84'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPreviewTarget

<sub>Class</sub>

An object that specifies the container view to use for animations.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIPreviewTarget
```

## Overview

Create a [UIPreviewTarget](uipreviewtarget.md) object when animating views to or from a separate container view. For example, use this method to animate views to or from a different part of your app’s interface.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UIDragPreviewTarget](uidragpreviewtarget.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a preview target object

- [- initWithContainer:center:transform:](<uipreviewtarget/init(container_center_transform_).md>) — Creates a preview target object using the specified container view and configuration details.
- [- initWithContainer:center:](<uipreviewtarget/init(container_center_).md>) — Creates a preview target object using the specified container view and center point.

### Getting the target attributes

- [container](uipreviewtarget/container.md) — The container for the view being animated.
- [center](uipreviewtarget/center.md) — The point in the containing view at which to place the center of the view being animated.
- [transform](uipreviewtarget/transform.md) — An affine transform to apply to the view being animated.

## See Also

### Contextual menus

- [UIContextMenuSystem](uicontextmenusystem.md) — The context menu system.
- [UIContextMenuInteraction](uicontextmenuinteraction.md) — An interaction object that you use to display relevant actions for your content.
- [UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md) — The methods for providing the set of actions to perform on your content, and for customizing the preview of that content.
- [UITargetedPreview](uitargetedpreview.md) — An object describing the view to use during preview-related animations.
- [UIPreviewParameters](uipreviewparameters.md) — Additional parameters to use when animating a preview interface.
