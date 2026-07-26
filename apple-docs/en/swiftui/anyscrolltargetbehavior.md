---
title: AnyScrollTargetBehavior
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/anyscrolltargetbehavior
source_url: 'https://developer.apple.com/documentation/swiftui/anyscrolltargetbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/anyscrolltargetbehavior.json'
content_hash: 'sha256:4f5e2c3a476ad686'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AnyScrollTargetBehavior

<sub>Structure</sub>

A type-erased scroll target behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct AnyScrollTargetBehavior
```

## Overview

Provide this to the [scrollTargetBehavior(_:)](<view/scrolltargetbehavior(__).md>) modifier. When the underlying behavior changes, the scroll view to which this behavior applies will be updated.

Use this to dynamically control the scroll target behavior at runtime. For example, you could provide a paging behavior in compact size classes and a view aligned behavior otherwise.

```swift
@Environment(\.horizontalSizeClass) var sizeClass

var body: some View {
    ScrollView { ... }
        .scrollTargetBehavior(scrollTargetBehavior)
}

 var scrollTargetBehavior: some ScrollTargetBehavior {
    sizeClass == .compact
        ? AnyScrollTargetBehavior(.paging)
        : AnyScrollTargetBehavior(.viewAligned)
}
```

## Relationships

- **Conforms To**: [ScrollTargetBehavior](scrolltargetbehavior.md)

## Topics

### Initializers

- [init(_:)](<anyscrolltargetbehavior/init(__).md>) — Creates a new type-erase scroll target behavior.

### Instance Properties

- [base](anyscrolltargetbehavior/base.md) — The type-erased scroll target behavior.

## See Also

### Defining scroll targets

- [scrollTargetBehavior(_:)](<view/scrolltargetbehavior(__).md>) — Sets the scroll behavior of views scrollable in the provided axes.
- [scrollTargetLayout(isEnabled:)](<view/scrolltargetlayout(isenabled_).md>) — Configures the outermost layout as a scroll target layout.
- [ScrollTarget](scrolltarget.md) — A type defining the target in which a scroll view should try and scroll to.
- [ScrollTargetBehavior](scrolltargetbehavior.md) — A type that defines the scroll behavior of a scrollable view.
- [ScrollTargetBehaviorContext](scrolltargetbehaviorcontext.md) — The context in which a scroll target behavior updates its scroll target.
- [PagingScrollTargetBehavior](pagingscrolltargetbehavior.md) — The scroll behavior that aligns scroll targets to container-based geometry.
- [ViewAlignedScrollTargetBehavior](viewalignedscrolltargetbehavior.md) — The scroll behavior that aligns scroll targets to view-based geometry.
- [ScrollTargetBehaviorProperties](scrolltargetbehaviorproperties.md) — Properties influencing the scroll view a scroll target behavior applies to.
- [ScrollTargetBehaviorPropertiesContext](scrolltargetbehaviorpropertiescontext.md) — The context in which a scroll target behavior can decide its properties.
