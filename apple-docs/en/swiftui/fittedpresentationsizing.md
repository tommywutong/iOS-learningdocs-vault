---
title: FittedPresentationSizing
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/fittedpresentationsizing
source_url: 'https://developer.apple.com/documentation/swiftui/fittedpresentationsizing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/fittedpresentationsizing.json'
content_hash: 'sha256:0c3a8488d037590d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# FittedPresentationSizing

<sub>Structure</sub>

The size of the presentation is dictated by the ideal size of the content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct FittedPresentationSizing
```

## Overview

The presentation is sized by proposing `nil` in the horizontal and vertical dimensions.

> [!info] See Also
> [fitted](presentationsizing/fitted.md)

## Relationships

- **Conforms To**: [PresentationSizing](presentationsizing.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## See Also

### Supporting types

- [AutomaticPresentationSizing](automaticpresentationsizing.md) — The default presentation sizing, appropriate for the platform.
- [FormPresentationSizing](formpresentationsizing.md) — The size is appropriate for forms and slightly less wide than`.page`
- [PagePresentationSizing](pagepresentationsizing.md) — The size is roughly the size of a page of paper, appropriate for informational or compositional content.
