---
title: identity
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/contenttransition/identity
source_url: 'https://developer.apple.com/documentation/swiftui/contenttransition/identity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/contenttransition/identity.json'
content_hash: 'sha256:1239b24cc50a6904'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ContentTransition](../contenttransition.md)

# identity

<sub>Type Property</sub>

The identity content transition, which indicates that content changes shouldn’t animate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let identity: ContentTransition
```

## Discussion

You can pass this value to a [contentTransition(_:)](<../view/contenttransition(__).md>) modifier to selectively disable animations that would otherwise be applied by a [withAnimation(_:_:)](<../withanimation(____).md>) block.

## See Also

### Getting content transitions

- [interpolate](interpolate.md) — A content transition that indicates the views attempt to interpolate their contents during transitions, where appropriate.
- [numericText(countsDown:)](<numerictext(countsdown_).md>) — Creates a content transition intended to be used with `Text` views displaying numeric text. In certain environments changes to the text will enable a nonstandard transition tailored to numeric characters that count up or down.
- [numericText(value:)](<numerictext(value_).md>) — Creates a content transition intended to be used with `Text` views displaying numbers.
- [opacity](opacity.md) — A content transition that indicates content fades from transparent to opaque on insertion, and from opaque to transparent on removal.
- [symbolEffect](symboleffect.md) — A content transition that applies the default symbol effect transition to symbol images within the inserted or removed view hierarchy. Other views are unaffected by this transition.
- [symbolEffect(_:options:)](<symboleffect(__options_).md>) — Creates a content transition that applies the symbol Replace animation to symbol images that it is applied to.
