---
title: AccessibilityTechnologies
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/accessibilitytechnologies
source_url: 'https://developer.apple.com/documentation/swiftui/accessibilitytechnologies'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessibilitytechnologies.json'
content_hash: 'sha256:11da3a6682d5cf4a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AccessibilityTechnologies

<sub>Structure</sub>

Accessibility technologies available to the system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AccessibilityTechnologies
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Getting technology types

- [switchControl](accessibilitytechnologies/switchcontrol.md) — The value that represents a Switch Control, allowing the use of the entire system using controller buttons, a breath-controlled switch or similar hardware.
- [voiceOver](accessibilitytechnologies/voiceover.md) — The value that represents the VoiceOver screen reader, allowing use of the system without seeing the screen visually.

### Creating a technology type

- [init()](<accessibilitytechnologies/init().md>) — Creates a new accessibility technologies structure with an empy accessibility technology set.

## See Also

### Supporting types

- [AccessibilityAttachmentModifier](accessibilityattachmentmodifier.md) — A view modifier that adds accessibility properties to the view
