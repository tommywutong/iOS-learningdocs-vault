---
title: PresentationBackgroundInteraction
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/presentationbackgroundinteraction
source_url: 'https://developer.apple.com/documentation/swiftui/presentationbackgroundinteraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/presentationbackgroundinteraction.json'
content_hash: 'sha256:f09b1ed76fc0c3bf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PresentationBackgroundInteraction

<sub>Structure</sub>

The kinds of interaction available to views behind a presentation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PresentationBackgroundInteraction
```

## Overview

Use values of this type with the [presentationBackgroundInteraction(_:)](<view/presentationbackgroundinteraction(__).md>) modifier.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting interaction types

- [automatic](presentationbackgroundinteraction/automatic.md) — The default background interaction for the presentation.
- [disabled](presentationbackgroundinteraction/disabled.md) — People can’t interact with the view behind a presentation.
- [enabled](presentationbackgroundinteraction/enabled.md) — People can interact with the view behind a presentation.
- [enabled(upThrough:)](<presentationbackgroundinteraction/enabled(upthrough_).md>) — People can interact with the view behind a presentation up through a specified detent.

## See Also

### Styling a sheet and its background

- [presentationCornerRadius(_:)](<view/presentationcornerradius(__).md>) — Requests that the presentation have a specific corner radius.
- [presentationBackground(_:)](<view/presentationbackground(__).md>) — Sets the presentation background of the enclosing sheet using a shape style.
- [presentationBackground(alignment:content:)](<view/presentationbackground(alignment_content_).md>) — Sets the presentation background of the enclosing sheet to a custom view.
- [presentationBackgroundInteraction(_:)](<view/presentationbackgroundinteraction(__).md>) — Controls whether people can interact with the view behind a presentation.
