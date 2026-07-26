---
title: 'init(minimumAngleDelta:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/rotategesture/init(minimumangledelta:)'
source_url: 'https://developer.apple.com/documentation/swiftui/rotategesture/init(minimumangledelta:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/rotategesture/init%28minimumangledelta%3A%29.json'
content_hash: 'sha256:cf83eedde5b363eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [RotateGesture](../rotategesture.md)

# init(minimumAngleDelta:)

<sub>Initializer</sub>

Creates a rotation gesture with a minimum delta for the gesture to start.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init(minimumAngleDelta: Angle = .degrees(1))
```

## Parameters

- `minimumAngleDelta` — The minimum delta required before the gesture starts. The default value is a one-degree angle.

## See Also

### Creating the gesture

- [init(minimumAngleDelta:inputKinds:)](<init(minimumangledelta_inputkinds_).md>) — Creates a rotation gesture with a minimum delta for the gesture to start, and the input kinds the gesture recognizes. _(beta)_
- [minimumAngleDelta](minimumangledelta.md) — The minimum delta required before the gesture succeeds.
