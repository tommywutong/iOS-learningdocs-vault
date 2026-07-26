---
title: PresentationDetent
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/presentationdetent
source_url: 'https://developer.apple.com/documentation/swiftui/presentationdetent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/presentationdetent.json'
content_hash: 'sha256:a4a8a85a8474c996'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PresentationDetent

<sub>Structure</sub>

A type that represents a height where a sheet naturally rests.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PresentationDetent
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting built-in detents

- [large](presentationdetent/large.md) — The system detent for a sheet at full height.
- [medium](presentationdetent/medium.md) — The system detent for a sheet that’s approximately half the height of the screen, and is inactive in compact height.

### Creating custom detents

- [custom(_:)](<presentationdetent/custom(__).md>) — A custom detent with a calculated height.
- [fraction(_:)](<presentationdetent/fraction(__).md>) — A custom detent with the specified fractional height.
- [height(_:)](<presentationdetent/height(__).md>) — A custom detent with the specified height.
- [Context](presentationdetent/context.md) — Information that you use to calculate the presentation’s height.

## See Also

### Configuring a sheet’s height

- [presentationDetents(_:)](<view/presentationdetents(__).md>) — Sets the available detents for the enclosing sheet.
- [presentationDetents(_:selection:)](<view/presentationdetents(__selection_).md>) — Sets the available detents for the enclosing sheet, giving you programmatic control of the currently selected detent.
- [presentationContentInteraction(_:)](<view/presentationcontentinteraction(__).md>) — Configures the behavior of swipe gestures on a presentation.
- [presentationDragIndicator(_:)](<view/presentationdragindicator(__).md>) — Sets the visibility of the drag indicator on top of a sheet.
- [CustomPresentationDetent](custompresentationdetent.md) — The definition of a custom detent with a calculated height.
- [PresentationContentInteraction](presentationcontentinteraction.md) — A behavior that you can use to influence how a presentation responds to swipe gestures.
