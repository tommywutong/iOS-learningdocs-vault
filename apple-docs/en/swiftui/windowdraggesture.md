---
title: WindowDragGesture
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/windowdraggesture
source_url: 'https://developer.apple.com/documentation/swiftui/windowdraggesture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowdraggesture.json'
content_hash: 'sha256:07e3d28b2bd18e60'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# WindowDragGesture

<sub>Structure</sub>

A gesture that recognizes the motion of and handles dragging a window.

<sub>macOS</sub>

```swift
nonisolated struct WindowDragGesture
```

## Overview

To recognize a window drag gesture on a view, create and configure the gesture, and then add it to the view using the [gesture(_:isEnabled:)](<view/gesture(__isenabled_).md>) modifier. Consider also letting the gesture [handle events that activate the containing window](<view/allowswindowactivationevents(__).md>) so that dragging the containing window works even when it’s inactive.

To add a window drag gesture to a [Circle](circle.md) and change its color while a user performs the window drag gesture:

```swift
struct MyView: View {
    @GestureState var isDraggingWindow = false

    var dragWindow: some Gesture {
        WindowDragGesture()
            .updating($isDraggingWindow) { _, state, _ in
                state = true
            }
    }

    var body: some View {
        Circle()
            .fill(isDraggingWindow ? Color.green : .blue)
            .frame(width: 50, height: 50)
            .gesture(dragWindow)
            .allowsWindowActivationEvents()
    }
}
```

## Relationships

- **Conforms To**: [Gesture](gesture.md)

## Topics

### Creating a window drag gesture

- [init()](<windowdraggesture/init().md>) — Creates a window drag gesture.

### Getting the gesture’s value

- [Value](windowdraggesture/value.md) — The properties of a window drag gesture.

## See Also

### Recognizing gestures that change over time

- [gesture(_:)](<view/gesture(__).md>) — Attaches an [NSGestureRecognizerRepresentable](nsgesturerecognizerrepresentable.md) to the view.
- [gesture(_:isEnabled:)](<view/gesture(__isenabled_).md>) — Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [gesture(_:name:isEnabled:)](<view/gesture(__name_isenabled_).md>) — Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [gesture(_:including:)](<view/gesture(__including_).md>) — Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [DragGesture](draggesture.md) — A dragging motion that invokes an action as the drag-event sequence changes.
- [MagnifyGesture](magnifygesture.md) — A gesture that recognizes a magnification motion and tracks the amount of magnification.
- [RotateGesture](rotategesture.md) — A gesture that recognizes a rotation motion and tracks the angle of the rotation.
- [RotateGesture3D](rotategesture3d.md) — A gesture that recognizes 3D rotation motion and tracks the angle and axis of the rotation.
- [GestureMask](gesturemask.md) — Options that control how adding a gesture to a view affects other gestures recognized by the view and its subviews.
