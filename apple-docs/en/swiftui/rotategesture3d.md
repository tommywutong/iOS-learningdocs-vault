---
title: RotateGesture3D
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/rotategesture3d
source_url: 'https://developer.apple.com/documentation/swiftui/rotategesture3d'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/rotategesture3d.json'
content_hash: 'sha256:2b7c5223722ecc2f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# RotateGesture3D

<sub>Structure</sub>

A gesture that recognizes 3D rotation motion and tracks the angle and axis of the rotation.

<sub>visionOS</sub>

```swift
nonisolated struct RotateGesture3D
```

## Overview

You can constrain this gesture to recognize rotation about a specific 3D axis. For example, `RotateGesture3D(constrainedToAxis: .x)` creates a gesture that recognizes rotation only around the global X axis. The axis you provide will be normalized.

A rotation gesture tracks how a rotation event sequence changes. To recognize a rotation gesture on a view, create and configure the gesture, and then add it to the view using the [gesture(_:including:)](<view/gesture(__including_).md>) modifier.

## Relationships

- **Conforms To**: [Gesture](gesture.md)

## Topics

### Creating the gesture

- [init(constrainedToAxis:minimumAngleDelta:)](<rotategesture3d/init(constrainedtoaxis_minimumangledelta_).md>) — Creates a rotation gesture with a minimum delta for the gesture to start and axis to constrain measurement of rotation.
- [init(constrainedToAxis:minimumAngleDelta:inputKinds:)](<rotategesture3d/init(constrainedtoaxis_minimumangledelta_inputkinds_).md>) — Creates a rotation gesture with a minimum delta for the gesture to start, an axis to constrain measurement of rotation, and the input kinds the gesture should recognize.
- [minimumAngleDelta](rotategesture3d/minimumangledelta.md) — The minimum angle delta before the gesture becomes active.
- [constrainedAxis](rotategesture3d/constrainedaxis.md) — An axis around which the rotation is constrained.

## See Also

### Recognizing gestures that change over time

- [gesture(_:)](<view/gesture(__).md>) — Attaches an [NSGestureRecognizerRepresentable](nsgesturerecognizerrepresentable.md) to the view.
- [gesture(_:isEnabled:)](<view/gesture(__isenabled_).md>) — Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [gesture(_:name:isEnabled:)](<view/gesture(__name_isenabled_).md>) — Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [gesture(_:including:)](<view/gesture(__including_).md>) — Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [DragGesture](draggesture.md) — A dragging motion that invokes an action as the drag-event sequence changes.
- [WindowDragGesture](windowdraggesture.md) — A gesture that recognizes the motion of and handles dragging a window.
- [MagnifyGesture](magnifygesture.md) — A gesture that recognizes a magnification motion and tracks the amount of magnification.
- [RotateGesture](rotategesture.md) — A gesture that recognizes a rotation motion and tracks the angle of the rotation.
- [GestureMask](gesturemask.md) — Options that control how adding a gesture to a view affects other gestures recognized by the view and its subviews.
