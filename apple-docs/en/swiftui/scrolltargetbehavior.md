---
title: ScrollTargetBehavior
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrolltargetbehavior
source_url: 'https://developer.apple.com/documentation/swiftui/scrolltargetbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrolltargetbehavior.json'
content_hash: 'sha256:3df0caffa1b69660'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ScrollTargetBehavior

<sub>Protocol</sub>

A type that defines the scroll behavior of a scrollable view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol ScrollTargetBehavior
```

## Overview

A scrollable view calculates where scroll gestures should end using its deceleration rate and the state of its scroll gesture by default. A scroll behavior allows for customizing this logic.

You define a scroll behavior using the [updateTarget(_:context:)](<scrolltargetbehavior/updatetarget(__context_).md>) method.

Using this method, you can control where someone can scroll in a scrollable view. For example, you can create a custom scroll behavior that aligns to every 10 points by doing the following:

```swift
struct BasicScrollTargetBehavior: ScrollTargetBehavior {
    func updateTarget(_ target: inout ScrollTarget, context: TargetContext) {
        // Align to every 1/10 the size of the scroll view.
        let multiple = context.containerSize.width / 10.0
        let newX = (target.rect.origin.x / multiple).rounded() * multiple
        target.rect.origin.x = newX
    }
}
```

### Paging Behavior

SwiftUI offers built in scroll behaviors. One such behavior is the [PagingScrollTargetBehavior](pagingscrolltargetbehavior.md) which uses the geometry of the scroll view to decide where to allow scrolls to end.

In the following example, every view in the lazy stack is flexible in both directions and the scroll view will settle to container aligned boundaries.

```swift
ScrollView {
    LazyVStack(spacing: 0.0) {
        ForEach(items) { item in
            FullScreenItem(item)
        }
    }
}
.scrollTargetBehavior(.paging)
```

### View Aligned Behavior

SwiftUI also offers a [ViewAlignedScrollTargetBehavior](viewalignedscrolltargetbehavior.md) scroll behavior that will always settle on the geometry of individual views.

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
.safeAreaPadding(.horizontal, 20.0)
```

You configure which views should be used for settling using the [scrollTargetLayout(isEnabled:)](<view/scrolltargetlayout(isenabled_).md>) modifier. Apply this modifier to a layout container like [LazyVStack](lazyvstack.md) or [HStack](hstack.md) and each individual view in that layout will be considered for alignment.

Use types conforming to this protocol with the [scrollTargetBehavior(_:)](<view/scrolltargetbehavior(__).md>) modifier.

## Relationships

- **Conforming Types**: [AnyScrollTargetBehavior](anyscrolltargetbehavior.md), [PagingScrollTargetBehavior](pagingscrolltargetbehavior.md), [ViewAlignedScrollTargetBehavior](viewalignedscrolltargetbehavior.md)

## Topics

### Getting the scroll target behavior

- [paging](scrolltargetbehavior/paging.md) — The scroll behavior that aligns scroll targets to container-based geometry.
- [viewAligned](scrolltargetbehavior/viewaligned.md) — The scroll behavior that aligns scroll targets to view-based geometry.
- [viewAligned(limitBehavior:)](<scrolltargetbehavior/viewaligned(limitbehavior_).md>) — The scroll behavior that aligns scroll targets to view-based geometry.

### Updating the proposed target

- [updateTarget(_:context:)](<scrolltargetbehavior/updatetarget(__context_).md>) — Updates the proposed target that a scrollable view should scroll to.
- [TargetContext](scrolltargetbehavior/targetcontext.md) — The context in which a scroll behavior updates the scroll target.

### Instance Methods

- [properties(context:)](<scrolltargetbehavior/properties(context_).md>) — Properties of this behavior

### Type Aliases

- [Properties](scrolltargetbehavior/properties.md) — The properties of a scroll behavior
- [PropertiesContext](scrolltargetbehavior/propertiescontext.md) — The properties context of a scroll behavior.

### Type Methods

- [viewAligned(anchor:)](<scrolltargetbehavior/viewaligned(anchor_).md>) — The scroll behavior that aligns scroll targets to view-based geometry.
- [viewAligned(limitBehavior:anchor:)](<scrolltargetbehavior/viewaligned(limitbehavior_anchor_).md>) — The scroll behavior that aligns scroll targets to view-based geometry.

## See Also

### Defining scroll targets

- [scrollTargetBehavior(_:)](<view/scrolltargetbehavior(__).md>) — Sets the scroll behavior of views scrollable in the provided axes.
- [scrollTargetLayout(isEnabled:)](<view/scrolltargetlayout(isenabled_).md>) — Configures the outermost layout as a scroll target layout.
- [ScrollTarget](scrolltarget.md) — A type defining the target in which a scroll view should try and scroll to.
- [ScrollTargetBehaviorContext](scrolltargetbehaviorcontext.md) — The context in which a scroll target behavior updates its scroll target.
- [PagingScrollTargetBehavior](pagingscrolltargetbehavior.md) — The scroll behavior that aligns scroll targets to container-based geometry.
- [ViewAlignedScrollTargetBehavior](viewalignedscrolltargetbehavior.md) — The scroll behavior that aligns scroll targets to view-based geometry.
- [AnyScrollTargetBehavior](anyscrolltargetbehavior.md) — A type-erased scroll target behavior.
- [ScrollTargetBehaviorProperties](scrolltargetbehaviorproperties.md) — Properties influencing the scroll view a scroll target behavior applies to.
- [ScrollTargetBehaviorPropertiesContext](scrolltargetbehaviorpropertiescontext.md) — The context in which a scroll target behavior can decide its properties.
