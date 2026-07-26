---
title: 'init(constrainedToAxis:minimumAngleDelta:inputKinds:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/rotategesture3d/init(constrainedtoaxis:minimumangledelta:inputkinds:)'
source_url: 'https://developer.apple.com/documentation/swiftui/rotategesture3d/init(constrainedtoaxis:minimumangledelta:inputkinds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/rotategesture3d/init%28constrainedtoaxis%3Aminimumangledelta%3Ainputkinds%3A%29.json'
content_hash: 'sha256:777f08eaeac11b50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [RotateGesture3D](../rotategesture3d.md)

# init(constrainedToAxis:minimumAngleDelta:inputKinds:)

<sub>Initializer</sub>

Creates a rotation gesture with a minimum delta for the gesture to start, an axis to constrain measurement of rotation, and the input kinds the gesture should recognize.

<sub>visionOS</sub>

```swift
nonisolated init(constrainedToAxis: RotationAxis3D? = nil, minimumAngleDelta: Angle = .degrees(1), inputKinds: GestureInputKinds = .all)
```

## Parameters

- `constrainedToAxis` — The 3D axis about which rotation is measured.

- `minimumAngleDelta` — The minimum delta required before the gesture starts. The default value is a one-degree angle.

- `inputKinds` — A set of input kinds that this gesture recognizes. If not specified, the gesture will recognize all applicable input kinds that a person can use to perform it.

## Discussion

If the constrained axis is `nil`, the gesture measures unconstrained 3D rotation.

## See Also

### Creating the gesture

- [init(constrainedToAxis:minimumAngleDelta:)](<init(constrainedtoaxis_minimumangledelta_).md>) — Creates a rotation gesture with a minimum delta for the gesture to start and axis to constrain measurement of rotation.
- [minimumAngleDelta](minimumangledelta.md) — The minimum angle delta before the gesture becomes active.
- [constrainedAxis](constrainedaxis.md) — An axis around which the rotation is constrained.
