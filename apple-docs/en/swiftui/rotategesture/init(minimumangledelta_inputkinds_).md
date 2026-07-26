---
title: 'init(minimumAngleDelta:inputKinds:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/rotategesture/init(minimumangledelta:inputkinds:)'
source_url: 'https://developer.apple.com/documentation/swiftui/rotategesture/init(minimumangledelta:inputkinds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/rotategesture/init%28minimumangledelta%3Ainputkinds%3A%29.json'
content_hash: 'sha256:65a3dcee62f1cc62'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [RotateGesture](../rotategesture.md)

# init(minimumAngleDelta:inputKinds:)

<sub>Initializer</sub>

Creates a rotation gesture with a minimum delta for the gesture to start, and the input kinds the gesture recognizes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init(minimumAngleDelta: Angle = .degrees(1), inputKinds: GestureInputKinds = .all)
```

## Parameters

- `minimumAngleDelta` — The minimum delta required before the gesture starts. The default value is a one-degree angle.

- `inputKinds` — A set of input kinds that this gesture recognizes. If not specified, the gesture will recognize all applicable input kinds that a person can use to perform it.

## See Also

### Creating the gesture

- [init(minimumAngleDelta:)](<init(minimumangledelta_).md>) — Creates a rotation gesture with a minimum delta for the gesture to start.
- [minimumAngleDelta](minimumangledelta.md) — The minimum delta required before the gesture succeeds.
