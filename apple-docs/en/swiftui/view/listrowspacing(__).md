---
title: 'listRowSpacing(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 27.0+ beta, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/listrowspacing(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/listrowspacing(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/listrowspacing%28_%3A%29.json'
content_hash: 'sha256:26eca167603b9b03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# listRowSpacing(_:)

<sub>Instance Method</sub>

Sets the vertical spacing between two adjacent rows in a List.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated func listRowSpacing(_ spacing: CGFloat?) -> some View

```

## Parameters

- `spacing` — The spacing value to use. A value of `nil` uses the default spacing.

## Discussion

The following example creates a List with 10 pts of spacing between each row:

```swift
List {
    Text("Blue")
    Text("Red")
}
.listRowSpacing(10.0)
```

## See Also

### Configuring a list’s layout

- [listRowInsets(_:)](<listrowinsets(__).md>) — Applies an inset to the rows in a list.
- [listRowInsets(_:_:)](<listrowinsets(____).md>) — Sets the insets of rows in a list on the specified edges.
- [defaultMinListRowHeight](../environmentvalues/defaultminlistrowheight.md) — The default minimum height of rows in a list.
- [defaultMinListHeaderHeight](../environmentvalues/defaultminlistheaderheight.md) — The default minimum height of a header in a list.
- [listSectionSpacing(_:)](<listsectionspacing(__).md>) — Sets the spacing between adjacent sections in a [List](../list.md) to a custom value.
- [ListSectionSpacing](../listsectionspacing.md) — The spacing options between two adjacent sections in a list.
- [listSectionMargins(_:_:)](<listsectionmargins(____).md>) — Set the section margins for the specific edges.
