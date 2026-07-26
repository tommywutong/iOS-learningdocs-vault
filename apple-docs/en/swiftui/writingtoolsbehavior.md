---
title: WritingToolsBehavior
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/writingtoolsbehavior
source_url: 'https://developer.apple.com/documentation/swiftui/writingtoolsbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/writingtoolsbehavior.json'
content_hash: 'sha256:bab1eacac0857fd1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# WritingToolsBehavior

<sub>Structure</sub>

The Writing Tools editing experience for text and text input.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct WritingToolsBehavior
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [automatic](writingtoolsbehavior/automatic.md) — An appropriate editing experience will be provided based on context, which may include disabling the writing tools.
- [complete](writingtoolsbehavior/complete.md) — The complete inline-editing experience is provided if possible.
- [disabled](writingtoolsbehavior/disabled.md) — The writing tools are disabled.
- [limited](writingtoolsbehavior/limited.md) — The limited, overlay-panel experience is provided if possible.

## See Also

### Configuring the Writing Tools behavior

- [writingToolsBehavior(_:)](<view/writingtoolsbehavior(__).md>) — Specifies the Writing Tools behavior for text and text input in the environment.
- [writingToolsAffordanceVisibility(_:)](<view/writingtoolsaffordancevisibility(__).md>) — Specifies whether the system should show the Writing Tools affordance for text input views affected by the environment.
