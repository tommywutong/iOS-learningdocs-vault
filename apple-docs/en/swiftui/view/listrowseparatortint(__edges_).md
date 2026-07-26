---
title: 'listRowSeparatorTint(_:edges:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/listrowseparatortint(_:edges:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/listrowseparatortint(_:edges:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/listrowseparatortint%28_%3Aedges%3A%29.json'
content_hash: 'sha256:545424503a399f23'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# listRowSeparatorTint(_:edges:)

<sub>Instance Method</sub>

Sets the tint color associated with a row.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func listRowSeparatorTint(_ color: Color?, edges: VerticalEdge.Set = .all) -> some View

```

## Parameters

- `color` — The color to use to tint the row separators, or `nil` to use the default color for the current list style.

- `edges` — The set of row edges for which the tint applies. The list style might decide to not display certain separators, typically the top edge. The default is [all](../verticaledge/set/all.md).

## Discussion

Separators can be presented above and below a row. You can specify to which edge this preference should apply.

This modifier expresses a preference to the containing [List](../list.md). The list style is the final arbiter for the separator tint.

The following example shows a simple grouped list whose row separators are tinted based on row-specific data:

```swift
List {
    ForEach(garage.cars) { car in
        Text(car.model)
            .listRowSeparatorTint(car.brandColor)
    }
}
.listStyle(.grouped)
```

To hide a row separators, use [listRowSeparator(_:edges:)](<listrowseparator(__edges_).md>). To hide or change the tint color for a section separator, use [listSectionSeparator(_:edges:)](<listsectionseparator(__edges_).md>) and [listSectionSeparatorTint(_:edges:)](<listsectionseparatortint(__edges_).md>).

## See Also

### Configuring separators

- [listSectionSeparatorTint(_:edges:)](<listsectionseparatortint(__edges_).md>) — Sets the tint color associated with a section.
- [listRowSeparator(_:edges:)](<listrowseparator(__edges_).md>) — Sets the display mode for the separator associated with this specific row.
- [listSectionSeparator(_:edges:)](<listsectionseparator(__edges_).md>) — Sets whether to hide the separator associated with a list section.
