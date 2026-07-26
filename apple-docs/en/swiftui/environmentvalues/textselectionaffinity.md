---
title: textSelectionAffinity
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/textselectionaffinity
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/textselectionaffinity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/textselectionaffinity.json'
content_hash: 'sha256:cc0707350c97ff9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# textSelectionAffinity

<sub>Instance Property</sub>

A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var textSelectionAffinity: TextSelectionAffinity { get set }
```

## Discussion

You can configure the selection affinity on a given hierarchy by using the [textSelectionAffinity(_:)](<../view/textselectionaffinity(__).md>) modifier.

## See Also

### Selecting text

- [textSelection(_:)](<../view/textselection(__).md>) — Controls whether people can select text within this view.
- [TextSelectability](../textselectability.md) — A type that describes the ability to select text.
- [TextSelection](../textselection.md) — Represents a selection of text.
- [textSelectionAffinity(_:)](<../view/textselectionaffinity(__).md>) — Sets the direction of a selection or cursor relative to a text character.
- [TextSelectionAffinity](../textselectionaffinity.md) — A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).
- [AttributedTextSelection](../attributedtextselection.md) — Represents a selection of attributed text.
