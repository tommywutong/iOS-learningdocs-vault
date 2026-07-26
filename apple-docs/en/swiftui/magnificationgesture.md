---
title: MagnificationGesture
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/magnificationgesture
source_url: 'https://developer.apple.com/documentation/swiftui/magnificationgesture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/magnificationgesture.json'
content_hash: 'sha256:351920d5a30236a3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# MagnificationGesture

<sub>Structure</sub>

A gesture that recognizes a magnification motion and tracks the amount of magnification.

> [!warning] Deprecated
> Use [MagnifyGesture](magnifygesture.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated struct MagnificationGesture
```

## Relationships

- **Conforms To**: [Gesture](gesture.md)

## Topics

### Creating the gesture

- [init(minimumScaleDelta:)](<magnificationgesture/init(minimumscaledelta_).md>) — Creates a magnification gesture with a given minimum delta for the gesture to start. _(deprecated)_
- [minimumScaleDelta](magnificationgesture/minimumscaledelta.md) — The minimum required delta before the gesture starts. _(deprecated)_

## See Also

### Deprecated gestures

- [RotationGesture](rotationgesture.md) — A gesture that recognizes a rotation motion and tracks the angle of the rotation. _(deprecated)_
