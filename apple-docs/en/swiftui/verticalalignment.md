---
title: VerticalAlignment
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/verticalalignment
source_url: 'https://developer.apple.com/documentation/swiftui/verticalalignment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/verticalalignment.json'
content_hash: 'sha256:5b575f45b0d85b1f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# VerticalAlignment

<sub>Structure</sub>

An alignment position along the vertical axis.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct VerticalAlignment
```

## Overview

Use vertical alignment guides to position views relative to one another vertically, like when you place views side-by-side in an [HStack](hstack.md) or when you create a row of views in a [Grid](grid.md) using [GridRow](gridrow.md). The following example demonstrates common built-in vertical alignments:

![Five rows of content. Each row contains text inside](../../../attachments/a63aa800a94319cd283176a8b21bb7af/VerticalAlignment-1-iOS@2x.png)

You can generate the example above by creating a series of rows implemented as horizontal stacks, where you configure each stack with a different alignment guide:

```swift
private struct VerticalAlignmentGallery: View {
    var body: some View {
        VStack(spacing: 30) {
            row(alignment: .top, text: "Top")
            row(alignment: .center, text: "Center")
            row(alignment: .bottom, text: "Bottom")
            row(alignment: .firstTextBaseline, text: "First Text Baseline")
            row(alignment: .lastTextBaseline, text: "Last Text Baseline")
        }
    }

    private func row(alignment: VerticalAlignment, text: String) -> some View {
        HStack(alignment: alignment, spacing: 0) {
            Color.red.frame(height: 1)
            Text(text).font(.title).border(.gray)
            Color.red.frame(height: 1)
        }
    }
}
```

During layout, SwiftUI aligns the views inside each stack by bringing together the specified guides of the affected views. SwiftUI calculates the position of a guide for a particular view based on the characteristics of the view. For example, the [center](verticalalignment/center.md) guide appears at half the height of the view. You can override the guide calculation for a particular view using the [alignmentGuide(_:computeValue:)](<view/alignmentguide(__computevalue_).md>) view modifier.

### Text baseline alignment

Use the [firstTextBaseline](verticalalignment/firsttextbaseline.md) or [lastTextBaseline](verticalalignment/lasttextbaseline.md) guide to match the bottom of either the top- or bottom-most line of text that a view contains, respectively. Text baseline alignment excludes the parts of characters that descend below the baseline, like the tail on lower case g and j:

```swift
row(alignment: .firstTextBaseline, text: "fghijkl")
```

If you use a text baseline alignment on a view that contains no text, SwiftUI applies the equivalent of [bottom](verticalalignment/bottom.md) alignment instead. For the row in the example above, SwiftUI matches the bottom of the horizontal lines with the baseline of the text:

![A string containing the lowercase letters f, g, h, i, j, and](../../../attachments/dd76eb2e219217e46502bd95d368e453/VerticalAlignment-2-iOS@2x.png)

Aligning a text view to its baseline rather than to the bottom of its frame produces the best layout effect in many cases, like when creating forms. For example, you can align the baseline of descriptive text in one [GridRow](gridrow.md) cell with the baseline of a text field, or the label of a checkbox, in another cell in the same row.

### Custom alignment guides

You can create a custom vertical alignment guide by first creating a type that conforms to the [AlignmentID](alignmentid.md) protocol, and then using that type to initialize a new static property on `VerticalAlignment`:

```swift
private struct FirstThirdAlignment: AlignmentID {
    static func defaultValue(in context: ViewDimensions) -> CGFloat {
        context.height / 3
    }
}

extension VerticalAlignment {
    static let firstThird = VerticalAlignment(FirstThirdAlignment.self)
}
```

You implement the [defaultValue(in:)](<alignmentid/defaultvalue(in_).md>) method to calculate a default value for the custom alignment guide. The method receives a [ViewDimensions](viewdimensions.md) instance that you can use to calculate a value based on characteristics of the view. The example above places the guide at one-third of the height of the view as measured from the view’s origin.

You can then use the custom alignment guide like any built-in guide. For example, you can use it as the `alignment` parameter to an [HStack](hstack.md), or to alter the guide calculation for a specific view using the [alignmentGuide(_:computeValue:)](<view/alignmentguide(__computevalue_).md>) view modifier.

### Composite alignment

Combine a `VerticalAlignment` with a [HorizontalAlignment](horizontalalignment.md) to create a composite [Alignment](alignment.md) that indicates both vertical and horizontal positioning in one value. For example, you could combine your custom `firstThird` vertical alignment from the previous section with a built-in [center](horizontalalignment/center.md) horizontal alignment to use in a [ZStack](zstack.md):

```swift
struct LayeredHorizontalStripes: View {
    var body: some View {
        ZStack(alignment: Alignment(horizontal: .center, vertical: .firstThird)) {
            horizontalStripes(color: .blue)
                .frame(width: 180, height: 90)
            horizontalStripes(color: .green)
                .frame(width: 70, height: 60)
        }
    }

    private func horizontalStripes(color: Color) -> some View {
        VStack(spacing: 1) {
            ForEach(0..<3) { _ in color }
        }
    }
}
```

The example above uses widths and heights that generate two mismatched sets of three vertical stripes. The [ZStack](zstack.md) centers the two sets horizontally and aligns them vertically one-third from the top of each set. This aligns the bottom edges of the top stripe from each set:

![Two sets of three vertically stacked rectangles. The first](../../../attachments/4f1ff29e1d4d39bc64031e05701a5a60/VerticalAlignment-3-iOS@2x.png)

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting guides

- [top](verticalalignment/top.md) — A guide that marks the top edge of the view.
- [center](verticalalignment/center.md) — A guide that marks the vertical center of the view.
- [bottom](verticalalignment/bottom.md) — A guide that marks the bottom edge of the view.
- [firstTextBaseline](verticalalignment/firsttextbaseline.md) — A guide that marks the top-most text baseline in a view.
- [lastTextBaseline](verticalalignment/lasttextbaseline.md) — A guide that marks the bottom-most text baseline in a view.

### Creating a custom alignment

- [init(_:)](<verticalalignment/init(__).md>) — Creates a custom vertical alignment of the specified type.
- [combineExplicit(_:)](<verticalalignment/combineexplicit(__).md>) — Merges a sequence of explicit alignment values produced by this instance.

## See Also

### Aligning views

- [Aligning views within a stack](aligning-views-within-a-stack.md) — Position views inside a stack using alignment guides.
- [Aligning views across stacks](aligning-views-across-stacks.md) — Create a custom alignment and use it to align views across multiple stacks.
- [alignmentGuide(_:computeValue:)](<view/alignmentguide(__computevalue_).md>) — Sets the view’s horizontal alignment.
- [Alignment](alignment.md) — An alignment in both axes.
- [HorizontalAlignment](horizontalalignment.md) — An alignment position along the horizontal axis.
- [DepthAlignment](depthalignment.md) — An alignment position along the depth axis.
- [AlignmentID](alignmentid.md) — A type that you use to create custom alignment guides.
- [ViewDimensions](viewdimensions.md) — A view’s size and alignment guides in its own coordinate space.
- [ViewDimensions3D](viewdimensions3d.md) — A view’s 3D size and alignment guides in its own coordinate space.
- [SpatialContainer](spatialcontainer.md) — A layout container that aligns overlapping content in 3D space.
