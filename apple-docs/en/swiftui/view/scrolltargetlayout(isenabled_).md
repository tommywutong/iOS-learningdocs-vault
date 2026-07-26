---
title: 'scrollTargetLayout(isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/scrolltargetlayout(isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/scrolltargetlayout(isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/scrolltargetlayout%28isenabled%3A%29.json'
content_hash: 'sha256:cdb964180eec0865'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# scrollTargetLayout(isEnabled:)

<sub>Instance Method</sub>

Configures the outermost layout as a scroll target layout.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func scrollTargetLayout(isEnabled: Bool = true) -> some View

```

## Discussion

This modifier works together with the [ViewAlignedScrollTargetBehavior](../viewalignedscrolltargetbehavior.md) to ensure that scroll views align to view based content.

Apply this modifier to layout containers like [LazyHStack](../lazyhstack.md) or [VStack](../vstack.md) within a [ScrollView](../scrollview.md) that contain the main repeating content of your [ScrollView](../scrollview.md).

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
```

A scroll target layout ensures that any target layout nested within the primary one will not also become a scroll target layout.

```swift
LazyHStack { // a scroll target layout
    VStack { ... } // not a scroll target layout
    LazyHStack { ... } // also not a scroll target layout
}
.scrollTargetLayout()
```

## See Also

### Defining scroll targets

- [scrollTargetBehavior(_:)](<scrolltargetbehavior(__).md>) — Sets the scroll behavior of views scrollable in the provided axes.
- [ScrollTarget](../scrolltarget.md) — A type defining the target in which a scroll view should try and scroll to.
- [ScrollTargetBehavior](../scrolltargetbehavior.md) — A type that defines the scroll behavior of a scrollable view.
- [ScrollTargetBehaviorContext](../scrolltargetbehaviorcontext.md) — The context in which a scroll target behavior updates its scroll target.
- [PagingScrollTargetBehavior](../pagingscrolltargetbehavior.md) — The scroll behavior that aligns scroll targets to container-based geometry.
- [ViewAlignedScrollTargetBehavior](../viewalignedscrolltargetbehavior.md) — The scroll behavior that aligns scroll targets to view-based geometry.
- [AnyScrollTargetBehavior](../anyscrolltargetbehavior.md) — A type-erased scroll target behavior.
- [ScrollTargetBehaviorProperties](../scrolltargetbehaviorproperties.md) — Properties influencing the scroll view a scroll target behavior applies to.
- [ScrollTargetBehaviorPropertiesContext](../scrolltargetbehaviorpropertiescontext.md) — The context in which a scroll target behavior can decide its properties.
