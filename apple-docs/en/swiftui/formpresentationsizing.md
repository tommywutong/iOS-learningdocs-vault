---
title: FormPresentationSizing
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/formpresentationsizing
source_url: 'https://developer.apple.com/documentation/swiftui/formpresentationsizing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/formpresentationsizing.json'
content_hash: 'sha256:123a859c01347f8d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# FormPresentationSizing

<sub>Structure</sub>

The size is appropriate for forms and slightly less wide than`.page`

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct FormPresentationSizing
```

## Overview

On iOS, `.form` sizing enforces a platform-defined floor for the vertical and horizontal dimensions. On macOS, no floor is enforced, however a maximum proposed height is derived from the presenter height. To achieve presentations outside of these bounds, see `PresentationSizing.fitted` or implement your own custom [PresentationSizing](presentationsizing.md).

> [!info] See Also
> [form](presentationsizing/form.md)

## Relationships

- **Conforms To**: [PresentationSizing](presentationsizing.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## See Also

### Supporting types

- [AutomaticPresentationSizing](automaticpresentationsizing.md) — The default presentation sizing, appropriate for the platform.
- [FittedPresentationSizing](fittedpresentationsizing.md) — The size of the presentation is dictated by the ideal size of the content.
- [PagePresentationSizing](pagepresentationsizing.md) — The size is roughly the size of a page of paper, appropriate for informational or compositional content.
