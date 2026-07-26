---
title: ToolbarContentBuilder
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbarcontentbuilder
source_url: 'https://developer.apple.com/documentation/swiftui/toolbarcontentbuilder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbarcontentbuilder.json'
content_hash: 'sha256:e2c70fd307a0440b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ToolbarContentBuilder

<sub>Structure</sub>

Constructs a toolbar item set from multi-expression closures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@resultBuilder struct ToolbarContentBuilder
```

## Topics

### Building toolbar content

- [buildBlock(_:)](<toolbarcontentbuilder/buildblock(__).md>)
- [buildBlock(_:_:)](<toolbarcontentbuilder/buildblock(____).md>)
- [buildBlock(_:_:_:)](<toolbarcontentbuilder/buildblock(______).md>)
- [buildBlock(_:_:_:_:)](<toolbarcontentbuilder/buildblock(________).md>)
- [buildBlock(_:_:_:_:_:)](<toolbarcontentbuilder/buildblock(__________).md>)
- [buildBlock(_:_:_:_:_:_:)](<toolbarcontentbuilder/buildblock(____________).md>)
- [buildBlock(_:_:_:_:_:_:_:)](<toolbarcontentbuilder/buildblock(______________).md>)
- [buildBlock(_:_:_:_:_:_:_:_:)](<toolbarcontentbuilder/buildblock(________________).md>)
- [buildBlock(_:_:_:_:_:_:_:_:_:)](<toolbarcontentbuilder/buildblock(__________________).md>)
- [buildBlock(_:_:_:_:_:_:_:_:_:_:)](<toolbarcontentbuilder/buildblock(____________________).md>)

### Building conditional toolbar content

- [buildIf(_:)](<toolbarcontentbuilder/buildif(__).md>)
- [buildEither(first:)](<toolbarcontentbuilder/buildeither(first_).md>)
- [buildEither(second:)](<toolbarcontentbuilder/buildeither(second_).md>)
- [buildExpression(_:)](<toolbarcontentbuilder/buildexpression(__).md>) — Builds an expression within the builder.
- [buildLimitedAvailability(_:)](<toolbarcontentbuilder/buildlimitedavailability(__).md>)

## See Also

### Populating a toolbar

- [toolbar(content:)](<view/toolbar(content_).md>) — Populates the toolbar or navigation bar with the specified items.
- [ToolbarItem](toolbaritem.md) — A model that represents an item which can be placed in the toolbar or navigation bar.
- [ToolbarItemGroup](toolbaritemgroup.md) — A model that represents a group of `ToolbarItem`s which can be placed in the toolbar or navigation bar.
- [ToolbarItemPlacement](toolbaritemplacement.md) — A structure that defines the placement of a toolbar item.
- [toolbarOverflowMenu(content:)](<view/toolbaroverflowmenu(content_).md>) — Configures the overflow menu of a toolbar. _(beta)_
- [ToolbarOverflowMenu](toolbaroverflowmenu.md) — The overflow menu of a toolbar. _(beta)_
- [ToolbarContent](toolbarcontent.md) — Conforming types represent items that can be placed in various locations in a toolbar.
- [ToolbarSpacer](toolbarspacer.md) — A standard space item in toolbars.
- [DefaultToolbarItem](defaulttoolbaritem.md) — A toolbar item that represents a system component.
