---
title: SequenceGesture
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sequencegesture
source_url: 'https://developer.apple.com/documentation/swiftui/sequencegesture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sequencegesture.json'
content_hash: 'sha256:fc305ed90c1864ee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SequenceGesture

<sub>Structure</sub>

A gesture that’s a sequence of two gestures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen nonisolated struct SequenceGesture<First, Second> where First : Gesture, Second : Gesture
```

## Overview

Read [Composing SwiftUI gestures](composing-swiftui-gestures.md) to learn how you can create a sequence of two gestures.

## Relationships

- **Conforms To**: [Gesture](gesture.md)

## Topics

### Creating the gesture

- [init(_:_:)](<sequencegesture/init(____).md>) — Creates a sequence gesture with two gestures.
- [first](sequencegesture/first.md) — The first gesture in a sequence of two gestures.
- [second](sequencegesture/second.md) — The second gesture in a sequence of two gestures.

### Getting the gesture’s values

- [Value](sequencegesture/value.md) — The value of a sequence gesture that helps to detect whether the first gesture succeeded, so the second gesture can start.

## See Also

### Combining gestures

- [Composing SwiftUI gestures](composing-swiftui-gestures.md) — Combine gestures to create complex interactions.
- [simultaneousGesture(_:including:)](<view/simultaneousgesture(__including_).md>) — Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [simultaneousGesture(_:isEnabled:)](<view/simultaneousgesture(__isenabled_).md>) — Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [simultaneousGesture(_:name:isEnabled:)](<view/simultaneousgesture(__name_isenabled_).md>) — Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [SimultaneousGesture](simultaneousgesture.md) — A gesture containing two gestures that can happen at the same time with neither of them preceding the other.
- [ExclusiveGesture](exclusivegesture.md) — A gesture that consists of two gestures where only one of them can succeed.
