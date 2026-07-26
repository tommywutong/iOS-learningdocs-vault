---
title: 'push(from:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/anytransition/push(from:)'
source_url: 'https://developer.apple.com/documentation/swiftui/anytransition/push(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/anytransition/push%28from%3A%29.json'
content_hash: 'sha256:b5ca92c468b7206a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AnyTransition](../anytransition.md)

# push(from:)

<sub>Type Method</sub>

Creates a transition that when added to a view will animate the view’s insertion by moving it in from the specified edge while fading it in, and animate its removal by moving it out towards the opposite edge and fading it out.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func push(from edge: Edge) -> AnyTransition
```

## Parameters

- `edge` — The edge from which the view will be animated in.

## Return Value

A transition that animates a view by moving and fading it.

## See Also

### Getting built-in transitions

- [identity](identity.md) — A transition that returns the input view, unmodified, as the output view.
- [move(edge:)](<move(edge_).md>) — Returns a transition that moves the view away, towards the specified edge of the view.
- [offset(_:)](<offset(__).md>)
- [offset(x:y:)](<offset(x_y_).md>)
- [opacity](opacity.md) — A transition from transparent to opaque on insertion, and from opaque to transparent on removal.
- [scale](scale.md) — Returns a transition that scales the view.
- [scale(scale:anchor:)](<scale(scale_anchor_).md>) — Returns a transition that scales the view by the specified amount.
- [slide](slide.md) — A transition that inserts by moving in from the leading edge, and removes by moving out towards the trailing edge.
