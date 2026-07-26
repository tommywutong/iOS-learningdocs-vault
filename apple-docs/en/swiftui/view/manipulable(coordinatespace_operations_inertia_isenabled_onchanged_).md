---
title: 'manipulable(coordinateSpace:operations:inertia:isEnabled:onChanged:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/manipulable(coordinatespace:operations:inertia:isenabled:onchanged:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/manipulable(coordinatespace:operations:inertia:isenabled:onchanged:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/manipulable%28coordinatespace%3Aoperations%3Ainertia%3Aisenabled%3Aonchanged%3A%29.json'
content_hash: 'sha256:89453f7e325ccd43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# manipulable(coordinateSpace:operations:inertia:isEnabled:onChanged:)

<sub>Instance Method</sub>

Allows this view to be manipulated using common hand gestures.

<sub>visionOS</sub>

```swift
@export(implementation) nonisolated func manipulable(coordinateSpace: some CoordinateSpaceProtocol = .local, operations: Manipulable.Operation.Set = .all, inertia: Manipulable.Inertia = .medium, isEnabled: Bool = true, onChanged: ((Manipulable.Event) -> Void)? = nil) -> some View

```

## Parameters

- `coordinateSpace` — The coordinate space of the manipulation gesture event locations.

- `operations` — The set of allowed operations that can be applied when a person manipulates this view.

- `inertia` — The inertia of this view that defines how much it resists being manipulated.

- `isEnabled` — The Boolean value that indicates whether the manipulation gesture added by this view modifier is enabled or not.

- `onChanged` — The action to perform with each new manipulation gesture event.

## Return Value

A view that can be manipulated using common hand gestures.

## Discussion

When a person ends the manipulation gesture, the view will return to its initial transform from before the gesture began.

```swift
Model3D(named: "ToyRocket")
    .manipulable()
```

## See Also

### Hand interactions

- [handGestureShortcut(_:isEnabled:)](<handgestureshortcut(__isenabled_).md>) — Assigns a hand gesture shortcut to the modified control.
- [handPointerBehavior(_:)](<handpointerbehavior(__).md>) — Sets the behavior of the hand pointer while the user is interacting with the view.
- [manipulable(transform:coordinateSpace:operations:inertia:isEnabled:onChanged:)](<manipulable(transform_coordinatespace_operations_inertia_isenabled_onchanged_).md>) — Applies the given 3D affine transform to the view and allows it to be manipulated using common hand gestures.
- [manipulable(using:)](<manipulable(using_).md>) — Allows the view to be manipulated using a manipulation gesture attached to a different view.
- [manipulationGesture(updating:coordinateSpace:operations:inertia:isEnabled:onChanged:)](<manipulationgesture(updating_coordinatespace_operations_inertia_isenabled_onchanged_).md>) — Adds a manipulation gesture to this view without allowing this view to be manipulable itself.
