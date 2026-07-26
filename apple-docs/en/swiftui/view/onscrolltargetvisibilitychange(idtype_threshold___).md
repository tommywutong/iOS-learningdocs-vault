---
title: 'onScrollTargetVisibilityChange(idType:threshold:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/onscrolltargetvisibilitychange(idtype:threshold:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/onscrolltargetvisibilitychange(idtype:threshold:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/onscrolltargetvisibilitychange%28idtype%3Athreshold%3A_%3A%29.json'
content_hash: 'sha256:e1793fd61947005d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onScrollTargetVisibilityChange(idType:threshold:_:)

<sub>Instance Method</sub>

Adds an action to be called with information about what views would be considered visible.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func onScrollTargetVisibilityChange<ID>(idType: ID.Type, threshold: Double = 0.5, _ action: @escaping ([ID]) -> Void) -> some View where ID : Hashable

```

## Parameters

- `idType` — The type of Identity provided by the subviews.

- `threshold` — The amount required to be visible within the viewport of the the scrollview before the `action` is fired.  By default when the view has crossed more than 50% on-screen, the action will be called.

- `action` — The action which will be called when the views within the scroll view cross the provided threshold. The callback will include which views are considered visible.

## Discussion

Use this modifier along with the modifier `View/scrollTargetLayout()` to be informed when the views in the targetted scroll view have crossed the provided threshold to be considered on/off screen.

```swift
ScrollView {
    LazyVStack {
        ForEach(models) { model in
            CardView(model: model)
        }
    }
    .scrollTargetLayout()
}
.onScrollTargetVisibilityChange(for: Model.ID.self, threshold: 0.2) { onScreenCards in
    // Disable video playback for cards that are offscreen...
}
```

## See Also

### Responding to scroll view changes

- [onScrollGeometryChange(for:of:action:)](<onscrollgeometrychange(for_of_action_).md>) — Adds an action to be performed when a value, created from a scroll geometry, changes.
- [onScrollVisibilityChange(threshold:_:)](<onscrollvisibilitychange(threshold___).md>) — Adds an action to be called when the view crosses the threshold to be considered on/off screen.
- [onScrollPhaseChange(_:)](<onscrollphasechange(__).md>) — Adds an action to perform when the scroll phase of the first scroll view in the hierarchy changes.
- [ScrollGeometry](../scrollgeometry.md) — A type that defines the geometry of a scroll view.
- [ScrollPhase](../scrollphase.md) — A type that describes the state of a scroll gesture of a scrollable view like a scroll view.
- [ScrollPhaseChangeContext](../scrollphasechangecontext.md) — A type that provides you with more content when the phase of a scroll view changes.
