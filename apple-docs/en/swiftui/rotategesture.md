---
title: RotateGesture
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/rotategesture
source_url: 'https://developer.apple.com/documentation/swiftui/rotategesture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/rotategesture.json'
content_hash: 'sha256:c58efe1d7f90a72b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# RotateGesture

<sub>Structure</sub>

A gesture that recognizes a rotation motion and tracks the angle of the rotation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated struct RotateGesture
```

## Overview

A rotate gesture tracks how a rotation event sequence changes. To recognize a rotate gesture on a view, create and configure the gesture, and then add it to the view using the [gesture(_:including:)](<view/gesture(__including_).md>) modifier.

Add a rotate gesture to a [Rectangle](rectangle.md) and apply a rotation effect:

```swift
struct RotateGestureView: View {
    @State private var angle = Angle(degrees: 0.0)

    var rotation: some Gesture {
        RotateGesture()
            .onChanged { value in
                angle = value.rotation
            }
    }

    var body: some View {
        Rectangle()
            .frame(width: 200, height: 200, alignment: .center)
            .rotationEffect(angle)
            .gesture(rotation)
    }
}
```

## Relationships

- **Conforms To**: [Gesture](gesture.md)

## Topics

### Creating the gesture

- [init(minimumAngleDelta:)](<rotategesture/init(minimumangledelta_).md>) — Creates a rotation gesture with a minimum delta for the gesture to start.
- [init(minimumAngleDelta:inputKinds:)](<rotategesture/init(minimumangledelta_inputkinds_).md>) — Creates a rotation gesture with a minimum delta for the gesture to start, and the input kinds the gesture recognizes. _(beta)_
- [minimumAngleDelta](rotategesture/minimumangledelta.md) — The minimum delta required before the gesture succeeds.

## See Also

### Recognizing gestures that change over time

- [gesture(_:)](<view/gesture(__).md>) — Attaches an [NSGestureRecognizerRepresentable](nsgesturerecognizerrepresentable.md) to the view.
- [gesture(_:isEnabled:)](<view/gesture(__isenabled_).md>) — Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [gesture(_:name:isEnabled:)](<view/gesture(__name_isenabled_).md>) — Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [gesture(_:including:)](<view/gesture(__including_).md>) — Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [DragGesture](draggesture.md) — A dragging motion that invokes an action as the drag-event sequence changes.
- [WindowDragGesture](windowdraggesture.md) — A gesture that recognizes the motion of and handles dragging a window.
- [MagnifyGesture](magnifygesture.md) — A gesture that recognizes a magnification motion and tracks the amount of magnification.
- [RotateGesture3D](rotategesture3d.md) — A gesture that recognizes 3D rotation motion and tracks the angle and axis of the rotation.
- [GestureMask](gesturemask.md) — Options that control how adding a gesture to a view affects other gestures recognized by the view and its subviews.
