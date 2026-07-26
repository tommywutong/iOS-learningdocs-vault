---
title: WorldRecenterPhase
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/worldrecenterphase
source_url: 'https://developer.apple.com/documentation/swiftui/worldrecenterphase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/worldrecenterphase.json'
content_hash: 'sha256:37024540be08a1c1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# WorldRecenterPhase

<sub>Enumeration</sub>

A type that represents information associated with a phase of a system recenter event. Values of this type are passed to the closure specified in View.onWorldRecenter(action:).

<sub>macOS, visionOS</sub>

```swift
enum WorldRecenterPhase
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [WorldRecenterPhase.began](worldrecenterphase/began.md) — The app has begun to fade out. It is not re-positioned yet.
- [WorldRecenterPhase.ended](worldrecenterphase/ended.md) — The app has begun to fade in after it has been re-positioned.
