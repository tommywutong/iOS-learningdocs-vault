---
title: 'containerRelativeFrame(_:alignment:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/containerrelativeframe(_:alignment:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/containerrelativeframe(_:alignment:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/containerrelativeframe%28_%3Aalignment%3A_%3A%29.json'
content_hash: 'sha256:85ddb1ca90b93571'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# containerRelativeFrame(_:alignment:_:)

<sub>Instance Method</sub>

Positions this view within an invisible frame with a size relative to the nearest container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func containerRelativeFrame(_ axes: Axis.Set, alignment: Alignment = .center, _ length: @escaping (CGFloat, Axis) -> CGFloat) -> some View

```

## Discussion

Use the [containerRelativeFrame(_:alignment:)](<containerrelativeframe(__alignment_).md>) modifier to specify a size for a view’s width, height, or both that is dependent on the size of the nearest container. Different things can represent a “container” including:

- The window presenting a view on iPadOS or macOS, or the screen of a device on iOS.
- A column of a NavigationSplitView
- A NavigationStack
- A tab of a TabView
- A scrollable view like ScrollView or List

The size provided to this modifier is the size of a container like the ones listed above subtracting any safe area insets that might be applied to that container.

The following example will have each purple rectangle occupy the full size of the screen on iOS:

```swift
ScrollView(.horizontal) {
    LazyHStack(spacing: 0.0) {
        ForEach(items) { item in
            Rectangle()
                .fill(.purple)
                .containerRelativeFrame([.horizontal, .vertical])
        }
    }
}
```

Use the [containerRelativeFrame(_:count:span:spacing:alignment:)](<containerrelativeframe(__count_span_spacing_alignment_).md>) modifier to size a view such that multiple views will be visible in the container. When using this modifier, the count refers to the total number of rows or columns that the length of the container size in a particular axis should be divided into. The span refers to the number of rows or columns that the modified view should actually occupy. Thus the size of the element can be described like so:

```swift
let availableWidth = (containerWidth - (spacing * (count - 1)))
let columnWidth = (availableWidth / count)
let itemWidth = (columnWidth * span) + ((span - 1) * spacing)
```

The following example only uses the nearest container size in the horizontal axis, allowing the vertical axis to be determined using the [aspectRatio(_:contentMode:)](<aspectratio(__contentmode_).md>) modifier.

```swift
ScrollView(.horizontal) {
    LazyHStack(spacing: 10.0) {
        ForEach(items) { item in
            Rectangle()
                .fill(.purple)
                .aspectRatio(3.0 / 2.0, contentMode: .fit)
                .containerRelativeFrame(
                    .horizontal, count: 4, span: 3, spacing: 10.0)
        }
    }
}
.safeAreaPadding(.horizontal, 20.0)
```

Use this modifier to apply your own custom logic to adjust the size of the nearest container for your view. The following example will result in the container frame’s width being divided by 3 and using that value as the width of the purple rectangle.

```swift
Rectangle()
    .fill(.purple)
    .aspectRatio(1.0, contentMode: .fill)
    .containerRelativeFrame(
        .horizontal, alignment: .topLeading
    ) { length, axis in
        if axis == .vertical {
            return length / 3.0
        } else {
            return length / 5.0
        }
    }
```

## See Also

### Influencing a view’s size

- [frame(width:height:alignment:)](<frame(width_height_alignment_).md>) — Positions this view within an invisible frame with the specified size.
- [frame(depth:alignment:)](<frame(depth_alignment_).md>) — Positions this view within an invisible frame with the specified depth.
- [frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)](<frame(minwidth_idealwidth_maxwidth_minheight_idealheight_maxheight_alignment_).md>) — Positions this view within an invisible frame having the specified size constraints.
- [frame(minDepth:idealDepth:maxDepth:alignment:)](<frame(mindepth_idealdepth_maxdepth_alignment_).md>) — Positions this view within an invisible frame having the specified depth constraints.
- [containerRelativeFrame(_:alignment:)](<containerrelativeframe(__alignment_).md>) — Positions this view within an invisible frame with a size relative to the nearest container.
- [containerRelativeFrame(_:count:span:spacing:alignment:)](<containerrelativeframe(__count_span_spacing_alignment_).md>) — Positions this view within an invisible frame with a size relative to the nearest container.
- [fixedSize()](<fixedsize().md>) — Fixes this view at its ideal size.
- [fixedSize(horizontal:vertical:)](<fixedsize(horizontal_vertical_).md>) — Fixes this view at its ideal size in the specified dimensions.
- [layoutPriority(_:)](<layoutpriority(__).md>) — Sets the priority by which a parent layout should apportion space to this child.
