---
title: ToolbarContent
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbarcontent
source_url: 'https://developer.apple.com/documentation/swiftui/toolbarcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbarcontent.json'
content_hash: 'sha256:7abd64f56846787f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ToolbarContent

<sub>Protocol</sub>

Conforming types represent items that can be placed in various locations in a toolbar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency protocol ToolbarContent
```

## Overview

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Relationships

- **Inherited By**: [CustomizableToolbarContent](customizabletoolbarcontent.md)

- **Conforming Types**: [DefaultToolbarItem](defaulttoolbaritem.md), [EmptyView](emptyview.md), [ForEach](foreach.md), [Group](group.md), [ToolbarItem](toolbaritem.md), [ToolbarItemGroup](toolbaritemgroup.md), [ToolbarOverflowMenu](toolbaroverflowmenu.md), [ToolbarSpacer](toolbarspacer.md), [ToolbarTitleMenu](toolbartitlemenu.md), [TupleContent](tuplecontent.md)

## Topics

### Implementing toolbar content

- [body](toolbarcontent/body-swift.property.md) — The composition of content that comprise the toolbar content.
- [Body](toolbarcontent/body-swift.associatedtype.md) — The type of content representing the body of this toolbar content.

### Setting visibility

- [visibilityPriority(_:)](<toolbarcontent/visibilitypriority(__).md>) — Defines the visibility priority for a toolbar item.

### Instance Methods

- [contentMarginsRemoved(_:)](<toolbarcontent/contentmarginsremoved(__).md>) — Configures whether the content margins are removed. _(beta)_
- [hidden(_:)](<toolbarcontent/hidden(__).md>) — Hides a toolbar item within its toolbar.
- [matchedTransitionSource(id:in:)](<toolbarcontent/matchedtransitionsource(id_in_).md>) — Identifies this toolbar content as the source of a navigation transition, such as a zoom transition.
- [sharedBackgroundVisibility(_:)](<toolbarcontent/sharedbackgroundvisibility(__).md>) — Controls the visibility of the glass background effect on items in the toolbar. In certain contexts, such as the navigation bar on iOS and the window toolbar on macOS, toolbar items will be given a glass background effect that is shared with other items in the same logical grouping.

## See Also

### Populating a toolbar

- [toolbar(content:)](<view/toolbar(content_).md>) — Populates the toolbar or navigation bar with the specified items.
- [ToolbarItem](toolbaritem.md) — A model that represents an item which can be placed in the toolbar or navigation bar.
- [ToolbarItemGroup](toolbaritemgroup.md) — A model that represents a group of `ToolbarItem`s which can be placed in the toolbar or navigation bar.
- [ToolbarItemPlacement](toolbaritemplacement.md) — A structure that defines the placement of a toolbar item.
- [toolbarOverflowMenu(content:)](<view/toolbaroverflowmenu(content_).md>) — Configures the overflow menu of a toolbar. _(beta)_
- [ToolbarOverflowMenu](toolbaroverflowmenu.md) — The overflow menu of a toolbar. _(beta)_
- [ToolbarContentBuilder](toolbarcontentbuilder.md) — Constructs a toolbar item set from multi-expression closures.
- [ToolbarSpacer](toolbarspacer.md) — A standard space item in toolbars.
- [DefaultToolbarItem](defaulttoolbaritem.md) — A toolbar item that represents a system component.
