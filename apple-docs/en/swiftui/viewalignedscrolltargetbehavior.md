---
title: ViewAlignedScrollTargetBehavior
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/viewalignedscrolltargetbehavior
source_url: 'https://developer.apple.com/documentation/swiftui/viewalignedscrolltargetbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/viewalignedscrolltargetbehavior.json'
content_hash: 'sha256:39d06058b165dfd6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ViewAlignedScrollTargetBehavior

<sub>Structure</sub>

The scroll behavior that aligns scroll targets to view-based geometry.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ViewAlignedScrollTargetBehavior
```

## Overview

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

You configure which views should be used for settling using the [scrollTargetLayout(isEnabled:)](<view/scrolltargetlayout(isenabled_).md>) modifier. Apply this modifier to a layout container like [LazyVStack](lazyvstack.md) or [HStack](hstack.md) and each individual view in that layout will be considered for alignment.

You can customize whether the view aligned behavior limits the number of views that can be scrolled at a time by using the [LimitBehavior](viewalignedscrolltargetbehavior/limitbehavior.md) type. Provide a value of [always](viewalignedscrolltargetbehavior/limitbehavior/always.md) to always have the behavior only allow a few views to be scrolled at a time.

By default, the view aligned behavior will limit the number of views it scrolls when in a compact horizontal size class when scrollable in the horizontal axis, when in a compact vertical size class when scrollable in the vertical axis, and otherwise does not impose any limit on the number of views that can be scrolled.

## Relationships

- **Conforms To**: [ScrollTargetBehavior](scrolltargetbehavior.md)

## Topics

### Creating the target behavior

- [init(limitBehavior:)](<viewalignedscrolltargetbehavior/init(limitbehavior_).md>) — Creates a view aligned scroll behavior.
- [LimitBehavior](viewalignedscrolltargetbehavior/limitbehavior.md) — A type that defines the amount of views that can be scrolled at a time.

### Initializers

- [init(anchor:)](<viewalignedscrolltargetbehavior/init(anchor_).md>) — Creates a view aligned scroll behavior with the provided anchor.
- [init(limitBehavior:anchor:)](<viewalignedscrolltargetbehavior/init(limitbehavior_anchor_).md>) — Creates a view aligned scroll behavior with the provided limit behavior and anchor.

## See Also

### Defining scroll targets

- [scrollTargetBehavior(_:)](<view/scrolltargetbehavior(__).md>) — Sets the scroll behavior of views scrollable in the provided axes.
- [scrollTargetLayout(isEnabled:)](<view/scrolltargetlayout(isenabled_).md>) — Configures the outermost layout as a scroll target layout.
- [ScrollTarget](scrolltarget.md) — A type defining the target in which a scroll view should try and scroll to.
- [ScrollTargetBehavior](scrolltargetbehavior.md) — A type that defines the scroll behavior of a scrollable view.
- [ScrollTargetBehaviorContext](scrolltargetbehaviorcontext.md) — The context in which a scroll target behavior updates its scroll target.
- [PagingScrollTargetBehavior](pagingscrolltargetbehavior.md) — The scroll behavior that aligns scroll targets to container-based geometry.
- [AnyScrollTargetBehavior](anyscrolltargetbehavior.md) — A type-erased scroll target behavior.
- [ScrollTargetBehaviorProperties](scrolltargetbehaviorproperties.md) — Properties influencing the scroll view a scroll target behavior applies to.
- [ScrollTargetBehaviorPropertiesContext](scrolltargetbehaviorpropertiescontext.md) — The context in which a scroll target behavior can decide its properties.
