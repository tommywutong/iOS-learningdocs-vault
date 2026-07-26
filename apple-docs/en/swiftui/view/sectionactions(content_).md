---
title: 'sectionActions(content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/sectionactions(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/sectionactions(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/sectionactions%28content%3A%29.json'
content_hash: 'sha256:e265cc2d822d451c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# sectionActions(content:)

<sub>Instance Method</sub>

Adds custom actions to a section.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func sectionActions<Content>(@ContentBuilder content: () -> Content) -> some View where Content : View

```

## Discussion

On iOS, the actions are displayed as items after the content of the section. On macOS, the actions are displayed when a user hovers over the section.

The following example adds an ‘Add’ button to the ‘Categories’ section.

```swift
List {
    Label("Home", systemImage: "house")
    Label("Alerts", systemImage: "bell")

    Section("Categories") {
        Label("Climate", systemImage: "fan")
        Label("Lights", systemImage: "lightbulb")
    }
    .sectionActions {
        Button("Add Category", systemImage: "plus") { }
    }
}
```

## See Also

### Configuring a tab

- [TabPlacement](../tabplacement.md) — A place that a tab can appear.
- [TabContentBuilder](../tabcontentbuilder.md) — A result builder that constructs tabs for a tab view that supports programmatic selection. This builder requires that all tabs in the tab view have the same selection type.
- [TabContent](../tabcontent.md) — A type that provides content for programmatically selectable tabs in a tab view.
- [AnyTabContent](../anytabcontent.md) — Type erased tab content.
