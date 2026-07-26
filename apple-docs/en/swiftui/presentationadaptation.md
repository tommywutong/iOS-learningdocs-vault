---
title: PresentationAdaptation
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/presentationadaptation
source_url: 'https://developer.apple.com/documentation/swiftui/presentationadaptation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/presentationadaptation.json'
content_hash: 'sha256:320e103d672d4665'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PresentationAdaptation

<sub>Structure</sub>

Strategies for adapting a presentation to a different size class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PresentationAdaptation
```

## Overview

Use values of this type with the [presentationCompactAdaptation(_:)](<view/presentationcompactadaptation(__).md>) and [presentationCompactAdaptation(horizontal:vertical:)](<view/presentationcompactadaptation(horizontal_vertical_).md>) modifiers.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting adaptation strategies

- [automatic](presentationadaptation/automatic.md) — Use the default presentation adaptation.
- [none](presentationadaptation/none.md) — Don’t adapt for the size class, if possible.
- [fullScreenCover](presentationadaptation/fullscreencover.md) — Prefer a full-screen-cover appearance when adapting for size classes.
- [popover](presentationadaptation/popover.md) — Prefer a popover appearance when adapting for size classes.
- [sheet](presentationadaptation/sheet.md) — Prefer a sheet appearance when adapting for size classes.

## See Also

### Adapting a presentation size

- [presentationCompactAdaptation(horizontal:vertical:)](<view/presentationcompactadaptation(horizontal_vertical_).md>) — Specifies how to adapt a presentation to horizontally and vertically compact size classes.
- [presentationCompactAdaptation(_:)](<view/presentationcompactadaptation(__).md>) — Specifies how to adapt a presentation to compact size classes.
- [presentationSizing(_:)](<view/presentationsizing(__).md>) — Sets the sizing of the containing presentation.
- [PresentationSizing](presentationsizing.md) — A type that defines the size of the presentation content and how the presentation size adjusts to its content’s size changing.
- [PresentationSizingRoot](presentationsizingroot.md) — A proxy to a view provided to the presentation with a defined presentation size.
- [PresentationSizingContext](presentationsizingcontext.md) — Contextual information about a presentation.
