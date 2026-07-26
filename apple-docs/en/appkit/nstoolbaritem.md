---
title: NSToolbarItem
framework: AppKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nstoolbaritem
source_url: 'https://developer.apple.com/documentation/appkit/nstoolbaritem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstoolbaritem.json'
content_hash: 'sha256:f1c9e0d54ea0d94a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AppKit](../appkit.md)

# NSToolbarItem

<sub>Class</sub>

A single item that appears in a window’s toolbar.

<sub>Mac Catalyst, macOS</sub>

```swift
@MainActor class NSToolbarItem
```

## Overview

An [NSToolbarItem](nstoolbaritem.md) object displays an image and text string in the toolbar area of a window. You can also create toolbar items that display custom views you provide. Toolbar items provide fast access to common commands or features in the window. For example, the Finder window uses toolbar items to help someone navigate the file system.

You typically create toolbar items at the same time you create your window’s toolbar. The system provides some standard items like spacers you can include in your toolbar. It also provides items that display standard interfaces like the color panel or font panel. For any custom toolbar items you create, provide an action method to call when someone clicks the item.

You can display your toolbar item’s content using a custom view if you prefer, rather than an image and text label. If you specify an [NSSearchField](nssearchfield.md) object for the view, the system automatically adjusts the minimum and maximum size of the search field to the system-standard values.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [NSMenuToolbarItem](nsmenutoolbaritem.md), [NSSearchToolbarItem](nssearchtoolbaritem.md), [NSSharingServicePickerToolbarItem](nssharingservicepickertoolbaritem.md), [NSToolbarItemGroup](nstoolbaritemgroup.md), [NSTrackingSeparatorToolbarItem](nstrackingseparatortoolbaritem.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSMenuItemValidation](nsmenuitemvalidation.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSValidatedUserInterfaceItem](nsvalidateduserinterfaceitem.md), [Sendable](../swift/sendable.md), [UIPopoverPresentationControllerSourceItem](../uikit/uipopoverpresentationcontrollersourceitem.md)

## Topics

### Creating a toolbar item

- [- initWithItemIdentifier:](<nstoolbaritem/init(itemidentifier_).md>) — Creates a toolbar item with the specified identifier.
- [+ itemWithItemIdentifier:barButtonItem:](<nstoolbaritem/init(itemidentifier_barbuttonitem_).md>) — Creates a toolbar item with property values from the specified bar button item.

### Getting the toolbar item’s identity

- [itemIdentifier](nstoolbaritem/itemidentifier.md) — The value you use to identify the toolbar item.
- [Identifier](nstoolbaritem/identifier.md) — Constants for the standard toolbar items that the system provides.

### Describing the item

- [possibleLabels](nstoolbaritem/possiblelabels.md) — The set of labels that the item might display.
- [label](nstoolbaritem/label.md) — The label that appears for this item in the toolbar.
- [paletteLabel](nstoolbaritem/palettelabel.md) — The label that appears when the toolbar item is in the customization palette.
- [title](nstoolbaritem/title.md) — The title of the toolbar item.
- [toolTip](nstoolbaritem/tooltip.md) — The tooltip to display when someone hovers over the item in the toolbar.

### Getting the item’s visual appearance

- [image](nstoolbaritem/image.md) — The image to display for the toolbar item.
- [backgroundTintColor](nstoolbaritem/backgroundtintcolor.md)
- [view](nstoolbaritem/view.md) — The custom view you use to draw the toolbar item.

### Performing the item’s action

- [target](nstoolbaritem/target.md) — The object that defines the action method the toolbar item calls when clicked.
- [action](nstoolbaritem/action.md) — The action method to call when someone clicks on the toolbar item.

### Configuring the item’s menu

- [menuFormRepresentation](nstoolbaritem/menuformrepresentation.md) — The menu item to use when the toolbar item is in the overflow menu.
- [itemMenuFormRepresentation](nstoolbaritem/itemmenuformrepresentation.md) — The menu item to use for the toolbar item is in the overflow menu in a Mac app built with Mac Catalyst.

### Getting the item’s configuration

- [visible](nstoolbaritem/isvisible.md) — A Boolean value that indicates whether the item is currently visible in the toolbar, and not in the overflow menu.
- [hidden](nstoolbaritem/ishidden.md) — Determines whether an item is visible in the toolbar.
- [bordered](nstoolbaritem/isbordered.md) — A Boolean value that indicates whether the toolbar item has a bordered style.
- [navigational](nstoolbaritem/isnavigational.md) — A Boolean value that indicates whether the item behaves as a navigation item in the toolbar.
- [enabled](nstoolbaritem/isenabled.md) — A Boolean value that indicates whether the item is enabled.
- [badge](nstoolbaritem/badge-17r3r.md) — A badge that can be attached to an NSToolbarItem. This provides a way to display small visual indicators that can be used to highlight important information, such as unread notifications or status indicators.
- [NSItemBadge](nsitembadge-swift.struct.md) — `NSItemBadge` represents a badge that can be attached to an `NSToolbarItem`.
- [style](nstoolbaritem/style-swift.property.md) — Defines the toolbar item’s appearance. The default style is plain. Prominent style tints the background. If a background tint color is set, it uses it; otherwise, it uses the app’s or system’s accent color. If grouped with other items, it moves to its own to avoid tinting other items’ background.
- [Style](nstoolbaritem/style-swift.enum.md)
- [visibilityPriority](nstoolbaritem/visibilitypriority-swift.property.md) — The display priority associated with the toolbar item.
- [VisibilityPriority](nstoolbaritem/visibilitypriority-swift.struct.md) — Constants that indicate which toolbar items to keep in the toolbar when space is limited.
- [tag](nstoolbaritem/tag.md) — An integer tag you can use to identify the toolbar item.

### Getting the parent toolbar

- [toolbar](nstoolbaritem/toolbar.md) — The toolbar that currently includes the item.

### Validating the item

- [autovalidates](nstoolbaritem/autovalidates.md) — A Boolean value that indicates whether the toolbar automatically validates the item.
- [- validate](<nstoolbaritem/validate().md>) — Validates the toolbar item’s menu and its ability to perfrom its action.

### Deprecated

- [allowsDuplicatesInToolbar](nstoolbaritem/allowsduplicatesintoolbar.md) — A Boolean value that indicates whether the toolbar item can appear more than once in a toolbar. _(deprecated)_
- [minSize](nstoolbaritem/minsize.md) — The toolbar item’s minimum size. _(deprecated)_
- [maxSize](nstoolbaritem/maxsize.md) — The toolbar item’s maximum size. _(deprecated)_

## See Also

### Items

- [NSToolbarItemGroup](nstoolbaritemgroup.md) — A group of subitems in a toolbar item.
- [ControlRepresentation](nstoolbaritemgroup/controlrepresentation-swift.enum.md)
- [SelectionMode](nstoolbaritemgroup/selectionmode-swift.enum.md) — A value that indicates how a grouped toolbar item selects its subitems.
- [NSMenuToolbarItem](nsmenutoolbaritem.md) — A control that presents a menu in a window’s toolbar.
- [NSSearchToolbarItem](nssearchtoolbaritem.md) — A toolbar item that contains a search field optimized for performing text-based searches.
- [NSTrackingSeparatorToolbarItem](nstrackingseparatortoolbaritem.md) — A toolbar separator that aligns with the vertical split view in the same window.
