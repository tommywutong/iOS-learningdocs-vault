---
title: NSTrackingSeparatorToolbarItem
framework: AppKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nstrackingseparatortoolbaritem
source_url: 'https://developer.apple.com/documentation/appkit/nstrackingseparatortoolbaritem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstrackingseparatortoolbaritem.json'
content_hash: 'sha256:26cb542f8311182f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AppKit](../appkit.md)

# NSTrackingSeparatorToolbarItem

<sub>Class</sub>

A toolbar separator that aligns with the vertical split view in the same window.

<sub>macOS</sub>

```swift
class NSTrackingSeparatorToolbarItem
```

## Overview

Use a `NSTrackingSeparatorToolbarItem` to divide an [NSToolbar](nstoolbar.md) into sections that visually align with the views on either side of the divider of the [splitView](nstrackingseparatortoolbaritem/splitview.md). This keeps [NSToolbarItem](nstoolbaritem.md)s above the content that’s the [target](nstoolbaritem/target.md) for the item’s [target](nstoolbaritem/target.md).

The `splitView` must be in the same window as the toolbar containing this item before showing the toolbar.

## Relationships

- **Inherits From**: [NSToolbarItem](nstoolbaritem.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSMenuItemValidation](nsmenuitemvalidation.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSValidatedUserInterfaceItem](nsvalidateduserinterfaceitem.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a tracking separator

- [+ trackingSeparatorToolbarItemWithIdentifier:splitView:dividerIndex:](<nstrackingseparatortoolbaritem/init(identifier_splitview_dividerindex_).md>) — Creates a new tracking separator toolbar item and configures it to align with the divider of the split view.

### configuring a tracking separator

- [dividerIndex](nstrackingseparatortoolbaritem/dividerindex.md) — The index of the split view divider to align with the tracking separator.
- [splitView](nstrackingseparatortoolbaritem/splitview.md) — The vertical split view to align with the toolbar separator.

## See Also

### Items

- [NSToolbarItem](nstoolbaritem.md) — A single item that appears in a window’s toolbar.
- [NSToolbarItemGroup](nstoolbaritemgroup.md) — A group of subitems in a toolbar item.
- [ControlRepresentation](nstoolbaritemgroup/controlrepresentation-swift.enum.md)
- [SelectionMode](nstoolbaritemgroup/selectionmode-swift.enum.md) — A value that indicates how a grouped toolbar item selects its subitems.
- [NSMenuToolbarItem](nsmenutoolbaritem.md) — A control that presents a menu in a window’s toolbar.
- [NSSearchToolbarItem](nssearchtoolbaritem.md) — A toolbar item that contains a search field optimized for performing text-based searches.
