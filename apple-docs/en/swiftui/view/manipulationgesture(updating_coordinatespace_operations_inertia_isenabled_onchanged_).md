---
title: 'manipulationGesture(updating:coordinateSpace:operations:inertia:isEnabled:onChanged:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/manipulationgesture(updating:coordinatespace:operations:inertia:isenabled:onchanged:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/manipulationgesture(updating:coordinatespace:operations:inertia:isenabled:onchanged:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/manipulationgesture%28updating%3Acoordinatespace%3Aoperations%3Ainertia%3Aisenabled%3Aonchanged%3A%29.json'
content_hash: 'sha256:0d446b713311e3a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# manipulationGesture(updating:coordinateSpace:operations:inertia:isEnabled:onChanged:)

<sub>Instance Method</sub>

Adds a manipulation gesture to this view without allowing this view to be manipulable itself.

<sub>visionOS</sub>

```swift
@export(implementation) nonisolated func manipulationGesture(updating gestureState: Binding<Manipulable.GestureState>, coordinateSpace: some CoordinateSpaceProtocol = .local, operations: Manipulable.Operation.Set = .all, inertia: Manipulable.Inertia = .medium, isEnabled: Bool = true, onChanged: ((Manipulable.Event) -> Void)? = nil) -> some View

```

## Parameters

- `gestureState` — The state that the manipulation gesture updates.

- `coordinateSpace` — The coordinate space of the manipulation gesture event locations.

- `operations` — The set of allowed operations that can be applied when a person manipulates this view.

- `inertia` — The inertia of this view that defines how much it resists being manipulated.

- `isEnabled` — The Boolean value that indicates whether the manipulation gesture added by this view modifier is enabled or not.

- `onChanged` — The action to perform with each new manipulation gesture event.

## Return Value

A view with a manipulation gesture attached but that isn’t manipulable itself.

## Discussion

Use this view modifier alongside [manipulable(using:)](<manipulable(using_).md>) when you want to allow a person to manipulate a view by interacting with a different view.

In the following example, a person can begin a manipulation gesture attached to a deck of cards which, in turn, manipulates a single card instead of the entire deck:

```swift
struct CardDeck: View {
    @State private var manipulationState = Manipulable.GestureState()

    var body: some View {
        ZStack {
            Model3D(named: "CardDeck")
                .manipulationGesture(updating: $manipulationState)
            Model3D(named: "Card")
                .manipulable(using: manipulationState)
                .opacity(manipulationState.isActive ? 1 : 0)
        }
    }
}
```

> [!info] See Also
> [manipulable(using:)](<manipulable(using_).md>)

## See Also

### Hand interactions

- [handGestureShortcut(_:isEnabled:)](<handgestureshortcut(__isenabled_).md>) — Assigns a hand gesture shortcut to the modified control.
- [handPointerBehavior(_:)](<handpointerbehavior(__).md>) — Sets the behavior of the hand pointer while the user is interacting with the view.
- [manipulable(coordinateSpace:operations:inertia:isEnabled:onChanged:)](<manipulable(coordinatespace_operations_inertia_isenabled_onchanged_).md>) — Allows this view to be manipulated using common hand gestures.
- [manipulable(transform:coordinateSpace:operations:inertia:isEnabled:onChanged:)](<manipulable(transform_coordinatespace_operations_inertia_isenabled_onchanged_).md>) — Applies the given 3D affine transform to the view and allows it to be manipulated using common hand gestures.
- [manipulable(using:)](<manipulable(using_).md>) — Allows the view to be manipulated using a manipulation gesture attached to a different view.
