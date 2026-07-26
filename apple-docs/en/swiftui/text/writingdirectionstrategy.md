---
title: Text.WritingDirectionStrategy
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/text/writingdirectionstrategy
source_url: 'https://developer.apple.com/documentation/swiftui/text/writingdirectionstrategy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/writingdirectionstrategy.json'
content_hash: 'sha256:75b8c2f09aefb860'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Text](../text.md)

# Text.WritingDirectionStrategy

<sub>Structure</sub>

The way SwiftUI infers the appropriate writing direction if no value is explicitly provided.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct WritingDirectionStrategy
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Type Properties

- [contentBased](writingdirectionstrategy/contentbased.md) — The writing direction following the language of the string that is laid out.
- [default](writingdirectionstrategy/default.md) — The default strategy is [contentBased](writingdirectionstrategy/contentbased.md).
- [layoutBased](writingdirectionstrategy/layoutbased.md) — The writing direction following the general UI layout direction.
