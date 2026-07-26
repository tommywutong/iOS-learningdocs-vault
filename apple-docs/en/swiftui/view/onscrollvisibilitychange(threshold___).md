---
title: 'onScrollVisibilityChange(threshold:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/onscrollvisibilitychange(threshold:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/onscrollvisibilitychange(threshold:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/onscrollvisibilitychange%28threshold%3A_%3A%29.json'
content_hash: 'sha256:d183611352bd53b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onScrollVisibilityChange(threshold:_:)

<sub>Instance Method</sub>

Adds an action to be called when the view crosses the threshold to be considered on/off screen.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func onScrollVisibilityChange(threshold: Double = 0.5, _ action: @escaping (Bool) -> Void) -> some View

```

## Parameters

- `threshold` — The amount required to be visible within the viewport of the parent view before the `action` is fired. By default when the view has crossed more than 50% on-screen, the action will be called.

- `action` — The action which will be called when the threshold has been reached.

## Discussion

Use this modifier to be informed when the view has crossed the provided threshold to be considered on/off screen.

```swift
struct VideoPlayer: View {
    @State var playing: Bool

    var body: some View {
        Group {
            // ...
        }
        .onScrollVisibilityChange(threshold: 0.2) { isVisible in
            playing = isVisible
        }
    }
}
```

When the view appears on-screen, the action will be called if the threshold has already been reached.

## See Also

### Responding to scroll view changes

- [onScrollGeometryChange(for:of:action:)](<onscrollgeometrychange(for_of_action_).md>) — Adds an action to be performed when a value, created from a scroll geometry, changes.
- [onScrollTargetVisibilityChange(idType:threshold:_:)](<onscrolltargetvisibilitychange(idtype_threshold___).md>) — Adds an action to be called with information about what views would be considered visible.
- [onScrollPhaseChange(_:)](<onscrollphasechange(__).md>) — Adds an action to perform when the scroll phase of the first scroll view in the hierarchy changes.
- [ScrollGeometry](../scrollgeometry.md) — A type that defines the geometry of a scroll view.
- [ScrollPhase](../scrollphase.md) — A type that describes the state of a scroll gesture of a scrollable view like a scroll view.
- [ScrollPhaseChangeContext](../scrollphasechangecontext.md) — A type that provides you with more content when the phase of a scroll view changes.
