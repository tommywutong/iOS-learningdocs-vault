---
title: constrainedAxis
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/rotategesture3d/constrainedaxis
source_url: 'https://developer.apple.com/documentation/swiftui/rotategesture3d/constrainedaxis'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/rotategesture3d/constrainedaxis.json'
content_hash: 'sha256:8730969b7315e2f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [RotateGesture3D](../rotategesture3d.md)

# constrainedAxis

<sub>Instance Property</sub>

An axis around which the rotation is constrained.

<sub>visionOS</sub>

```swift
var constrainedAxis: RotationAxis3D?
```

## Discussion

If the axis is `nil`, the rotation is unconstrained.

## See Also

### Creating the gesture

- [init(constrainedToAxis:minimumAngleDelta:)](<init(constrainedtoaxis_minimumangledelta_).md>) — Creates a rotation gesture with a minimum delta for the gesture to start and axis to constrain measurement of rotation.
- [init(constrainedToAxis:minimumAngleDelta:inputKinds:)](<init(constrainedtoaxis_minimumangledelta_inputkinds_).md>) — Creates a rotation gesture with a minimum delta for the gesture to start, an axis to constrain measurement of rotation, and the input kinds the gesture should recognize.
- [minimumAngleDelta](minimumangledelta.md) — The minimum angle delta before the gesture becomes active.
