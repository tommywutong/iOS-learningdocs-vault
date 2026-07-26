---
title: repeat
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/gradientoptions/repeat
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/gradientoptions/repeat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/gradientoptions/repeat.json'
content_hash: 'sha256:75bfc356d64db523'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [GradientOptions](../gradientoptions.md)

# repeat

<sub>Type Property</sub>

An option that repeats the gradient outside its nominal range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var `repeat`: GraphicsContext.GradientOptions { get }
```

## Discussion

Use this option to cause the gradient to repeat its pattern in areas that exceed the bounds of its start and end points. The repetitions use the same start and end value for each repetition.

Without this option or [mirror](mirror.md), the gradient stops at the end of its range. The [mirror](mirror.md) option takes precendence if you set both this one and that one.

## See Also

### Getting gradient options

- [linearColor](linearcolor.md) — An option that interpolates between colors in a linear color space.
- [mirror](mirror.md) — An option that repeats the gradient outside its nominal range, reflecting every other instance.
