---
title: DisclosureGroup
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/disclosuregroup
source_url: 'https://developer.apple.com/documentation/swiftui/disclosuregroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/disclosuregroup.json'
content_hash: 'sha256:0d8d447acbdfcb19'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DisclosureGroup

<sub>Structure</sub>

A view that shows or hides another content view, based on the state of a disclosure control.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated struct DisclosureGroup<Label, Content> where Label : View, Content : View
```

## Overview

A disclosure group view consists of a label to identify the contents, and a control to show and hide the contents. Showing the contents puts the disclosure group into the “expanded” state, and hiding them makes the disclosure group “collapsed”.

In the following example, a disclosure group contains two toggles and an embedded disclosure group. The top level disclosure group exposes its expanded state with the bound property, `topLevelExpanded`. By expanding the disclosure group, the user can use the toggles to update the state of the `toggleStates` structure.

```swift
struct ToggleStates {
    var oneIsOn: Bool = false
    var twoIsOn: Bool = true
}
@State private var toggleStates = ToggleStates()
@State private var topExpanded: Bool = true

var body: some View {
    DisclosureGroup("Items", isExpanded: $topExpanded) {
        Toggle("Toggle 1", isOn: $toggleStates.oneIsOn)
        Toggle("Toggle 2", isOn: $toggleStates.twoIsOn)
        DisclosureGroup("Sub-items") {
            Text("Sub-item 1")
        }
    }
}
```

## Relationships

- **Conforms To**: [View](view.md)

## Topics

### Creating a disclosure group

- [init(_:content:)](<disclosuregroup/init(__content_).md>) — Creates a disclosure group, using a provided localized string resource to create a text view for the label.
- [init(content:label:)](<disclosuregroup/init(content_label_).md>) — Creates a disclosure group with the given label and content views.
- [init(_:isExpanded:content:)](<disclosuregroup/init(__isexpanded_content_).md>) — Creates a disclosure group, using a provided localized string resource to create a text view for the label, and a binding to the expansion state (expanded or collapsed).
- [init(isExpanded:content:label:)](<disclosuregroup/init(isexpanded_content_label_).md>) — Creates a disclosure group with the given label and content views, and a binding to the expansion state (expanded or collapsed).

## See Also

### Disclosing information progressively

- [OutlineGroup](outlinegroup.md) — A structure that computes views and disclosure groups on demand from an underlying collection of tree-structured, identified data.
- [disclosureGroupStyle(_:)](<view/disclosuregroupstyle(__).md>) — Sets the style for disclosure groups within this view.
