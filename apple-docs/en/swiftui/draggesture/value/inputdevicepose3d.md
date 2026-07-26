---
title: inputDevicePose3D
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/draggesture/value/inputdevicepose3d
source_url: 'https://developer.apple.com/documentation/swiftui/draggesture/value/inputdevicepose3d'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/draggesture/value/inputdevicepose3d.json'
content_hash: 'sha256:07bf8d853016af39'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [DragGesture](../../draggesture.md) · [Value](../value.md)

# inputDevicePose3D

<sub>Instance Property</sub>

The 3D pose of the device driving the drag, if one exists.

<sub>visionOS</sub>

```swift
var inputDevicePose3D: Pose3D? { get }
```

## See Also

### Getting 3D position

- [startLocation3D](startlocation3d.md) — The 3D start location of the drag gesture.
- [location3D](location3d.md) — The 3D location of the drag gesture.
- [predictedEndLocation3D](predictedendlocation3d.md) — A prediction of where the final location would be if dragging stopped now, based on the current drag velocity.
- [translation3D](translation3d.md) — The translation of the drag gesture from `startLocation3D` to `location3D`.
- [predictedEndTranslation3D](predictedendtranslation3d.md) — A prediction of what the final translation would be if dragging stopped now, based on the current drag velocity.
- [startInputDevicePose3D](startinputdevicepose3d.md) — The starting 3D pose of the device driving the drag, if one exists.
