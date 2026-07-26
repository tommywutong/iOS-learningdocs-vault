---
title: ToolbarItemPlacement
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbaritemplacement
source_url: 'https://developer.apple.com/documentation/swiftui/toolbaritemplacement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbaritemplacement.json'
content_hash: 'sha256:e62cf1082d68b0fc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ToolbarItemPlacement

<sub>Structure</sub>

A structure that defines the placement of a toolbar item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ToolbarItemPlacement
```

## Overview

There are two types of placements:

- Semantic placements, such as [principal](toolbaritemplacement/principal.md) and [navigation](toolbaritemplacement/navigation.md), denote the intent of the item being added. SwiftUI determines the appropriate placement for the item based on this intent and its surrounding context, like the current platform.
- Positional placements, such as [navigationBarLeading](toolbaritemplacement/navigationbarleading.md), denote a precise placement for the item, usually for a particular platform.

In iOS, iPadOS, and macOS, the system uses the space available to the toolbar when determining how many items to render in the toolbar. If not all items fit in the available space, an overflow menu may be created and remaining items placed in that menu.

## Topics

### Getting semantic placement

- [automatic](toolbaritemplacement/automatic.md) — A placement the system positions automatically.
- [principal](toolbaritemplacement/principal.md) — A placement for the principal item section.
- [status](toolbaritemplacement/status.md) — A placement for items that represents a change in status.

### Getting placement for specific actions

- [primaryAction](toolbaritemplacement/primaryaction.md) — A placement for the primary action.
- [secondaryAction](toolbaritemplacement/secondaryaction.md) — A placement for secondary actions.
- [confirmationAction](toolbaritemplacement/confirmationaction.md) — A placement for confirmation actions in a modal interface.
- [cancellationAction](toolbaritemplacement/cancellationaction.md) — A placement for cancellation actions in a modal interface.
- [destructiveAction](toolbaritemplacement/destructiveaction.md) — A placement for destructive actions in a modal interface.
- [navigation](toolbaritemplacement/navigation.md) — A placement for navigation actions.

### Getting explicit placement

- [topBarLeading](toolbaritemplacement/topbarleading.md) — A placement for items in the leading edge of the top bar.
- [topBarTrailing](toolbaritemplacement/topbartrailing.md) — A placement for items in the trailing edge of the top bar.
- [topBarPinnedTrailing](toolbaritemplacement/topbarpinnedtrailing.md) — A placement that pins the item to the trailing edge of the toolbar. _(beta)_
- [bottomBar](toolbaritemplacement/bottombar.md) — A placement for items in the bottom toolbar.
- [bottomOrnament](toolbaritemplacement/bottomornament.md) — A placement for items in an ornament under the window.
- [keyboard](toolbaritemplacement/keyboard.md) — A placement for items in the keyboard section.
- [accessoryBar(id:)](<toolbaritemplacement/accessorybar(id_).md>) — Creates a unique accessory bar placement.

### Deprecated symbols

- [init(id:)](<toolbaritemplacement/init(id_).md>) — Creates a custom accessory bar item placement. _(deprecated)_
- [navigationBarLeading](toolbaritemplacement/navigationbarleading.md) — Places the item in the leading edge of the navigation bar. _(deprecated)_
- [navigationBarTrailing](toolbaritemplacement/navigationbartrailing.md) — Places the item in the trailing edge of the navigation bar. _(deprecated)_

### Type Properties

- [largeSubtitle](toolbaritemplacement/largesubtitle.md) — A placement for items in the navigation bar’s large title subtitle area.
- [largeTitle](toolbaritemplacement/largetitle.md) — A placement for items in the navigation bar’s title area.
- [subtitle](toolbaritemplacement/subtitle.md) — A placement for items in the navigation bar’s inline subtitle area.
- [title](toolbaritemplacement/title.md) — A placement for items in the title area of the navigation bar.

## See Also

### Populating a toolbar

- [toolbar(content:)](<view/toolbar(content_).md>) — Populates the toolbar or navigation bar with the specified items.
- [ToolbarItem](toolbaritem.md) — A model that represents an item which can be placed in the toolbar or navigation bar.
- [ToolbarItemGroup](toolbaritemgroup.md) — A model that represents a group of `ToolbarItem`s which can be placed in the toolbar or navigation bar.
- [toolbarOverflowMenu(content:)](<view/toolbaroverflowmenu(content_).md>) — Configures the overflow menu of a toolbar. _(beta)_
- [ToolbarOverflowMenu](toolbaroverflowmenu.md) — The overflow menu of a toolbar. _(beta)_
- [ToolbarContent](toolbarcontent.md) — Conforming types represent items that can be placed in various locations in a toolbar.
- [ToolbarContentBuilder](toolbarcontentbuilder.md) — Constructs a toolbar item set from multi-expression closures.
- [ToolbarSpacer](toolbarspacer.md) — A standard space item in toolbars.
- [DefaultToolbarItem](defaulttoolbaritem.md) — A toolbar item that represents a system component.
