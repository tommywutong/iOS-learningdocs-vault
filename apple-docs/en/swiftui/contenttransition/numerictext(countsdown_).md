---
title: 'numericText(countsDown:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/contenttransition/numerictext(countsdown:)'
source_url: 'https://developer.apple.com/documentation/swiftui/contenttransition/numerictext(countsdown:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/contenttransition/numerictext%28countsdown%3A%29.json'
content_hash: 'sha256:3a7de7945457470d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ContentTransition](../contenttransition.md)

# numericText(countsDown:)

<sub>Type Method</sub>

Creates a content transition intended to be used with `Text` views displaying numeric text. In certain environments changes to the text will enable a nonstandard transition tailored to numeric characters that count up or down.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func numericText(countsDown: Bool = false) -> ContentTransition
```

## Parameters

- `countsDown` — True if the numbers represented by the text are counting downwards.

## Return Value

A new content transition.

## See Also

### Getting content transitions

- [identity](identity.md) — The identity content transition, which indicates that content changes shouldn’t animate.
- [interpolate](interpolate.md) — A content transition that indicates the views attempt to interpolate their contents during transitions, where appropriate.
- [numericText(value:)](<numerictext(value_).md>) — Creates a content transition intended to be used with `Text` views displaying numbers.
- [opacity](opacity.md) — A content transition that indicates content fades from transparent to opaque on insertion, and from opaque to transparent on removal.
- [symbolEffect](symboleffect.md) — A content transition that applies the default symbol effect transition to symbol images within the inserted or removed view hierarchy. Other views are unaffected by this transition.
- [symbolEffect(_:options:)](<symboleffect(__options_).md>) — Creates a content transition that applies the symbol Replace animation to symbol images that it is applied to.
