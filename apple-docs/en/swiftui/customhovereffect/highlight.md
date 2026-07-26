---
title: highlight
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/customhovereffect/highlight
source_url: 'https://developer.apple.com/documentation/swiftui/customhovereffect/highlight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/customhovereffect/highlight.json'
content_hash: 'sha256:874bc41d7d018b43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CustomHoverEffect](../customhovereffect.md)

# highlight

<sub>Type Property</sub>

A hover effect that highlights views using a light source to indicate position.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var highlight: HighlightHoverEffect { get }
```

## Discussion

For pointer input this effect morphs the pointer into a platter behind the view and shows a light source indicating position.

On tvOS it applies a projection effect accompanied with a specular highlight on the view when contained within a focused view. It also incorporates motion effects to produce a parallax effect by adjusting the projection matrix and specular offset.

On visionOS this effect applies a glow effect based on where the user is looking or touching the view.

## See Also

### Getting built-in hover effects

- [automatic](automatic.md) — The default hover effect based on the surrounding context.
- [empty](empty.md) — An effect that applies no changes when hovered.
- [lift](lift.md) — A hover effect that slides the pointer under the view and disappears as the view scales up and gains a shadow.
