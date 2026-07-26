---
title: CustomizableToolbarContent
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/customizabletoolbarcontent
source_url: 'https://developer.apple.com/documentation/swiftui/customizabletoolbarcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/customizabletoolbarcontent.json'
content_hash: 'sha256:725275ab2a982166'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# CustomizableToolbarContent

<sub>Protocol</sub>

Conforming types represent items that can be placed in various locations in a customizable toolbar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol CustomizableToolbarContent : ToolbarContent where Self.Body : CustomizableToolbarContent
```

## Relationships

- **Inherits From**: [ToolbarContent](toolbarcontent.md)

- **Conforming Types**: [EmptyView](emptyview.md), [ForEach](foreach.md), [Group](group.md), [ToolbarItem](toolbaritem.md), [ToolbarOverflowMenu](toolbaroverflowmenu.md), [ToolbarSpacer](toolbarspacer.md), [ToolbarTitleMenu](toolbartitlemenu.md), [TupleContent](tuplecontent.md)

## Topics

### Using default options

- [defaultCustomization()](<customizabletoolbarcontent/defaultcustomization().md>) — Configures customizable toolbar content with the default visibility and options. _(deprecated)_
- [defaultCustomization(_:options:)](<customizabletoolbarcontent/defaultcustomization(__options_).md>) — Configures the way customizable toolbar items with the default behavior behave.

### Customizing the behavior

- [customizationBehavior(_:)](<customizabletoolbarcontent/customizationbehavior(__).md>) — Configures the customization behavior of customizable toolbar content.

### Setting visibility

- [visibilityPriority(_:)](<customizabletoolbarcontent/visibilitypriority(__).md>) — Defines the visibility priority for a toolbar item.

### Instance Methods

- [contentMarginsRemoved(_:)](<customizabletoolbarcontent/contentmarginsremoved(__).md>) — Configures whether the content margins are removed. _(beta)_
- [hidden(_:)](<customizabletoolbarcontent/hidden(__).md>) — Hides a toolbar item within its toolbar.
- [matchedTransitionSource(id:in:)](<customizabletoolbarcontent/matchedtransitionsource(id_in_).md>) — Identifies this toolbar content as the source of a navigation transition, such as a zoom transition.
- [sharedBackgroundVisibility(_:)](<customizabletoolbarcontent/sharedbackgroundvisibility(__).md>) — Controls the visibility of the glass background effect on items in the toolbar. In certain contexts, such as the navigation bar on iOS and the window toolbar on macOS, toolbar items will be given a glass background effect that is shared with other items in the same logical grouping.

## See Also

### Populating a customizable toolbar

- [toolbar(id:content:)](<view/toolbar(id_content_).md>) — Populates the toolbar or navigation bar with the specified items, allowing for user customization.
- [toolbarItemHidden(_:)](<view/toolbaritemhidden(__).md>) — Hides an individual view within a control group toolbar item.
- [ToolbarCustomizationBehavior](toolbarcustomizationbehavior.md) — The customization behavior of customizable toolbar content.
- [ToolbarCustomizationOptions](toolbarcustomizationoptions.md) — Options that influence the default customization behavior of customizable toolbar content.
- [SearchToolbarBehavior](searchtoolbarbehavior.md) — The behavior of a search field in a toolbar.
