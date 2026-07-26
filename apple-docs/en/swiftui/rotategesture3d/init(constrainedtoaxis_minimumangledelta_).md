---
title: 'init(constrainedToAxis:minimumAngleDelta:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/rotategesture3d/init(constrainedtoaxis:minimumangledelta:)'
source_url: 'https://developer.apple.com/documentation/swiftui/rotategesture3d/init(constrainedtoaxis:minimumangledelta:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/rotategesture3d/init%28constrainedtoaxis%3Aminimumangledelta%3A%29.json'
content_hash: 'sha256:700add9e03f15afc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [RotateGesture3D](../rotategesture3d.md)

# init(constrainedToAxis:minimumAngleDelta:)

<sub>Initializer</sub>

Creates a rotation gesture with a minimum delta for the gesture to start and axis to constrain measurement of rotation.

<sub>visionOS</sub>

```swift
nonisolated init(constrainedToAxis: RotationAxis3D? = nil, minimumAngleDelta: Angle = .degrees(1))
```

## Parameters

- `constrainedToAxis` — The 3D axis about which rotation is measured.

- `minimumAngleDelta` — The minimum delta required before the gesture starts. The default value is a one-degree angle.

## Discussion

If the constrained axis is `nil`, the gesture measures unconstrained 3D rotation.

## See Also

### Creating the gesture

- [init(constrainedToAxis:minimumAngleDelta:inputKinds:)](<init(constrainedtoaxis_minimumangledelta_inputkinds_).md>) — Creates a rotation gesture with a minimum delta for the gesture to start, an axis to constrain measurement of rotation, and the input kinds the gesture should recognize.
- [minimumAngleDelta](minimumangledelta.md) — The minimum angle delta before the gesture becomes active.
- [constrainedAxis](constrainedaxis.md) — An axis around which the rotation is constrained.
