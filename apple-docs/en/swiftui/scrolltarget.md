---
title: ScrollTarget
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrolltarget
source_url: 'https://developer.apple.com/documentation/swiftui/scrolltarget'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrolltarget.json'
content_hash: 'sha256:f5a1897010a9cbca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ScrollTarget

<sub>Structure</sub>

A type defining the target in which a scroll view should try and scroll to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ScrollTarget
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Getting the scroll target

- [anchor](scrolltarget/anchor.md) — The anchor to which the rect should be aligned within the visible region of the scrollable view.
- [rect](scrolltarget/rect.md) — The rect that a scrollable view should try and have contained.

## See Also

### Defining scroll targets

- [scrollTargetBehavior(_:)](<view/scrolltargetbehavior(__).md>) — Sets the scroll behavior of views scrollable in the provided axes.
- [scrollTargetLayout(isEnabled:)](<view/scrolltargetlayout(isenabled_).md>) — Configures the outermost layout as a scroll target layout.
- [ScrollTargetBehavior](scrolltargetbehavior.md) — A type that defines the scroll behavior of a scrollable view.
- [ScrollTargetBehaviorContext](scrolltargetbehaviorcontext.md) — The context in which a scroll target behavior updates its scroll target.
- [PagingScrollTargetBehavior](pagingscrolltargetbehavior.md) — The scroll behavior that aligns scroll targets to container-based geometry.
- [ViewAlignedScrollTargetBehavior](viewalignedscrolltargetbehavior.md) — The scroll behavior that aligns scroll targets to view-based geometry.
- [AnyScrollTargetBehavior](anyscrolltargetbehavior.md) — A type-erased scroll target behavior.
- [ScrollTargetBehaviorProperties](scrolltargetbehaviorproperties.md) — Properties influencing the scroll view a scroll target behavior applies to.
- [ScrollTargetBehaviorPropertiesContext](scrolltargetbehaviorpropertiescontext.md) — The context in which a scroll target behavior can decide its properties.
