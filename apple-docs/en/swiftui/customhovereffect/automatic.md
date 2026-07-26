---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/customhovereffect/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/customhovereffect/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/customhovereffect/automatic.json'
content_hash: 'sha256:eec1cbfbc320982d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CustomHoverEffect](../customhovereffect.md)

# automatic

<sub>Type Property</sub>

The default hover effect based on the surrounding context.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated static var automatic: AutomaticHoverEffect { get }
```

## Discussion

The automatic effect will resolve to any [defaultHoverEffect(_:)](<../view/defaulthovereffect(__).md>) applied to the current View hierarchy, or a system-defined effect if no default effect has been defined.

## See Also

### Getting built-in hover effects

- [empty](empty.md) — An effect that applies no changes when hovered.
- [highlight](highlight.md) — A hover effect that highlights views using a light source to indicate position.
- [lift](lift.md) — A hover effect that slides the pointer under the view and disappears as the view scales up and gains a shadow.
