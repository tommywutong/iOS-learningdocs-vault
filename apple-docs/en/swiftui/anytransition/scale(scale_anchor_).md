---
title: 'scale(scale:anchor:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/anytransition/scale(scale:anchor:)'
source_url: 'https://developer.apple.com/documentation/swiftui/anytransition/scale(scale:anchor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/anytransition/scale%28scale%3Aanchor%3A%29.json'
content_hash: 'sha256:4b99d9a8c04910aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AnyTransition](../anytransition.md)

# scale(scale:anchor:)

<sub>Type Method</sub>

Returns a transition that scales the view by the specified amount.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func scale(scale: CGFloat, anchor: UnitPoint = .center) -> AnyTransition
```

## See Also

### Getting built-in transitions

- [identity](identity.md) — A transition that returns the input view, unmodified, as the output view.
- [move(edge:)](<move(edge_).md>) — Returns a transition that moves the view away, towards the specified edge of the view.
- [offset(_:)](<offset(__).md>)
- [offset(x:y:)](<offset(x_y_).md>)
- [opacity](opacity.md) — A transition from transparent to opaque on insertion, and from opaque to transparent on removal.
- [push(from:)](<push(from_).md>) — Creates a transition that when added to a view will animate the view’s insertion by moving it in from the specified edge while fading it in, and animate its removal by moving it out towards the opposite edge and fading it out.
- [scale](scale.md) — Returns a transition that scales the view.
- [slide](slide.md) — A transition that inserts by moving in from the leading edge, and removes by moving out towards the trailing edge.
