---
title: Manipulable
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/manipulable
source_url: 'https://developer.apple.com/documentation/swiftui/manipulable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/manipulable.json'
content_hash: 'sha256:4481d63ba17b3590'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Manipulable

<sub>Enumeration</sub>

A namespace for various manipulable related types.

<sub>visionOS</sub>

```swift
enum Manipulable
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Structures

- [Event](manipulable/event.md) — Describes an event generated during a manipulation gesture.
- [GestureState](manipulable/gesturestate.md) — Describes the state of a manipulation gesture.
- [Inertia](manipulable/inertia.md) — Describes inertia of a view that defines how much a view resists being manipulated.
- [InputDevice](manipulable/inputdevice.md) — Describes an input device like a hand or a trackpad.
- [Operation](manipulable/operation.md) — Describes an operation applied to a view when a person is manipulating a view.

## See Also

### Modifying a view

- [Configuring views](configuring-views.md) — Adjust the characteristics of a view by applying view modifiers.
- [Reducing view modifier maintenance](reducing-view-modifier-maintenance.md) — Bundle view modifiers that you regularly reuse into a custom view modifier.
- [modifier(_:)](<view/modifier(__).md>) — Applies a modifier to a view and returns a new view.
- [ViewModifier](viewmodifier.md) — A modifier that you apply to a view or another view modifier, producing a different version of the original value.
- [EmptyModifier](emptymodifier.md) — An empty, or identity, modifier, used during development to switch modifiers at compile time.
- [ModifiedContent](modifiedcontent.md) — A value with a modifier applied to it.
- [EnvironmentalModifier](environmentalmodifier.md) — A modifier that must resolve to a concrete modifier in an environment before use.
- [ManipulableModifier](manipulablemodifier.md)
- [ManipulableResponderModifier](manipulablerespondermodifier.md)
- [ManipulableTransformBindingModifier](manipulabletransformbindingmodifier.md)
- [ManipulationGeometryModifier](manipulationgeometrymodifier.md)
- [ManipulationGestureModifier](manipulationgesturemodifier.md)
- [ManipulationUsingGestureStateModifier](manipulationusinggesturestatemodifier.md)
