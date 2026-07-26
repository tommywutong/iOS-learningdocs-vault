---
title: listRowSeparatorLeading
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/horizontalalignment/listrowseparatorleading
source_url: 'https://developer.apple.com/documentation/swiftui/horizontalalignment/listrowseparatorleading'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/horizontalalignment/listrowseparatorleading.json'
content_hash: 'sha256:8cf9fdd9864d0d98'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [HorizontalAlignment](../horizontalalignment.md)

# listRowSeparatorLeading

<sub>Type Property</sub>

A guide marking the leading edge of a `List` row separator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let listRowSeparatorLeading: HorizontalAlignment
```

## Discussion

Use this guide to align the leading end of the bottom `List` row separator with any other horizontal guide of a view that is part of the cell content.

The following example shows the row separator aligned with the leading edge of the `Text` containing the name of food:

```swift
List {
    ForEach(favoriteFoods) { food in
        HStack {
            Text(food.emoji)
                .font(.system(size: 40))
            Text(food.name)
                .alignmentGuide(.listRowSeparatorLeading) {
                    $0[.leading]
                }
        }
    }
}
```

To change the visibility or tint of the row separator use respectively [listRowSeparator(_:edges:)](<../view/listrowseparator(__edges_).md>) and [listRowSeparatorTint(_:edges:)](<../view/listrowseparatortint(__edges_).md>).

## See Also

### Getting guides

- [leading](leading.md) — A guide that marks the leading edge of the view.
- [center](center.md) — A guide that marks the horizontal center of the view.
- [trailing](trailing.md) — A guide that marks the trailing edge of the view.
- [listRowSeparatorTrailing](listrowseparatortrailing.md) — A guide marking the trailing edge of a `List` row separator.
