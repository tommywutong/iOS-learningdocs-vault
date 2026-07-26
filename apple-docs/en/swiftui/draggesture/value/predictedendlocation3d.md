---
title: predictedEndLocation3D
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/draggesture/value/predictedendlocation3d
source_url: 'https://developer.apple.com/documentation/swiftui/draggesture/value/predictedendlocation3d'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/draggesture/value/predictedendlocation3d.json'
content_hash: 'sha256:aca90b08363a8fc4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [DragGesture](../../draggesture.md) · [Value](../value.md)

# predictedEndLocation3D

<sub>Instance Property</sub>

A prediction of where the final location would be if dragging stopped now, based on the current drag velocity.

<sub>visionOS</sub>

```swift
var predictedEndLocation3D: Point3D { get }
```

## See Also

### Getting 3D position

- [startLocation3D](startlocation3d.md) — The 3D start location of the drag gesture.
- [location3D](location3d.md) — The 3D location of the drag gesture.
- [translation3D](translation3d.md) — The translation of the drag gesture from `startLocation3D` to `location3D`.
- [predictedEndTranslation3D](predictedendtranslation3d.md) — A prediction of what the final translation would be if dragging stopped now, based on the current drag velocity.
- [startInputDevicePose3D](startinputdevicepose3d.md) — The starting 3D pose of the device driving the drag, if one exists.
- [inputDevicePose3D](inputdevicepose3d.md) — The 3D pose of the device driving the drag, if one exists.
