---
title: TabSectionExpansion
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/tabsectionexpansion
source_url: 'https://developer.apple.com/documentation/swiftui/tabsectionexpansion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabsectionexpansion.json'
content_hash: 'sha256:4dc625bf6898fa7f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TabSectionExpansion

<sub>Structure</sub>

The default expansion state for a tab section in the sidebar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TabSectionExpansion
```

## Overview

Use this type in conjunction with the [defaultSectionExpansion(_:)](<tabcontent/defaultsectionexpansion(__).md>) modifier.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Tab section expansion options

- [automatic](tabsectionexpansion/automatic.md) — The system determines the default expansion state. _(beta)_
- [collapsed](tabsectionexpansion/collapsed.md) — The section is initially collapsed in the sidebar. _(beta)_
- [expanded](tabsectionexpansion/expanded.md) — The section is initially expanded in the sidebar. _(beta)_

## See Also

### Configuring tab content

- [badge(_:)](<tabcontent/badge(__).md>) — Generates a badge for the tab from a localized string resource.
- [contextMenu(menuItems:)](<tabcontent/contextmenu(menuitems_).md>) — Adds a context menu to a tab.
- [customizationBehavior(_:for:)](<tabcontent/customizationbehavior(__for_).md>) — Configures the customization behavior of customizable tab view content.
- [customizationID(_:)](<tabcontent/customizationid(__).md>) — Sets the identifier for a tab to persist its state.
- [defaultSectionExpansion(_:)](<tabcontent/defaultsectionexpansion(__).md>) — Sets the default expansion state for the section containing this tab when displayed in the sidebar. _(beta)_
- [defaultVisibility(_:for:)](<tabcontent/defaultvisibility(__for_).md>) — Configures the default visibility of a tab in customizable contexts.
- [disabled(_:)](<tabcontent/disabled(__).md>) — Controls whether users can interact with this tab.
- [draggable(_:)](<tabcontent/draggable(__).md>) — Activates this tab as the source of a drag and drop operation. This tab can only be dragged when in the sidebar.
- [dropDestination(for:action:)](<tabcontent/dropdestination(for_action_).md>) — Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [help(_:)](<tabcontent/help(__).md>) — Adds help text to a tab using a text view that you provide. _(beta)_
- [hidden(_:)](<tabcontent/hidden(__).md>) — Hides the tab from the user.
- [popover(isPresented:attachmentAnchor:arrowEdge:content:)](<tabcontent/popover(ispresented_attachmentanchor_arrowedge_content_).md>) — Presents a popover when a given condition is true.
- [popover(item:attachmentAnchor:arrowEdge:content:)](<tabcontent/popover(item_attachmentanchor_arrowedge_content_).md>) — Presents a popover using the given item as a data source for the popover’s content.
- [sectionActions(content:)](<tabcontent/sectionactions(content_).md>) — Adds custom actions to a tab section.
- [springLoadingBehavior(_:)](<tabcontent/springloadingbehavior(__).md>) — Sets the spring loading behavior for the tab.
