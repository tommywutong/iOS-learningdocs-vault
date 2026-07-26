---
title: 'onScrollPhaseChange(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/onscrollphasechange(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/onscrollphasechange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/onscrollphasechange%28_%3A%29.json'
content_hash: 'sha256:c36cf78a004ac805'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onScrollPhaseChange(_:)

<sub>Instance Method</sub>

Adds an action to perform when the scroll phase of the first scroll view in the hierarchy changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func onScrollPhaseChange(_ action: @escaping (ScrollPhase, ScrollPhase) -> Void) -> some View

```

## Parameters

- `action` — A closure to run when the scroll phase changes. - **oldPhase** — The old scroll phase. - **newPhase** — The new scroll phase.

## Discussion

Use this modifier to be informed of changes to a scroll view’s phase. A scroll view may be in a variety of different phases like panning or decelerating. See [ScrollPhase](../scrollphase.md) for more information on the phases of a scroll view.

When the phase of a scroll view changes, the system invokes the action you provide. In the following example, a selection binding is updated when the scroll view transitions to the [ScrollPhase.decelerating](../scrollphase/decelerating.md) or [ScrollPhase.idle](../scrollphase/idle.md) phase.

```swift
@Binding var selection: SelectionValue?

ScrollView {
    // ...
}
.onScrollPhaseChange { _, newPhase in
    if newPhase == .decelerating || newPhase == .idle {
        selection = updateSelection()
    }
}
```

The system can also provide you with the geometry of the scroll view at the time of the phase change. You can use the geometry to understand where the scroll view has come or gone between the phase changes and update dependent state on that information. In the following example, whether toolbar content is hidden is determined based on the direction of the last user initiated scroll.

```swift
@Binding var hidesToolbarContent: Bool
@State private var lastOffset: CGFloat = 0.0

ScrollView {
    // ...
}
.onScrollPhaseChange { oldPhase, newPhase, context in
    if newPhase == .interacting {
        lastOffset = context.geometry.contentOffset.y
    }
    if oldPhase == .interacting, newPhase != .animating,
        context.geometry.contentOffset.y - lastOffset < 0.0
    {
        hidesToolbarContent = true
    } else {
        hidesToolbarContent = false
    }
}
```

If multiple scroll views are found within the view hierarchy, only the first one will invoke the closure you provide and a runtime issue will be logged. For example, in the following view, only the vertical scroll view will have its phase changes invoke the provided closure.

```swift
VStack {
    ScrollView(.vertical) { ... }
    ScrollView(.horizontal) { ... }
}
.onScrollPhaseChange { ... }
```

## See Also

### Responding to scroll view changes

- [onScrollGeometryChange(for:of:action:)](<onscrollgeometrychange(for_of_action_).md>) — Adds an action to be performed when a value, created from a scroll geometry, changes.
- [onScrollTargetVisibilityChange(idType:threshold:_:)](<onscrolltargetvisibilitychange(idtype_threshold___).md>) — Adds an action to be called with information about what views would be considered visible.
- [onScrollVisibilityChange(threshold:_:)](<onscrollvisibilitychange(threshold___).md>) — Adds an action to be called when the view crosses the threshold to be considered on/off screen.
- [ScrollGeometry](../scrollgeometry.md) — A type that defines the geometry of a scroll view.
- [ScrollPhase](../scrollphase.md) — A type that describes the state of a scroll gesture of a scrollable view like a scroll view.
- [ScrollPhaseChangeContext](../scrollphasechangecontext.md) — A type that provides you with more content when the phase of a scroll view changes.
