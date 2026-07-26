---
title: symbolEffect
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/contenttransition/symboleffect
source_url: 'https://developer.apple.com/documentation/swiftui/contenttransition/symboleffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/contenttransition/symboleffect.json'
content_hash: 'sha256:222e29b2b7dca37e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ContentTransition](../contenttransition.md)

# symbolEffect

<sub>Type Property</sub>

A content transition that applies the default symbol effect transition to symbol images within the inserted or removed view hierarchy. Other views are unaffected by this transition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static var symbolEffect: ContentTransition { get }
```

## See Also

### Getting content transitions

- [identity](identity.md) — The identity content transition, which indicates that content changes shouldn’t animate.
- [interpolate](interpolate.md) — A content transition that indicates the views attempt to interpolate their contents during transitions, where appropriate.
- [numericText(countsDown:)](<numerictext(countsdown_).md>) — Creates a content transition intended to be used with `Text` views displaying numeric text. In certain environments changes to the text will enable a nonstandard transition tailored to numeric characters that count up or down.
- [numericText(value:)](<numerictext(value_).md>) — Creates a content transition intended to be used with `Text` views displaying numbers.
- [opacity](opacity.md) — A content transition that indicates content fades from transparent to opaque on insertion, and from opaque to transparent on removal.
- [symbolEffect(_:options:)](<symboleffect(__options_).md>) — Creates a content transition that applies the symbol Replace animation to symbol images that it is applied to.
