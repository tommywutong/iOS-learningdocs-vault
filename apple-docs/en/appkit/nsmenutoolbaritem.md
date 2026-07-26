---
title: NSMenuToolbarItem
framework: AppKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsmenutoolbaritem
source_url: 'https://developer.apple.com/documentation/appkit/nsmenutoolbaritem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsmenutoolbaritem.json'
content_hash: 'sha256:7cbf5b9fbdd08f34'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AppKit](../appkit.md)

# NSMenuToolbarItem

<sub>Class</sub>

A control that presents a menu in a window’s toolbar.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSMenuToolbarItem
```

## Overview

If you set an action on an [NSMenuToolbarItem](nsmenutoolbaritem.md) control item, the user invokes the action when clicking on the item through pressing and holding to display the menu. If you set an action on the item and [showsIndicator](nsmenutoolbaritem/showsindicator.md) to [true](../swift/true.md), the system displays the indicator as a separate segment so the user can invoke the menu with a click on that segment.

If you don’t set an action on the [NSMenuToolbarItem](nsmenutoolbaritem.md), a simple click invokes the menu, and the indicator is purely decorative.

## Relationships

- **Inherits From**: [NSToolbarItem](nstoolbaritem.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSMenuItemValidation](nsmenuitemvalidation.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSValidatedUserInterfaceItem](nsvalidateduserinterfaceitem.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Configuring a menu toolbar item

- [showsIndicator](nsmenutoolbaritem/showsindicator.md) — A Boolean value that determines whether the toolbar item displays an indicator of additional functionality.
- [menu](nsmenutoolbaritem/menu.md) — The menu presented from the toolbar item.
- [itemMenu](nsmenutoolbaritem/itemmenu.md)

## See Also

### Items

- [NSToolbarItem](nstoolbaritem.md) — A single item that appears in a window’s toolbar.
- [NSToolbarItemGroup](nstoolbaritemgroup.md) — A group of subitems in a toolbar item.
- [ControlRepresentation](nstoolbaritemgroup/controlrepresentation-swift.enum.md)
- [SelectionMode](nstoolbaritemgroup/selectionmode-swift.enum.md) — A value that indicates how a grouped toolbar item selects its subitems.
- [NSSearchToolbarItem](nssearchtoolbaritem.md) — A toolbar item that contains a search field optimized for performing text-based searches.
- [NSTrackingSeparatorToolbarItem](nstrackingseparatortoolbaritem.md) — A toolbar separator that aligns with the vertical split view in the same window.
