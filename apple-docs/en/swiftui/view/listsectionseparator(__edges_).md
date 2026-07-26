---
title: 'listSectionSeparator(_:edges:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/listsectionseparator(_:edges:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/listsectionseparator(_:edges:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/listsectionseparator%28_%3Aedges%3A%29.json'
content_hash: 'sha256:da7ec013d79f47fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# listSectionSeparator(_:edges:)

<sub>Instance Method</sub>

Sets whether to hide the separator associated with a list section.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func listSectionSeparator(_ visibility: Visibility, edges: VerticalEdge.Set = .all) -> some View

```

## Parameters

- `visibility` — The visibility of this section’s separators.

- `edges` — The set of row edges for which the preference applies. The list style might already decide to not display separators for some edges. The default is [all](../verticaledge/set/all.md).

## Discussion

Separators can be presented above and below a section. You can specify to which edge this preference should apply.

This modifier expresses a preference to the containing [List](../list.md). The list style is the final arbiter of the separator visibility.

The following example shows a simple grouped list whose bottom sections separator are hidden:

```swift
List {
    ForEach(garage) { garage in
        Section(header: Text(garage.location)) {
            ForEach(garage.cars) { car in
                Text(car.model)
                    .listRowSeparatorTint(car.brandColor)
            }
        }
        .listSectionSeparator(.hidden, edges: .bottom)
    }
}
.listStyle(.grouped)
```

To change the visibility and tint color for a row separator, use [listRowSeparator(_:edges:)](<listrowseparator(__edges_).md>) and [listRowSeparatorTint(_:edges:)](<listrowseparatortint(__edges_).md>). To set the tint color for a section separator, use [listSectionSeparatorTint(_:edges:)](<listsectionseparatortint(__edges_).md>).

## See Also

### Configuring separators

- [listRowSeparatorTint(_:edges:)](<listrowseparatortint(__edges_).md>) — Sets the tint color associated with a row.
- [listSectionSeparatorTint(_:edges:)](<listsectionseparatortint(__edges_).md>) — Sets the tint color associated with a section.
- [listRowSeparator(_:edges:)](<listrowseparator(__edges_).md>) — Sets the display mode for the separator associated with this specific row.
