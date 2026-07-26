---
title: RotationGesture
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/rotationgesture
source_url: 'https://developer.apple.com/documentation/swiftui/rotationgesture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/rotationgesture.json'
content_hash: 'sha256:bee8ec198514f333'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# RotationGesture

<sub>Structure</sub>

A gesture that recognizes a rotation motion and tracks the angle of the rotation.

> [!warning] Deprecated
> Use [RotateGesture](rotategesture.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated struct RotationGesture
```

## Relationships

- **Conforms To**: [Gesture](gesture.md)

## Topics

### Creating the gesture

- [init(minimumAngleDelta:)](<rotationgesture/init(minimumangledelta_).md>) — Creates a rotation gesture with a minimum delta for the gesture to start. _(deprecated)_
- [minimumAngleDelta](rotationgesture/minimumangledelta.md) — The minimum delta required before the gesture succeeds. _(deprecated)_

## See Also

### Deprecated gestures

- [MagnificationGesture](magnificationgesture.md) — A gesture that recognizes a magnification motion and tracks the amount of magnification. _(deprecated)_
