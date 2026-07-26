---
title: 'onContinuousHover(coordinateSpace:perform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/oncontinuoushover(coordinatespace:perform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/oncontinuoushover(coordinatespace:perform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/oncontinuoushover%28coordinatespace%3Aperform%3A%29.json'
content_hash: 'sha256:1649cda952492656'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onContinuousHover(coordinateSpace:perform:)

<sub>Instance Method</sub>

Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated func onContinuousHover(coordinateSpace: some CoordinateSpaceProtocol = .local, perform action: @escaping (HoverPhase) -> Void) -> some View

```

## Parameters

- `coordinateSpace` — The coordinate space for the location values. The default value is [CoordinateSpace.local](../coordinatespace/local.md).

- `action` — The action to perform whenever the pointer enters, moves within, or exits the view’s bounds. The closure takes a `phase` input that has the value [HoverPhase.active(_:)](<../hoverphase/active(__).md>) and contains the pointer’s coordinates if the pointer is within the view’s bounds. The closure receives the [HoverPhase.ended](../hoverphase/ended.md) phase when the pointer leaves the view’s bounds.

## Return Value

A view that calls `action` when the pointer enters, moves within, or exits the view’s bounds.

## Discussion

Use this modifier to define a region for detecting pointer movement with a view. The following example updates a small rectangle’s position and style by modifying `hoverLocation` and `isHovering` as the pointer moves within the larger, red rectangle:

```swift
@State private var hoverLocation: CGPoint = .zero
@State private var isHovering = false

var body: some View {
    Color.red
        .frame(width: 400, height: 400)
        .onContinuousHover { phase in
            switch phase {
            case .active(let location):
                hoverLocation = location
                isHovering = true
            case .ended:
                isHovering = false
            }
        }
        .overlay {
            Rectangle()
                .frame(width: 50, height: 50)
                .foregroundStyle(isHovering ? .green : .blue)
                .offset(x: hoverLocation.x, y: hoverLocation.y)
        }
}
```

## See Also

### Responding to hover events

- [onHover(perform:)](<onhover(perform_).md>) — Adds an action to perform when the user moves the pointer over or away from the view’s frame.
- [hoverEffect(_:isEnabled:)](<hovereffect(__isenabled_).md>) — Applies a hover effect to this view.
- [hoverEffectDisabled(_:)](<hovereffectdisabled(__).md>) — Adds a condition that controls whether this view can display hover effects.
- [defaultHoverEffect(_:)](<defaulthovereffect(__).md>) — Sets the default hover effect to use for views within this view.
- [isHoverEffectEnabled](../environmentvalues/ishovereffectenabled.md) — A Boolean value that indicates whether the view associated with this environment allows hover effects to be displayed.
- [HoverPhase](../hoverphase.md) — The current hovering state and value of the pointer.
- [HoverEffectPhaseOverride](../hovereffectphaseoverride.md) — Options for overriding a hover effect’s current phase.
- [OrnamentHoverContentEffect](../ornamenthovercontenteffect.md) — Presents an ornament on hover using a custom effect.
- [OrnamentHoverEffect](../ornamenthovereffect.md) — Presents an ornament on hover.
