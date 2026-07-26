---
title: NSSearchToolbarItem
framework: AppKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nssearchtoolbaritem
source_url: 'https://developer.apple.com/documentation/appkit/nssearchtoolbaritem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nssearchtoolbaritem.json'
content_hash: 'sha256:6e649e26bd3752e4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AppKit](../appkit.md)

# NSSearchToolbarItem

<sub>Class</sub>

A toolbar item that contains a search field optimized for performing text-based searches.

<sub>macOS</sub>

```swift
class NSSearchToolbarItem
```

## Overview

[NSSearchToolbarItem](nssearchtoolbaritem.md) automatically resizes to accommodate typing when the focus switches to the toolbar item. When the toolbar is low on space, the system may collapse the search item into a button representation, which then expands to a full search field when the user clicks on it.

## Relationships

- **Inherits From**: [NSToolbarItem](nstoolbaritem.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSMenuItemValidation](nsmenuitemvalidation.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSValidatedUserInterfaceItem](nsvalidateduserinterfaceitem.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Configuring a search item

- [preferredWidthForSearchField](nssearchtoolbaritem/preferredwidthforsearchfield.md) — The preferred width for the toolbar item when it has keyboard focus.
- [resignsFirstResponderWithCancel](nssearchtoolbaritem/resignsfirstresponderwithcancel.md) — A Boolean value that enables the cancel button in the search field to resign the first responder in addition to clearing the contents.
- [searchField](nssearchtoolbaritem/searchfield.md) — The search field inside the toolbar item.

### Controlling search interactions

- [- beginSearchInteraction](<nssearchtoolbaritem/beginsearchinteraction().md>) — Starts a search interaction and moves the keyboard focus to the search field.
- [- endSearchInteraction](<nssearchtoolbaritem/endsearchinteraction().md>) — Ends a search interaction by giving up the first responder and adjusting the size of the search field to the available width for the toolbar item if necessary.

## See Also

### Items

- [NSToolbarItem](nstoolbaritem.md) — A single item that appears in a window’s toolbar.
- [NSToolbarItemGroup](nstoolbaritemgroup.md) — A group of subitems in a toolbar item.
- [ControlRepresentation](nstoolbaritemgroup/controlrepresentation-swift.enum.md)
- [SelectionMode](nstoolbaritemgroup/selectionmode-swift.enum.md) — A value that indicates how a grouped toolbar item selects its subitems.
- [NSMenuToolbarItem](nsmenutoolbaritem.md) — A control that presents a menu in a window’s toolbar.
- [NSTrackingSeparatorToolbarItem](nstrackingseparatortoolbaritem.md) — A toolbar separator that aligns with the vertical split view in the same window.
