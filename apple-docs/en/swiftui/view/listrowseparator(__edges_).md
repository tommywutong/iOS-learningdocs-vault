---
title: 'listRowSeparator(_:edges:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/listrowseparator(_:edges:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/listrowseparator(_:edges:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/listrowseparator%28_%3Aedges%3A%29.json'
content_hash: 'sha256:f11dfcfa91b3b926'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# listRowSeparator(_:edges:)

<sub>Instance Method</sub>

Sets the display mode for the separator associated with this specific row.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func listRowSeparator(_ visibility: Visibility, edges: VerticalEdge.Set = .all) -> some View

```

## Parameters

- `visibility` — The visibility of this row’s separators.

- `edges` — The set of row edges for which this preference applies. The list style might already decide to not display separators for some edges, typically the top edge. The default is [all](../verticaledge/set/all.md).

## Discussion

Separators can be presented above and below a row. You can specify to which edge this preference should apply.

This modifier expresses a preference to the containing [List](../list.md). The list style is the final arbiter of the separator visibility.

The following example shows a simple grouped list whose row separators are hidden:

```swift
List {
    ForEach(garage.cars) { car in
        Text(car.model)
            .listRowSeparator(.hidden)
    }
}
.listStyle(.grouped)
```

To change the color of a row separators, use [listRowSeparatorTint(_:edges:)](<listrowseparatortint(__edges_).md>). To hide or change the tint color for a section separators, use [listSectionSeparator(_:edges:)](<listsectionseparator(__edges_).md>) and [listSectionSeparatorTint(_:edges:)](<listsectionseparatortint(__edges_).md>).

## See Also

### Configuring separators

- [listRowSeparatorTint(_:edges:)](<listrowseparatortint(__edges_).md>) — Sets the tint color associated with a row.
- [listSectionSeparatorTint(_:edges:)](<listsectionseparatortint(__edges_).md>) — Sets the tint color associated with a section.
- [listSectionSeparator(_:edges:)](<listsectionseparator(__edges_).md>) — Sets whether to hide the separator associated with a list section.
