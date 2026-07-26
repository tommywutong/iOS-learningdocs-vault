---
title: ScrollTargetBehaviorContext
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrolltargetbehaviorcontext
source_url: 'https://developer.apple.com/documentation/swiftui/scrolltargetbehaviorcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrolltargetbehaviorcontext.json'
content_hash: 'sha256:8753b5cc5cbc1633'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ScrollTargetBehaviorContext

<sub>Structure</sub>

The context in which a scroll target behavior updates its scroll target.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@dynamicMemberLookup struct ScrollTargetBehaviorContext
```

## Topics

### Getting the scroll target behavior context

- [axes](scrolltargetbehaviorcontext/axes.md) — The axes in which the scrollable view is scrollable.
- [containerSize](scrolltargetbehaviorcontext/containersize.md) — The size of the container of the scrollable view.
- [contentSize](scrolltargetbehaviorcontext/contentsize.md) — The size of the content of the scrollable view.
- [originalTarget](scrolltargetbehaviorcontext/originaltarget.md) — The original target when the scroll gesture began.
- [velocity](scrolltargetbehaviorcontext/velocity.md) — The current velocity of the scrollable view’s scroll gesture.

### Accessing the context

- [subscript(dynamicMember:)](<scrolltargetbehaviorcontext/subscript(dynamicmember_).md>)

## See Also

### Defining scroll targets

- [scrollTargetBehavior(_:)](<view/scrolltargetbehavior(__).md>) — Sets the scroll behavior of views scrollable in the provided axes.
- [scrollTargetLayout(isEnabled:)](<view/scrolltargetlayout(isenabled_).md>) — Configures the outermost layout as a scroll target layout.
- [ScrollTarget](scrolltarget.md) — A type defining the target in which a scroll view should try and scroll to.
- [ScrollTargetBehavior](scrolltargetbehavior.md) — A type that defines the scroll behavior of a scrollable view.
- [PagingScrollTargetBehavior](pagingscrolltargetbehavior.md) — The scroll behavior that aligns scroll targets to container-based geometry.
- [ViewAlignedScrollTargetBehavior](viewalignedscrolltargetbehavior.md) — The scroll behavior that aligns scroll targets to view-based geometry.
- [AnyScrollTargetBehavior](anyscrolltargetbehavior.md) — A type-erased scroll target behavior.
- [ScrollTargetBehaviorProperties](scrolltargetbehaviorproperties.md) — Properties influencing the scroll view a scroll target behavior applies to.
- [ScrollTargetBehaviorPropertiesContext](scrolltargetbehaviorpropertiescontext.md) — The context in which a scroll target behavior can decide its properties.
