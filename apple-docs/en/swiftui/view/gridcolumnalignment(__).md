---
title: 'gridColumnAlignment(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/gridcolumnalignment(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/gridcolumnalignment(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/gridcolumnalignment%28_%3A%29.json'
content_hash: 'sha256:8ffda07af1567f15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# gridColumnAlignment(_:)

<sub>Instance Method</sub>

Overrides the default horizontal alignment of the grid column that the view appears in.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func gridColumnAlignment(_ guide: HorizontalAlignment) -> some View

```

## Parameters

- `guide` — The [HorizontalAlignment](../horizontalalignment.md) guide to use for the grid column that the view appears in.

## Return Value

A view that uses the specified horizontal alignment, and that causes all cells in the same column of a grid to use the same alignment.

## Discussion

You set a default alignment for the cells in a grid in both vertical and horizontal dimensions when you create the grid with the [init(alignment:horizontalSpacing:verticalSpacing:content:)](<../grid/init(alignment_horizontalspacing_verticalspacing_content_).md>) initializer. However, you can use the `gridColumnAlignment(_:)` modifier to override the horizontal alignment of a column within the grid. The following example sets a grid’s alignment to [leadingFirstTextBaseline](../alignment/leadingfirsttextbaseline.md), and then sets the first column to use [trailing](../horizontalalignment/trailing.md) alignment:

```swift
Grid(alignment: .leadingFirstTextBaseline) {
    GridRow {
        Text("Regular font:")
            .gridColumnAlignment(.trailing) // Align the entire first column.
        Text("Helvetica 12")
        Button("Select...") { }
    }
    GridRow {
        Text("Fixed-width font:")
        Text("Menlo Regular 11")
        Button("Select...") { }
    }
    GridRow {
        Color.clear
            .gridCellUnsizedAxes([.vertical, .horizontal])
        Toggle("Use fixed-width font for new documents", isOn: $isOn)
            .gridCellColumns(2)
    }
}
```

This creates the layout of a typical macOS configuration view, with the trailing edge of the first column flush with the leading edge of the second column:

![A screenshot of a configuration view, arranged in a grid. The grid](../../../../attachments/4f5b4b93d67b82887d0e3b515f084470/View-gridColumnAlignment-1-macOS@2x.png)

Add the modifier to only one cell in a column. The grid automatically aligns all cells in that column the same way. You get undefined behavior if you apply different alignments to different cells in the same column.

To override row alignment, see [init(alignment:content:)](<../gridrow/init(alignment_content_).md>). To override alignment for a single cell, see [gridCellAnchor(_:)](<gridcellanchor(__).md>).

## See Also

### Statically arranging views in two dimensions

- [Grid](../grid.md) — A container view that arranges other views in a two dimensional layout.
- [GridRow](../gridrow.md) — A horizontal row in a two dimensional grid container.
- [gridCellColumns(_:)](<gridcellcolumns(__).md>) — Tells a view that acts as a cell in a grid to span the specified number of columns.
- [gridCellAnchor(_:)](<gridcellanchor(__).md>) — Specifies a custom alignment anchor for a view that acts as a grid cell.
- [gridCellUnsizedAxes(_:)](<gridcellunsizedaxes(__).md>) — Asks grid layouts not to offer the view extra size in the specified axes.
