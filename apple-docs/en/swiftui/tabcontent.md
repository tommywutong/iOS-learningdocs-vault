---
title: TabContent
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tabcontent
source_url: 'https://developer.apple.com/documentation/swiftui/tabcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabcontent.json'
content_hash: 'sha256:b84010923ec38f1e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TabContent

<sub>Protocol</sub>

A type that provides content for programmatically selectable tabs in a tab view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency protocol TabContent<TabValue>
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

- **Conforming Types**: [AnyTabContent](anytabcontent.md), [ForEach](foreach.md), [Group](group.md), [Tab](tab.md), [TabSection](tabsection.md)

## Topics

### Setting tab content

- [body](tabcontent/body-swift.property.md) — The value of this type’s nested content.
- [Body](tabcontent/body-swift.associatedtype.md) — The type of content representing the body of this content type.
- [TabValue](tabcontent/tabvalue.md) — The type used to drive selection for the containing tab view.

### Configuring tab content

- [badge(_:)](<tabcontent/badge(__).md>) — Generates a badge for the tab from a localized string resource.
- [contextMenu(menuItems:)](<tabcontent/contextmenu(menuitems_).md>) — Adds a context menu to a tab.
- [customizationBehavior(_:for:)](<tabcontent/customizationbehavior(__for_).md>) — Configures the customization behavior of customizable tab view content.
- [customizationID(_:)](<tabcontent/customizationid(__).md>) — Sets the identifier for a tab to persist its state.
- [defaultSectionExpansion(_:)](<tabcontent/defaultsectionexpansion(__).md>) — Sets the default expansion state for the section containing this tab when displayed in the sidebar. _(beta)_
- [TabSectionExpansion](tabsectionexpansion.md) — The default expansion state for a tab section in the sidebar. _(beta)_
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
- [swipeActions(edge:allowsFullSwipe:content:)](<tabcontent/swipeactions(edge_allowsfullswipe_content_).md>) — Adds custom swipe actions to a tab in a tab view.
- [tabPlacement(_:)](<tabcontent/tabplacement(__).md>) — Specifies the placement of a tab.
- [TabPlacement](tabplacement.md) — A place that a tab can appear.

### Configuring tab accessibility

- [accessibilityHint(_:isEnabled:)](<tabcontent/accessibilityhint(__isenabled_).md>) — Communicates to the user what happens after selecting the tab.
- [accessibilityIdentifier(_:isEnabled:)](<tabcontent/accessibilityidentifier(__isenabled_).md>) — Uses the string you specify to identify the view. Use this value for testing. It isn’t visible to the user.
- [accessibilityInputLabels(_:isEnabled:)](<tabcontent/accessibilityinputlabels(__isenabled_).md>) — Sets alternate input labels with which users identify a tab.
- [accessibilityLabel(_:isEnabled:)](<tabcontent/accessibilitylabel(__isenabled_).md>) — Adds a label to the tab that describes its contents.
- [accessibilityValue(_:isEnabled:)](<tabcontent/accessibilityvalue(__isenabled_).md>) — Adds a textual description of the value that the tab contains.

## See Also

### Configuring a tab

- [sectionActions(content:)](<view/sectionactions(content_).md>) — Adds custom actions to a section.
- [TabPlacement](tabplacement.md) — A place that a tab can appear.
- [TabContentBuilder](tabcontentbuilder.md) — A result builder that constructs tabs for a tab view that supports programmatic selection. This builder requires that all tabs in the tab view have the same selection type.
- [AnyTabContent](anytabcontent.md) — Type erased tab content.
