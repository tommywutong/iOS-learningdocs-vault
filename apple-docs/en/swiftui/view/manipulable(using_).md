---
title: 'manipulable(using:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/manipulable(using:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/manipulable(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/manipulable%28using%3A%29.json'
content_hash: 'sha256:077a0b96e3bd5f24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# manipulable(using:)

<sub>Instance Method</sub>

Allows the view to be manipulated using a manipulation gesture attached to a different view.

<sub>visionOS</sub>

```swift
@export(implementation) nonisolated func manipulable(using gestureState: Manipulable.GestureState) -> some View

```

## Parameters

- `gestureState` — The manipulation gesture state that’s updated by a manipulation gesture added to a different view.

## Return Value

A view that can be manipulated by a manipulation gesture attached to a different view.

## Discussion

Use this view modifier alongside [manipulationGesture(updating:coordinateSpace:operations:inertia:isEnabled:onChanged:)](<manipulationgesture(updating_coordinatespace_operations_inertia_isenabled_onchanged_).md>) when you want to allow a person to manipulate a view by interacting with a different view.

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
> [manipulationGesture(updating:coordinateSpace:operations:inertia:isEnabled:onChanged:)](<manipulationgesture(updating_coordinatespace_operations_inertia_isenabled_onchanged_).md>)

## See Also

### Hand interactions

- [handGestureShortcut(_:isEnabled:)](<handgestureshortcut(__isenabled_).md>) — Assigns a hand gesture shortcut to the modified control.
- [handPointerBehavior(_:)](<handpointerbehavior(__).md>) — Sets the behavior of the hand pointer while the user is interacting with the view.
- [manipulable(coordinateSpace:operations:inertia:isEnabled:onChanged:)](<manipulable(coordinatespace_operations_inertia_isenabled_onchanged_).md>) — Allows this view to be manipulated using common hand gestures.
- [manipulable(transform:coordinateSpace:operations:inertia:isEnabled:onChanged:)](<manipulable(transform_coordinatespace_operations_inertia_isenabled_onchanged_).md>) — Applies the given 3D affine transform to the view and allows it to be manipulated using common hand gestures.
- [manipulationGesture(updating:coordinateSpace:operations:inertia:isEnabled:onChanged:)](<manipulationgesture(updating_coordinatespace_operations_inertia_isenabled_onchanged_).md>) — Adds a manipulation gesture to this view without allowing this view to be manipulable itself.
