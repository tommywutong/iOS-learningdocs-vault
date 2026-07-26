---
title: PresentationContentInteraction
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/presentationcontentinteraction
source_url: 'https://developer.apple.com/documentation/swiftui/presentationcontentinteraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/presentationcontentinteraction.json'
content_hash: 'sha256:1474237e0d9c8989'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PresentationContentInteraction

<sub>Structure</sub>

A behavior that you can use to influence how a presentation responds to swipe gestures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PresentationContentInteraction
```

## Overview

Use values of this type with the [presentationContentInteraction(_:)](<view/presentationcontentinteraction(__).md>) modifier.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting interaction behaviors

- [automatic](presentationcontentinteraction/automatic.md) — The default swipe behavior for the presentation.
- [resizes](presentationcontentinteraction/resizes.md) — A behavior that prioritizes resizing a presentation when swiping, rather than scrolling the content of the presentation.
- [scrolls](presentationcontentinteraction/scrolls.md) — A behavior that prioritizes scrolling the content of a presentation when swiping, rather than resizing the presentation.

## See Also

### Configuring a sheet’s height

- [presentationDetents(_:)](<view/presentationdetents(__).md>) — Sets the available detents for the enclosing sheet.
- [presentationDetents(_:selection:)](<view/presentationdetents(__selection_).md>) — Sets the available detents for the enclosing sheet, giving you programmatic control of the currently selected detent.
- [presentationContentInteraction(_:)](<view/presentationcontentinteraction(__).md>) — Configures the behavior of swipe gestures on a presentation.
- [presentationDragIndicator(_:)](<view/presentationdragindicator(__).md>) — Sets the visibility of the drag indicator on top of a sheet.
- [PresentationDetent](presentationdetent.md) — A type that represents a height where a sheet naturally rests.
- [CustomPresentationDetent](custompresentationdetent.md) — The definition of a custom detent with a calculated height.
