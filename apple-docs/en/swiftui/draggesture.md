---
title: DragGesture
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/draggesture
source_url: 'https://developer.apple.com/documentation/swiftui/draggesture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/draggesture.json'
content_hash: 'sha256:6f9717ed92194f62'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DragGesture

<sub>Structure</sub>

A dragging motion that invokes an action as the drag-event sequence changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct DragGesture
```

## Overview

To recognize a drag gesture on a view, create and configure the gesture, and then add it to the view using the [gesture(_:including:)](<view/gesture(__including_).md>) modifier.

Add a drag gesture to a [Circle](circle.md) and change its color while the user performs the drag gesture:

```swift
struct DragGestureView: View {
    @State private var isDragging = false

    var drag: some Gesture {
        DragGesture()
            .onChanged { _ in self.isDragging = true }
            .onEnded { _ in self.isDragging = false }
    }

    var body: some View {
        Circle()
            .fill(self.isDragging ? Color.red : Color.blue)
            .frame(width: 100, height: 100, alignment: .center)
            .gesture(drag)
    }
}
```

## Relationships

- **Conforms To**: [Gesture](gesture.md)

## Topics

### Creating a drag gesture

- [init(minimumDistance:coordinateSpace:)](<draggesture/init(minimumdistance_coordinatespace_)-8ffe5.md>) — Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.
- [init(minimumDistance:coordinateSpace:)](<draggesture/init(minimumdistance_coordinatespace_).md>) — Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.
- [init(minimumDistance:coordinateSpace3D:)](<draggesture/init(minimumdistance_coordinatespace3d_).md>) — Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.
- [init(minimumDistance:coordinateSpace:inputKinds:)](<draggesture/init(minimumdistance_coordinatespace_inputkinds_).md>) — Creates a dragging gesture with the minimum dragging distance before the gesture succeeds, the coordinate space of the gesture’s location, and the input kinds the gesture recognizes. _(beta)_
- [minimumDistance](draggesture/minimumdistance.md) — The minimum dragging distance before the gesture succeeds.
- [coordinateSpace](draggesture/coordinatespace.md) — The coordinate space in which to receive location values.

### Getting the gesture’s value

- [Value](draggesture/value.md) — The attributes of a drag gesture.

### Deprecated initializers

- [init(minimumDistance:coordinateSpace:)](<draggesture/init(minimumdistance_coordinatespace_)-3804h.md>) — Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location. _(deprecated)_

## See Also

### Recognizing gestures that change over time

- [gesture(_:)](<view/gesture(__).md>) — Attaches an [NSGestureRecognizerRepresentable](nsgesturerecognizerrepresentable.md) to the view.
- [gesture(_:isEnabled:)](<view/gesture(__isenabled_).md>) — Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [gesture(_:name:isEnabled:)](<view/gesture(__name_isenabled_).md>) — Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [gesture(_:including:)](<view/gesture(__including_).md>) — Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [WindowDragGesture](windowdraggesture.md) — A gesture that recognizes the motion of and handles dragging a window.
- [MagnifyGesture](magnifygesture.md) — A gesture that recognizes a magnification motion and tracks the amount of magnification.
- [RotateGesture](rotategesture.md) — A gesture that recognizes a rotation motion and tracks the angle of the rotation.
- [RotateGesture3D](rotategesture3d.md) — A gesture that recognizes 3D rotation motion and tracks the angle and axis of the rotation.
- [GestureMask](gesturemask.md) — Options that control how adding a gesture to a view affects other gestures recognized by the view and its subviews.
