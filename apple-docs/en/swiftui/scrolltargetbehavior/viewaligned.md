---
title: viewAligned
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrolltargetbehavior/viewaligned
source_url: 'https://developer.apple.com/documentation/swiftui/scrolltargetbehavior/viewaligned'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrolltargetbehavior/viewaligned.json'
content_hash: 'sha256:619831263dce0fe1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollTargetBehavior](../scrolltargetbehavior.md)

# viewAligned

<sub>Type Property</sub>

The scroll behavior that aligns scroll targets to view-based geometry.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static var viewAligned: ViewAlignedScrollTargetBehavior { get }
```

## Discussion

You use this behavior when a scroll view should always align its scroll targets to a rectangle that’s aligned to the geometry of a view. In the following example, the scroll view always picks an item view to settle on.

```swift
ScrollView(.horizontal) {
    LazyHStack(spacing: 10.0) {
        ForEach(items) { item in
            ItemView(item)
        }
    }
    .scrollTargetLayout()
}
.scrollTargetBehavior(.viewAligned)
.padding(.horizontal, 20.0)
```

You configure which views should be used for settling using the `View/scrollTargetLayout()` modifier. Apply this modifier to a layout container like [LazyVStack](../lazyvstack.md) or [HStack](../hstack.md) and each individual view in that layout will be considered for alignment.

You can customize whether the view aligned behavior limits the number of views that can be scrolled at a time by using the `ViewAlignedScrollTargetBehavior.LimitBehavior` type. Provide a value of `ViewAlignedScrollTargetBehavior.LimitBehavior/always` to always have the behavior only allow a few views to be scrolled at a time.

By default, the view aligned behavior limits the number of views it scrolls when in a compact horizontal size class when scrollable in the horizontal axis, when in a compact vertical size class when scrollable in the vertical axis, and otherwise doesn’t impose any limit on the number of views that can be scrolled.

## See Also

### Getting the scroll target behavior

- [paging](paging.md) — The scroll behavior that aligns scroll targets to container-based geometry.
- [viewAligned(limitBehavior:)](<viewaligned(limitbehavior_).md>) — The scroll behavior that aligns scroll targets to view-based geometry.
