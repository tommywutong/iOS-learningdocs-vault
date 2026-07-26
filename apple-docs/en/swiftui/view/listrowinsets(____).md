---
title: 'listRowInsets(_:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/listrowinsets(_:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/listrowinsets(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/listrowinsets%28_%3A_%3A%29.json'
content_hash: 'sha256:da67d1288cbf8998'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# listRowInsets(_:_:)

<sub>Instance Method</sub>

Sets the insets of rows in a list on the specified edges.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func listRowInsets(_ edges: Edge.Set = .all, _ length: CGFloat?) -> some View

```

## Parameters

- `edges` — The edges to set the insets to.

- `length` — An amount, given in points, to set the insets to on the specified edges.

## Return Value

A view in which the margins of list sections are set to the specified amount

## Discussion

Use this modifier to change the default insets of list rows on the specified edges.

In the example below, the `Flavor` enumeration provides content for list items. The SwiftUI [ForEach](../foreach.md) structure computes views for each element of the `Flavor` enumeration and extracts the raw value of each of its elements using the resulting text to create each list row item. The `listRowInsets(_:_:)` modifier then changes the leading inset of each row of the list and leaves the default insets on the other edges untouched:

```swift
struct ContentView: View {
    enum Flavor: String, CaseIterable, Identifiable {
        var id: String { self.rawValue }
        case vanilla, chocolate, strawberry
    }

    var body: some View {
        List {
            ForEach(Flavor.allCases) {
                Text($0.rawValue)
                    .listRowInsets(.leading, 25)
            }
        }
    }
}
```

![A screenshot showing a list with leading 25 point inset on each](../../../../attachments/0b10922ed606478b5a4155f90ed18221/SwiftUI-View-ListRowInsets@2x.png)

When applying multiple `listRowInsets` modifiers, modifiers with the same edges will override modifiers higher up in the view hierarchy.

> [!note] Note
> On iOS 18 and earlier, and on visionOS 2 and earlier, the content of list rows can grow slightly into the row insets. The effective vertical insets can then be smaller than expected.

## See Also

### Configuring a list’s layout

- [listRowInsets(_:)](<listrowinsets(__).md>) — Applies an inset to the rows in a list.
- [defaultMinListRowHeight](../environmentvalues/defaultminlistrowheight.md) — The default minimum height of rows in a list.
- [defaultMinListHeaderHeight](../environmentvalues/defaultminlistheaderheight.md) — The default minimum height of a header in a list.
- [listRowSpacing(_:)](<listrowspacing(__).md>) — Sets the vertical spacing between two adjacent rows in a List.
- [listSectionSpacing(_:)](<listsectionspacing(__).md>) — Sets the spacing between adjacent sections in a [List](../list.md) to a custom value.
- [ListSectionSpacing](../listsectionspacing.md) — The spacing options between two adjacent sections in a list.
- [listSectionMargins(_:_:)](<listsectionmargins(____).md>) — Set the section margins for the specific edges.
