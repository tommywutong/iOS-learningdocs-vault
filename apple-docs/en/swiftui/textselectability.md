---
title: TextSelectability
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/textselectability
source_url: 'https://developer.apple.com/documentation/swiftui/textselectability'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textselectability.json'
content_hash: 'sha256:330979a8e9051155'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TextSelectability

<sub>Protocol</sub>

A type that describes the ability to select text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
protocol TextSelectability
```

## Overview

To configure whether people can select text in your app, use the [textSelection(_:)](<view/textselection(__).md>) modifier, passing in a text selectability value like [enabled](textselectability/enabled.md) or [disabled](textselectability/disabled.md).

## Relationships

- **Conforming Types**: [DisabledTextSelectability](disabledtextselectability.md), [EnabledTextSelectability](enabledtextselectability.md)

## Topics

### Getting selectability options

- [enabled](textselectability/enabled.md) — A selectability value that enables text selection by a person using your app.
- [disabled](textselectability/disabled.md) — A selectability value that disables text selection by the person using your app.

### Specifying selectability

- [allowsSelection](textselectability/allowsselection.md) — A Boolean value that indicates whether the selectability type allows selection.

### Supporting types

- [EnabledTextSelectability](enabledtextselectability.md) — A selectability type that enables text selection by the person using your app.
- [DisabledTextSelectability](disabledtextselectability.md) — A selectability type that disables text selection by the person using your app.

## See Also

### Selecting text

- [textSelection(_:)](<view/textselection(__).md>) — Controls whether people can select text within this view.
- [TextSelection](textselection.md) — Represents a selection of text.
- [textSelectionAffinity(_:)](<view/textselectionaffinity(__).md>) — Sets the direction of a selection or cursor relative to a text character.
- [textSelectionAffinity](environmentvalues/textselectionaffinity.md) — A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).
- [TextSelectionAffinity](textselectionaffinity.md) — A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).
- [AttributedTextSelection](attributedtextselection.md) — Represents a selection of attributed text.
