---
title: 'gesture(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/gesture(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/gesture(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/gesture%28_%3A%29.json'
content_hash: 'sha256:60faa2efbff2472d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# gesture(_:)

<sub>Instance Method</sub>

Attaches an [NSGestureRecognizerRepresentable](../nsgesturerecognizerrepresentable.md) to the view.

<sub>macOS</sub>

```swift
nonisolated func gesture(_ representable: some NSGestureRecognizerRepresentable) -> some View

```

## Parameters

- `representable` — The [NSGestureRecognizerRepresentable](../nsgesturerecognizerrepresentable.md) that creates and manages a gesture recognizer.

## Return Value

A view with an [NSGestureRecognizerRepresentable](../nsgesturerecognizerrepresentable.md) attached.

## See Also

### Recognizing gestures that change over time

- [gesture(_:isEnabled:)](<gesture(__isenabled_).md>) — Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [gesture(_:name:isEnabled:)](<gesture(__name_isenabled_).md>) — Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [gesture(_:including:)](<gesture(__including_).md>) — Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [DragGesture](../draggesture.md) — A dragging motion that invokes an action as the drag-event sequence changes.
- [WindowDragGesture](../windowdraggesture.md) — A gesture that recognizes the motion of and handles dragging a window.
- [MagnifyGesture](../magnifygesture.md) — A gesture that recognizes a magnification motion and tracks the amount of magnification.
- [RotateGesture](../rotategesture.md) — A gesture that recognizes a rotation motion and tracks the angle of the rotation.
- [RotateGesture3D](../rotategesture3d.md) — A gesture that recognizes 3D rotation motion and tracks the angle and axis of the rotation.
- [GestureMask](../gesturemask.md) — Options that control how adding a gesture to a view affects other gestures recognized by the view and its subviews.
