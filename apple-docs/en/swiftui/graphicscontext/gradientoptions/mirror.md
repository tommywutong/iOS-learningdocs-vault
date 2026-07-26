---
title: mirror
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/gradientoptions/mirror
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/gradientoptions/mirror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/gradientoptions/mirror.json'
content_hash: 'sha256:2ed8127f602b9456'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [GradientOptions](../gradientoptions.md)

# mirror

<sub>Type Property</sub>

An option that repeats the gradient outside its nominal range, reflecting every other instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var mirror: GraphicsContext.GradientOptions { get }
```

## Discussion

Use this option to cause the gradient to repeat its pattern in areas that exceed the bounds of its start and end points. The repetitions alternately reverse the start and end points, producing a pattern like `0 -> 1`, `1 -> 0`, `0 -> 1`, and so on.

Without either this option or [repeat](repeat.md), the gradient stops at the end of its range. This option takes precendence if you set both this one and [repeat](repeat.md).

## See Also

### Getting gradient options

- [linearColor](linearcolor.md) — An option that interpolates between colors in a linear color space.
- [repeat](repeat.md) — An option that repeats the gradient outside its nominal range.
