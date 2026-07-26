---
title: 'handActivationBehavior(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/gesture/handactivationbehavior(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/gesture/handactivationbehavior(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gesture/handactivationbehavior%28_%3A%29.json'
content_hash: 'sha256:23b343446c90af7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Gesture](../gesture.md)

# handActivationBehavior(_:)

<sub>Instance Method</sub>

Customizes the activation behavior for a gesture when driven by hand or hand-like input.

<sub>visionOS</sub>

```swift
@MainActor @preconcurrency func handActivationBehavior(_ behavior: HandActivationBehavior) -> some Gesture<Self.Value>

```

## Parameters

- `behavior` — The hand activation behavior to use for the gesture.

## Return Value

A new gesture with a preference to activate with the provided behavior.

## Discussion

Use [automatic](../handactivationbehavior/automatic.md) to allow a gesture to activate with default system behaviors. Use [pinch](../handactivationbehavior/pinch.md) when a gesture should only trigger when the hand is pinched.

For example, in a 3D chess application, a [DragGesture](../draggesture.md) that enables movement of the pieces could use the pinch behavior to ensure that piece movement is only possible when a hand is pinched in order to avoid pushing the piece around by only touching it:

```swift
Model3D(named: "Pawn")
    .gesture(
        DragGesture()
            .handActivationBehavior(.pinch)
            .updating($chessDragState) { value, state, _ in
                // ...
            }
    )
```
