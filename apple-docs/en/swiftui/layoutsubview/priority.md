---
title: priority
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/layoutsubview/priority
source_url: 'https://developer.apple.com/documentation/swiftui/layoutsubview/priority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layoutsubview/priority.json'
content_hash: 'sha256:16aa165610bc0689'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [LayoutSubview](../layoutsubview.md)

# priority

<sub>Instance Property</sub>

The layout priority of the subview.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var priority: Double { get }
```

## Discussion

If you define a custom layout type using the [Layout](../layout.md) protocol, you can read this value from subviews and use the value when deciding how to assign space to subviews. For example, you can read all of the subview priorities into an array before placing the subviews in a custom layout type called `BasicVStack`:

```swift
extension BasicVStack {
    func placeSubviews(
        in bounds: CGRect,
        proposal: ProposedViewSize,
        subviews: Subviews,
        cache: inout ()
    ) {
        let priorities = subviews.map { subview in
            subview.priority
        }

        // Place views, based on priorities.
    }
}
```

Set the layout priority for a view that appears in your layout by applying the [layoutPriority(_:)](<../view/layoutpriority(__).md>) view modifier. For example, you can assign two different priorities to views that you arrange with `BasicVStack`:

```swift
BasicVStack {
    Text("High priority")
        .layoutPriority(10)
    Text("Low priority")
        .layoutPriority(1)
}
```

## See Also

### Getting subview characteristics

- [dimensions(in:)](<dimensions(in_).md>) — Asks the subview for its dimensions and alignment guides.
- [sizeThatFits(_:)](<sizethatfits(__).md>) — Asks the subview for its size.
- [spacing](spacing.md) — The subviews’s preferred spacing values.
