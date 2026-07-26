---
title: Aligning views across stacks
framework: SwiftUI
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/aligning-views-across-stacks
source_url: 'https://developer.apple.com/documentation/swiftui/aligning-views-across-stacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/aligning-views-across-stacks.json'
content_hash: 'sha256:2b5ee817353d7fcb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md) · [Layout adjustments](layout-adjustments.md)

# Aligning views across stacks

<sub>Article</sub>

Create a custom alignment and use it to align views across multiple stacks.

## Overview

As you nest stacks together, you may want specific items within those stacks to align with each other. By default, the alignment you specify for a stack applies only to that stack’s child views. To align child views that reside in the nested stacks, define a custom alignment, assign it to the enclosing view, and use the alignment guide modifier to identify specific views to align.

### Begin with the default center alignment

To illustrate aligning items across stacks, the following view shows a horizontal stack wrapping around two nested vertical stacks that have a different number of child views. The enclosing [HStack](hstack.md) doesn’t define an alignment, so it defaults to [center](verticalalignment/center.md).

```swift
struct ImageRow: View {
    var body: some View {
        HStack {
            VStack {
                Image("bell_peppers")
                    .resizable()
                    .scaledToFit()
                Text("Bell Peppers")
                    .font(.title)
            }
            VStack {
                Image("chili_peppers")
                    .resizable()
                    .scaledToFit()
                Text("Chili Peppers")
                    .font(.title)
                Text("Higher levels of capsicum")
                    .font(.caption)
            }
        }
    }
}
```

The image below shows the contents of a nested vertical stack aligning at the center of the stack. The child elements within the vertical stacks, such as the titles beneath each image, don’t align with each other.

![](../../../attachments/480aa709dbda4c45359cc8f30eee7c53/Aligning-Views-Across-Stacks-1@2x.png)

<sub>Two stacks that each contain an image and a title beneath the image, vertically centered. The left stack contains an image in portrait mode with the title Bell Peppers beneath it. The right stack contains an image in landscape mode with the title Chili Peppers beneath it, and an additional caption that says Higher levels of capsicum.</sub>

### Define a custom alignment

To create a new vertical alignment guide, extend [VerticalAlignment](verticalalignment.md) with a new static property for your guide. Name the guide according to what it aligns to make it easier to use. The following example uses bottom positioning as the default value for this guide:

```swift
extension VerticalAlignment {
    /// A custom alignment for image titles.
    private struct ImageTitleAlignment: AlignmentID {
        static func defaultValue(in context: ViewDimensions) -> CGFloat {
            // Default to bottom alignment if no guides are set.
            context[VerticalAlignment.bottom]
        }
    }

    /// A guide for aligning titles.
    static let imageTitleAlignmentGuide = VerticalAlignment(
        ImageTitleAlignment.self
    )
}
```

### Assign and apply the custom alignment

To use the alignment guide, assign it to a parent view that encloses the views you want to align. The following example specifies `imageTitleAlignmentGuide` as the alignment for the horizontal stack:

```swift
struct RowOfAlignedImages: View {
    var body: some View {
        HStack(alignment: .imageTitleAlignmentGuide) {
            VStack {
                Image("bell_peppers")
                    .resizable()
                    .scaledToFit()

                Text("Bell Peppers")
                    .font(.title)
            }
            VStack {
                Image("chili_peppers")
                    .resizable()
                    .scaledToFit()

                Text("Chili Peppers")
                    .font(.title)

                Text("Higher levels of capsicum")
                    .font(.caption)
            }
        }
    }
}
```

The two vertical stacks now align on the bottoms of the stacks, using the default from your specification for the custom guide.

![](../../../attachments/7483e9c5eac752e7bad0acb112e35b23/Aligning-Views-Across-Stacks-2@2x.png)

<sub>Two stacks that each contain an image and a title beneath the image, aligned on the bottoms of the stacks. The left stack contains an image in portrait mode with the title Bell Peppers beneath it. The right stack contains an image in landscape mode with the title Chili Peppers beneath it, and an additional caption that says Higher levels of capsicum.</sub>

When you define an alignment on a stack, it projects through enclosed child views. Within the nested [VStack](vstack.md) instances, apply [alignmentGuide(_:computeValue:)](<view/alignmentguide(__computevalue_).md>) to the views to align, using your custom guide for the [HStack](hstack.md).

```swift
struct RowOfAlignedImages: View {
    var body: some View {
        HStack(alignment: .imageTitleAlignmentGuide) {
            VStack {
                Image("bell_peppers")
                    .resizable()
                    .scaledToFit()

                Text("Bell Peppers")
                    .font(.title)
                    .alignmentGuide(.imageTitleAlignmentGuide) { context in
                        context[.firstTextBaseline]
                    }
            }
            VStack {
                Image("chili_peppers")
                    .resizable()
                    .scaledToFit()

                Text("Chili Peppers")
                    .font(.title)
                    .alignmentGuide(.imageTitleAlignmentGuide) { context in
                        context[.firstTextBaseline]
                    }

                Text("Higher levels of capsicum")
                    .font(.caption)
            }
        }
    }
}
```

The closure from the alignment guide modifier returns [firstTextBaseline](verticalalignment/firsttextbaseline.md), which aligns the baselines of the titles with the alignment guide `imageTitleAlignmentGuide`.

![](../../../attachments/bc9dec8437221c95639947fbb0fb0073/Aligning-Views-Across-Stacks-3@2x.png)

<sub>Two stacks that each contain an image and a title beneath the image, aligned by the titles. The left stack contains an image in portrait mode with the title Bell Peppers beneath it. The right stack contains an image in landscape mode with the title Chili Peppers beneath it, and an additional caption that says Higher levels of capsicum.</sub>

## See Also

### Aligning views

- [Aligning views within a stack](aligning-views-within-a-stack.md) — Position views inside a stack using alignment guides.
- [alignmentGuide(_:computeValue:)](<view/alignmentguide(__computevalue_).md>) — Sets the view’s horizontal alignment.
- [Alignment](alignment.md) — An alignment in both axes.
- [HorizontalAlignment](horizontalalignment.md) — An alignment position along the horizontal axis.
- [VerticalAlignment](verticalalignment.md) — An alignment position along the vertical axis.
- [DepthAlignment](depthalignment.md) — An alignment position along the depth axis.
- [AlignmentID](alignmentid.md) — A type that you use to create custom alignment guides.
- [ViewDimensions](viewdimensions.md) — A view’s size and alignment guides in its own coordinate space.
- [ViewDimensions3D](viewdimensions3d.md) — A view’s 3D size and alignment guides in its own coordinate space.
- [SpatialContainer](spatialcontainer.md) — A layout container that aligns overlapping content in 3D space.
