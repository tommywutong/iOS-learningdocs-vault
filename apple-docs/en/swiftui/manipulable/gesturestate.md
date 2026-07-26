---
title: Manipulable.GestureState
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/manipulable/gesturestate
source_url: 'https://developer.apple.com/documentation/swiftui/manipulable/gesturestate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/manipulable/gesturestate.json'
content_hash: 'sha256:50f947805345c322'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Manipulable](../manipulable.md)

# Manipulable.GestureState

<sub>Structure</sub>

Describes the state of a manipulation gesture.

<sub>visionOS</sub>

```swift
struct GestureState
```

## Overview

> [!info] See Also
> [manipulationGesture(updating:coordinateSpace:operations:inertia:isEnabled:onChanged:)](<../view/manipulationgesture(updating_coordinatespace_operations_inertia_isenabled_onchanged_).md>)

> [!info] See Also
> [manipulable(using:)](<../view/manipulable(using_).md>)

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(transform:)](<gesturestate/init(transform_).md>) — Creates a new manipulation gesture state with the given transform.

### Instance Properties

- [isActive](gesturestate/isactive.md) — The Boolean value that indicates whether a manipulation gesture is currently active.
- [transform](gesturestate/transform.md) — The current 3D affine transform applied by an active manipulation gesture.
