---
title: Text.AlignmentStrategy
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/text/alignmentstrategy
source_url: 'https://developer.apple.com/documentation/swiftui/text/alignmentstrategy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/alignmentstrategy.json'
content_hash: 'sha256:11a80c9595465225'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Text](../text.md)

# Text.AlignmentStrategy

<sub>Structure</sub>

The way SwiftUI infers the appropriate text alignment if no value is explicitly provided.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AlignmentStrategy
```

## Overview

> [!note] Note
> [Text](../text.md) tightly wraps its content, so text alignment only affects how lines are positioned relative to each other. The text as a whole needs to be positioned at the view level using [Alignment](../alignment.md).

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Type Properties

- [default](alignmentstrategy/default.md) — The default strategy based on the context it is used in.
- [layoutBased](alignmentstrategy/layoutbased.md) — The alignment following the environment setting.
- [writingDirectionBased](alignmentstrategy/writingdirectionbased.md) — The alignment following the writing direction of the same paragraph.
