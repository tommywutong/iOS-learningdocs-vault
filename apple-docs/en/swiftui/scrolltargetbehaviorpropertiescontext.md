---
title: ScrollTargetBehaviorPropertiesContext
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.4+, iPadOS 18.4+, Mac Catalyst 18.4+, macOS 15.4+, tvOS 18.4+, visionOS 2.4+, watchOS 11.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrolltargetbehaviorpropertiescontext
source_url: 'https://developer.apple.com/documentation/swiftui/scrolltargetbehaviorpropertiescontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrolltargetbehaviorpropertiescontext.json'
content_hash: 'sha256:386399d813794cf6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ScrollTargetBehaviorPropertiesContext

<sub>Structure</sub>

The context in which a scroll target behavior can decide its properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ScrollTargetBehaviorPropertiesContext
```

## Topics

### Instance Properties

- [axes](scrolltargetbehaviorpropertiescontext/axes.md) — The scrollable axes of the scroll view.
- [environment](scrolltargetbehaviorpropertiescontext/environment.md) — The environment of the scroll view.

## See Also

### Defining scroll targets

- [scrollTargetBehavior(_:)](<view/scrolltargetbehavior(__).md>) — Sets the scroll behavior of views scrollable in the provided axes.
- [scrollTargetLayout(isEnabled:)](<view/scrolltargetlayout(isenabled_).md>) — Configures the outermost layout as a scroll target layout.
- [ScrollTarget](scrolltarget.md) — A type defining the target in which a scroll view should try and scroll to.
- [ScrollTargetBehavior](scrolltargetbehavior.md) — A type that defines the scroll behavior of a scrollable view.
- [ScrollTargetBehaviorContext](scrolltargetbehaviorcontext.md) — The context in which a scroll target behavior updates its scroll target.
- [PagingScrollTargetBehavior](pagingscrolltargetbehavior.md) — The scroll behavior that aligns scroll targets to container-based geometry.
- [ViewAlignedScrollTargetBehavior](viewalignedscrolltargetbehavior.md) — The scroll behavior that aligns scroll targets to view-based geometry.
- [AnyScrollTargetBehavior](anyscrolltargetbehavior.md) — A type-erased scroll target behavior.
- [ScrollTargetBehaviorProperties](scrolltargetbehaviorproperties.md) — Properties influencing the scroll view a scroll target behavior applies to.
