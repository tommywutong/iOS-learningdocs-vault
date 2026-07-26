---
title: UIContextMenuInteraction
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontextmenuinteraction
source_url: 'https://developer.apple.com/documentation/uikit/uicontextmenuinteraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontextmenuinteraction.json'
content_hash: 'sha256:1b847085343e3d63'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIContextMenuInteraction

<sub>Class</sub>

An interaction object that you use to display relevant actions for your content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIContextMenuInteraction
```

## Overview

Use a [UIContextMenuInteraction](uicontextmenuinteraction.md) object to focus the user’s attention on a specific portion of your content, and to provide actions for the user to perform on that content. A context menu interaction object tracks Force Touch gestures on devices that support 3D Touch, and long-press gestures on devices that don’t support it. When the appropriate gesture occurs, this object animates your content to a new interface and displays the contextual menu that you supplied. UIKit manages all menu-related interactions and reports the selected action, if any, back to your app.

A context menu interaction object inherits from [UIInteraction](uiinteraction.md). After creating the object, assign an appropriate object to its [delegate](uicontextmenuinteraction/delegate.md) property and use the [- addInteraction:](<uiview/addinteraction(__).md>) method to attach it to one of your views. The delegate object you provide must adopt the [UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md) protocol. Use the methods of that object to provide the contents of the contextual menu. Add your context menu interaction object to a view in your interface using the view’s [- addInteraction:](<uiview/addinteraction(__).md>) method.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UIInteraction](uiinteraction.md)

## Topics

### Creating a context menu interaction object

- [- initWithDelegate:](<uicontextmenuinteraction/init(delegate_).md>) — Creates a context menu interaction object with the specified delegate object.
- [Adding context menus in your app](adding-context-menus-in-your-app.md) — Provide quick access to useful actions by adding context menus to your iOS app.
- [Adding menus and shortcuts to the menu bar and user interface](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md) — Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.

### Previewing and managing the content

- [delegate](uicontextmenuinteraction/delegate.md) — The object that provides the preview and contextual menu for your content and responds to interaction-related events.
- [UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md) — The methods for providing the set of actions to perform on your content, and for customizing the preview of that content.

### Getting the interaction’s location

- [- locationInView:](<uicontextmenuinteraction/location(in_).md>) — Returns the location of the user interaction in the specified view’s coordinate system.

### Getting the menu appearance

- [menuAppearance](uicontextmenuinteraction/menuappearance.md) — The appearance of the context menu.
- [appearance](uicontextmenuinteraction/appearance.md) — Constants that describe the appearance of the menu.

### Managing menu interactions

- [- dismissMenu](<uicontextmenuinteraction/dismissmenu().md>) — Dismisses the context menu.
- [- updateVisibleMenuWithBlock:](<uicontextmenuinteraction/updatevisiblemenu(__).md>) — Updates the currently visible menu.

## See Also

### Contextual menus

- [UIContextMenuSystem](uicontextmenusystem.md) — The context menu system.
- [UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md) — The methods for providing the set of actions to perform on your content, and for customizing the preview of that content.
- [UITargetedPreview](uitargetedpreview.md) — An object describing the view to use during preview-related animations.
- [UIPreviewTarget](uipreviewtarget.md) — An object that specifies the container view to use for animations.
- [UIPreviewParameters](uipreviewparameters.md) — Additional parameters to use when animating a preview interface.
