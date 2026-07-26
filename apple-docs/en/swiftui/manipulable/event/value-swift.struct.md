---
title: Manipulable.Event.Value
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/manipulable/event/value-swift.struct
source_url: 'https://developer.apple.com/documentation/swiftui/manipulable/event/value-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/manipulable/event/value-swift.struct.json'
content_hash: 'sha256:da22d914dac3f43e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [Manipulable](../../manipulable.md) · [Event](../event.md)

# Manipulable.Event.Value

<sub>Structure</sub>

Describes the value associated with a manipulation gesture event.

<sub>visionOS</sub>

```swift
struct Value
```

## Relationships

- **Conforms To**: [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [frame](value-swift.struct/frame.md) — The 3D bounding box of the manipulated view.
- [inputDevices](value-swift.struct/inputdevices.md) — The input devices that a person is using to manipulate a view.
- [interactionPoint](value-swift.struct/interactionpoint.md) — The point at which a person interacted with a view to begin manipulating it.
- [timestamp](value-swift.struct/timestamp.md) — The time the event was processed.
- [transform](value-swift.struct/transform.md) — The 3D affine transform of the manipulated view, or `nil` if the view doesn’t have a well-defined 3D affine transfrorm.
