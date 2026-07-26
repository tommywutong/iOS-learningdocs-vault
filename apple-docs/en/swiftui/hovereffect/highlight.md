---
title: highlight
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/hovereffect/highlight
source_url: 'https://developer.apple.com/documentation/swiftui/hovereffect/highlight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/hovereffect/highlight.json'
content_hash: 'sha256:6d9ce208771fb0c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [HoverEffect](../hovereffect.md)

# highlight

<sub>Type Property</sub>

An effect  that morphs the pointer into a platter behind the view and shows a light source indicating position.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var highlight: HoverEffect { get }
```

## Discussion

On tvOS, it applies a projection effect accompanied with a specular highlight on the view when contained within a focused view. It also incorporates motion effects to produce a parallax effect by adjusting the projection matrix and specular offset.

## See Also

### Getting hover effects

- [automatic](automatic.md) — An effect  that attempts to determine the effect automatically. This is the default effect.
- [lift](lift.md) — An effect that slides the pointer under the view and disappears as the view scales up and gains a shadow.
