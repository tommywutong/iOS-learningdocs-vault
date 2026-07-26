---
title: SimultaneousGesture
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/simultaneousgesture
source_url: 'https://developer.apple.com/documentation/swiftui/simultaneousgesture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/simultaneousgesture.json'
content_hash: 'sha256:07d3ae7c73b9891d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SimultaneousGesture

<sub>Structure</sub>

A gesture containing two gestures that can happen at the same time with neither of them preceding the other.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen nonisolated struct SimultaneousGesture<First, Second> where First : Gesture, Second : Gesture
```

## Overview

A simultaneous gesture is a container-event handler that evaluates its two child gestures at the same time. Its value is a struct with two optional values, each representing the phases of one of the two gestures.

## Relationships

- **Conforms To**: [Gesture](gesture.md)

## Topics

### Creating the gesture

- [init(_:_:)](<simultaneousgesture/init(____).md>) — Creates a gesture with two gestures that can receive updates or succeed independently of each other.
- [first](simultaneousgesture/first.md) — The first of two gestures that can happen simultaneously.
- [second](simultaneousgesture/second.md) — The second of two gestures that can happen simultaneously.

### Getting the gesture’s values

- [Value](simultaneousgesture/value.md) — The value of a simultaneous gesture that indicates which of its two gestures receives events.

## See Also

### Combining gestures

- [Composing SwiftUI gestures](composing-swiftui-gestures.md) — Combine gestures to create complex interactions.
- [simultaneousGesture(_:including:)](<view/simultaneousgesture(__including_).md>) — Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [simultaneousGesture(_:isEnabled:)](<view/simultaneousgesture(__isenabled_).md>) — Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [simultaneousGesture(_:name:isEnabled:)](<view/simultaneousgesture(__name_isenabled_).md>) — Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [SequenceGesture](sequencegesture.md) — A gesture that’s a sequence of two gestures.
- [ExclusiveGesture](exclusivegesture.md) — A gesture that consists of two gestures where only one of them can succeed.
