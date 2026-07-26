---
title: 'numericText(value:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/contenttransition/numerictext(value:)'
source_url: 'https://developer.apple.com/documentation/swiftui/contenttransition/numerictext(value:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/contenttransition/numerictext%28value%3A%29.json'
content_hash: 'sha256:7a4b0503321619ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ContentTransition](../contenttransition.md)

# numericText(value:)

<sub>Type Method</sub>

Creates a content transition intended to be used with `Text` views displaying numbers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func numericText(value: Double) -> ContentTransition
```

## Parameters

- `value` — The value represented by the `Text` view being animated. The difference between the old and new values when the text changes will be used to determine the animation direction.

## Return Value

A new content transition.

## Discussion

The example below creates a text view displaying a particular value, assigning the same value to the associated transition:

```swift
Text("\(value)")
    .contentTransition(.numericText(value: value))
```

## See Also

### Getting content transitions

- [identity](identity.md) — The identity content transition, which indicates that content changes shouldn’t animate.
- [interpolate](interpolate.md) — A content transition that indicates the views attempt to interpolate their contents during transitions, where appropriate.
- [numericText(countsDown:)](<numerictext(countsdown_).md>) — Creates a content transition intended to be used with `Text` views displaying numeric text. In certain environments changes to the text will enable a nonstandard transition tailored to numeric characters that count up or down.
- [opacity](opacity.md) — A content transition that indicates content fades from transparent to opaque on insertion, and from opaque to transparent on removal.
- [symbolEffect](symboleffect.md) — A content transition that applies the default symbol effect transition to symbol images within the inserted or removed view hierarchy. Other views are unaffected by this transition.
- [symbolEffect(_:options:)](<symboleffect(__options_).md>) — Creates a content transition that applies the symbol Replace animation to symbol images that it is applied to.
