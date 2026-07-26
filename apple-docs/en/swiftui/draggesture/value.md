---
title: DragGesture.Value
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/draggesture/value
source_url: 'https://developer.apple.com/documentation/swiftui/draggesture/value'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/draggesture/value.json'
content_hash: 'sha256:6f94e19a6a730124'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DragGesture](../draggesture.md)

# DragGesture.Value

<sub>Structure</sub>

The attributes of a drag gesture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
struct Value
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting 2D position

- [startLocation](value/startlocation.md) — The location of the drag gesture’s first event.
- [location](value/location.md) — The location of the drag gesture’s current event.
- [predictedEndLocation](value/predictedendlocation.md) — A prediction, based on the current drag velocity, of where the final location will be if dragging stopped now.
- [translation](value/translation.md) — The total translation from the start of the drag gesture to the current event of the drag gesture.
- [predictedEndTranslation](value/predictedendtranslation.md) — A prediction, based on the current drag velocity, of what the final translation will be if dragging stopped now.

### Getting 3D position

- [startLocation3D](value/startlocation3d.md) — The 3D start location of the drag gesture.
- [location3D](value/location3d.md) — The 3D location of the drag gesture.
- [predictedEndLocation3D](value/predictedendlocation3d.md) — A prediction of where the final location would be if dragging stopped now, based on the current drag velocity.
- [translation3D](value/translation3d.md) — The translation of the drag gesture from `startLocation3D` to `location3D`.
- [predictedEndTranslation3D](value/predictedendtranslation3d.md) — A prediction of what the final translation would be if dragging stopped now, based on the current drag velocity.
- [startInputDevicePose3D](value/startinputdevicepose3d.md) — The starting 3D pose of the device driving the drag, if one exists.
- [inputDevicePose3D](value/inputdevicepose3d.md) — The 3D pose of the device driving the drag, if one exists.

### Handling changes over time

- [time](value/time.md) — The time associated with the drag gesture’s current event.
- [velocity](value/velocity.md) — The current drag velocity.
