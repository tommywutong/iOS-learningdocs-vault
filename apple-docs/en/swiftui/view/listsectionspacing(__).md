---
title: 'listSectionSpacing(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/listsectionspacing(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/listsectionspacing(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/listsectionspacing%28_%3A%29.json'
content_hash: 'sha256:0e9062c5db6384a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# listSectionSpacing(_:)

<sub>Instance Method</sub>

Sets the spacing between adjacent sections in a [List](../list.md) to a custom value.

<sub>iOS, iPadOS, Mac Catalyst, visionOS, watchOS</sub>

```swift
nonisolated func listSectionSpacing(_ spacing: CGFloat) -> some View

```

## Parameters

- `spacing` — The amount of spacing to apply.

## Discussion

The following example creates a [List](../list.md) with 5 pts of spacing between sections:

```swift
List {
    Section("Colors") {
        Text("Blue")
        Text("Red")
    }

    Section("Shapes") {
        Text("Square")
        Text("Circle")
    }
}
.listSectionSpacing(5.0)
```

Spacing can also be specified on an individual [Section](../section.md), as in this example:

```swift
Section("Borders") {
    Text("Dashed")
    Text("Solid")
}
.listSectionSpacing(10.0)
```

If adjacent sections have different spacing applied, each section applies half its spacing above and below. Sections without explicit spacing apply the spacing of their adjacent sections.

```swift
List {
    Section("Colors") {
        Text("Blue")
        Text("Red")
    }

    Section("Borders") {
        Text("Dashed")
        Text("Solid")
    }
    .listSectionSpacing(10.0)

    Section("Shapes") {
        Text("Square")
        Text("Circle")
    }
    .listSectionSpacing(100.0)
}
```

In the above example, the “Colors” and “Borders” section are separated by 10 pts of spacing, and the “Borders” and “Shapes” section are separated by 55 pts of spacing.

Spacing applied on sections in the [List](../list.md) overrides spacing applied on the [List](../list.md) as a whole.

## See Also

### Configuring a list’s layout

- [listRowInsets(_:)](<listrowinsets(__).md>) — Applies an inset to the rows in a list.
- [listRowInsets(_:_:)](<listrowinsets(____).md>) — Sets the insets of rows in a list on the specified edges.
- [defaultMinListRowHeight](../environmentvalues/defaultminlistrowheight.md) — The default minimum height of rows in a list.
- [defaultMinListHeaderHeight](../environmentvalues/defaultminlistheaderheight.md) — The default minimum height of a header in a list.
- [listRowSpacing(_:)](<listrowspacing(__).md>) — Sets the vertical spacing between two adjacent rows in a List.
- [ListSectionSpacing](../listsectionspacing.md) — The spacing options between two adjacent sections in a list.
- [listSectionMargins(_:_:)](<listsectionmargins(____).md>) — Set the section margins for the specific edges.
