---
title: GestureMask
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/gesturemask
source_url: 'https://developer.apple.com/documentation/swiftui/gesturemask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gesturemask.json'
content_hash: 'sha256:ee170cdb1f78c2ce'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# GestureMask

<sub>Structure</sub>

Options that control how adding a gesture to a view affects other gestures recognized by the view and its subviews.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct GestureMask
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Getting gesture options

- [all](gesturemask/all.md) — Enable both the added gesture as well as all other gestures on the view and its subviews.
- [gesture](gesturemask/gesture.md) — Enable the added gesture but disable all gestures in the subview hierarchy.
- [subviews](gesturemask/subviews.md) — Enable all gestures in the subview hierarchy but disable the added gesture.
- [none](gesturemask/none.md) — Disable all gestures in the subview hierarchy, including the added gesture.

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
- [RotateGesture3D](rotategesture3d.md) — A gesture that recognizes 3D rotation motion and tracks the angle and axis of the rotation.
