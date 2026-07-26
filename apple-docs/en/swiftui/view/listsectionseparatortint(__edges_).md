---
title: 'listSectionSeparatorTint(_:edges:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/listsectionseparatortint(_:edges:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/listsectionseparatortint(_:edges:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/listsectionseparatortint%28_%3Aedges%3A%29.json'
content_hash: 'sha256:9a95e690a197f3db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# listSectionSeparatorTint(_:edges:)

<sub>Instance Method</sub>

Sets the tint color associated with a section.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func listSectionSeparatorTint(_ color: Color?, edges: VerticalEdge.Set = .all) -> some View

```

## Parameters

- `color` — The color to use to tint the section separators, or `nil` to use the default color for the current list style.

- `edges` — The set of row edges for which the tint applies. The list style might decide to not display certain separators, typically the top edge. The default is [all](../verticaledge/set/all.md).

## Discussion

Separators can be presented above and below a section. You can specify to which edge this preference should apply.

This modifier expresses a preference to the containing [List](../list.md). The list style is the final arbiter for the separator tint.

The following example shows a simple grouped list whose section separators are tinted based on section-specific data:

```swift
List {
    ForEach(garage) { garage in
        Section(header: Text(garage.location)) {
            ForEach(garage.cars) { car in
                Text(car.model)
                    .listRowSeparatorTint(car.brandColor)
            }
        }
        .listSectionSeparatorTint(
            garage.cars.last?.brandColor, edges: .bottom)
    }
}
.listStyle(.grouped)
```

To change the visibility and tint color for a row separator, use [listRowSeparator(_:edges:)](<listrowseparator(__edges_).md>) and [listRowSeparatorTint(_:edges:)](<listrowseparatortint(__edges_).md>). To hide a section separator, use [listSectionSeparator(_:edges:)](<listsectionseparator(__edges_).md>).

## See Also

### Configuring separators

- [listRowSeparatorTint(_:edges:)](<listrowseparatortint(__edges_).md>) — Sets the tint color associated with a row.
- [listRowSeparator(_:edges:)](<listrowseparator(__edges_).md>) — Sets the display mode for the separator associated with this specific row.
- [listSectionSeparator(_:edges:)](<listsectionseparator(__edges_).md>) — Sets whether to hide the separator associated with a list section.
