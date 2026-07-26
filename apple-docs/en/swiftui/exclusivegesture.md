---
title: ExclusiveGesture
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/exclusivegesture
source_url: 'https://developer.apple.com/documentation/swiftui/exclusivegesture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/exclusivegesture.json'
content_hash: 'sha256:fd4d1c6e95792951'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ExclusiveGesture

<sub>Structure</sub>

A gesture that consists of two gestures where only one of them can succeed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen nonisolated struct ExclusiveGesture<First, Second> where First : Gesture, Second : Gesture
```

## Overview

The `ExclusiveGesture` gives precedence to its first gesture.

## Relationships

- **Conforms To**: [Gesture](gesture.md)

## Topics

### Creating the gesture

- [init(_:_:)](<exclusivegesture/init(____).md>) — Creates a gesture from two gestures where only one of them succeeds.
- [first](exclusivegesture/first.md) — The first of two gestures.
- [second](exclusivegesture/second.md) — The second of two gestures.

### Supporting types

- [Value](exclusivegesture/value.md) — The value of an exclusive gesture that indicates which of two gestures succeeded.

## See Also

### Combining gestures

- [Composing SwiftUI gestures](composing-swiftui-gestures.md) — Combine gestures to create complex interactions.
- [simultaneousGesture(_:including:)](<view/simultaneousgesture(__including_).md>) — Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [simultaneousGesture(_:isEnabled:)](<view/simultaneousgesture(__isenabled_).md>) — Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [simultaneousGesture(_:name:isEnabled:)](<view/simultaneousgesture(__name_isenabled_).md>) — Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [SequenceGesture](sequencegesture.md) — A gesture that’s a sequence of two gestures.
- [SimultaneousGesture](simultaneousgesture.md) — A gesture containing two gestures that can happen at the same time with neither of them preceding the other.
