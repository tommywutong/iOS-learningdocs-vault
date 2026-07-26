---
title: NSToolbarItemGroup
framework: AppKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nstoolbaritemgroup
source_url: 'https://developer.apple.com/documentation/appkit/nstoolbaritemgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstoolbaritemgroup.json'
content_hash: 'sha256:feedfa530f098ae4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AppKit](../appkit.md)

# NSToolbarItemGroup

<sub>Class</sub>

A group of subitems in a toolbar item.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSToolbarItemGroup
```

## Overview

An [NSToolbarItemGroup](nstoolbaritemgroup.md) represents a collection set of subitems in a toolbar that the system displays based on available space and settings that you specify. The system uses the views and labels of the subitems, but the parent’s attributes take precedence. This differs from other [NSToolbarItem](nstoolbaritem.md) objects because they’re attached — the user drags them together as a single item rather than separately.

If a subitem of the group has an action set on it, the group uses that action instead of its own when the user clicks or taps on that item. The system prefers the subitem’s action if it exists, otherwise it uses the group’s action.

To configure an instance of [NSToolbarItemGroup](nstoolbaritemgroup.md), you first create the individual toolbar subitems:

```objc
NSToolbarItem *item1 = [[NSToolbarItem alloc] initWithItemIdentifier:@"Item1"];
NSToolbarItem *item2 = [[NSToolbarItem alloc] initWithItemIdentifier:@"Item2"];
[item1 setImage:[NSImage imageNamed:@"LeftArrow"]];
[item2 setImage:[NSImage imageNamed:@"RightArrow"]];
[item1 setLabel:@"Prev"];
[item2 setLabel:@"Next"];
```

Then, you put them in a grouped item:

```objc
NSToolbarItemGroup *group = [[NSToolbarItemGroup alloc] initWithItemIdentifier:@"GroupItem"];
[group setSubitems:[NSArray arrayWithObjects:item1, item2, nil]];
```

In this configuration, you get two grouped items, and two labels.

If you set a label on the parent item, you get two grouped items with one shared label:

```objc
[group setLabel:@"Navigate"];
```

If instead you set a view on the parent item, you get two labels with one shared view:

```objc
[group setView:someSegmentedControl];
```

## Relationships

- **Inherits From**: [NSToolbarItem](nstoolbaritem.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSMenuItemValidation](nsmenuitemvalidation.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSValidatedUserInterfaceItem](nsvalidateduserinterfaceitem.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating grouped toolbar items

- [+ groupWithItemIdentifier:images:selectionMode:labels:target:action:](<nstoolbaritemgroup/init(itemidentifier_images_selectionmode_labels_target_action_).md>) — Creates a grouped toolbar item with images.
- [+ groupWithItemIdentifier:titles:selectionMode:labels:target:action:](<nstoolbaritemgroup/init(itemidentifier_titles_selectionmode_labels_target_action_).md>) — Creates a grouped toolbar item with labels.

### Working with subitems

- [subitems](nstoolbaritemgroup/subitems.md) — The subitems of the grouped toolbar item.
- [selectedIndex](nstoolbaritemgroup/selectedindex.md) — The index value for the most recently selected subitem of a grouped toolbar item.
- [- isSelectedAtIndex:](<nstoolbaritemgroup/isselected(at_).md>) — Indicates whether a specified index is currently selected.
- [- setSelected:atIndex:](<nstoolbaritemgroup/setselected(__at_).md>) — Sets the selected state of a subitem in a grouped toolbar item.

### Configuring grouped toolbar items

- [controlRepresentation](nstoolbaritemgroup/controlrepresentation-swift.property.md) — A value that represents how a toolbar displays a grouped toolbar item.
- [ControlRepresentation](nstoolbaritemgroup/controlrepresentation-swift.enum.md)
- [selectionMode](nstoolbaritemgroup/selectionmode-swift.property.md) — The selection mode of the grouped toolbar item.
- [SelectionMode](nstoolbaritemgroup/selectionmode-swift.enum.md) — A value that indicates how a grouped toolbar item selects its subitems.

### Instance Properties

- [role](nstoolbaritemgroup/role-swift.property.md) — The semantic role of the item. Defaults to `NSToolbarItemGroupRoleAutomatic`.

### Enumerations

- [Role](nstoolbaritemgroup/role-swift.enum.md) _(beta)_

## See Also

### Items

- [NSToolbarItem](nstoolbaritem.md) — A single item that appears in a window’s toolbar.
- [ControlRepresentation](nstoolbaritemgroup/controlrepresentation-swift.enum.md)
- [SelectionMode](nstoolbaritemgroup/selectionmode-swift.enum.md) — A value that indicates how a grouped toolbar item selects its subitems.
- [NSMenuToolbarItem](nsmenutoolbaritem.md) — A control that presents a menu in a window’s toolbar.
- [NSSearchToolbarItem](nssearchtoolbaritem.md) — A toolbar item that contains a search field optimized for performing text-based searches.
- [NSTrackingSeparatorToolbarItem](nstrackingseparatortoolbaritem.md) — A toolbar separator that aligns with the vertical split view in the same window.
