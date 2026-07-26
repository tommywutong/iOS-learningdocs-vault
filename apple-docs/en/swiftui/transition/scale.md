---
title: scale
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/transition/scale
source_url: 'https://developer.apple.com/documentation/swiftui/transition/scale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/transition/scale.json'
content_hash: 'sha256:7613004dba76dc12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Transition](../transition.md)

# scale

<sub>Type Property</sub>

Returns a transition that scales the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency static var scale: ScaleTransition { get }
```

## See Also

### Getting built-in transitions

- [blurReplace](blurreplace.md) — A transition that animates the insertion or removal of a view by combining blurring and scaling effects.
- [blurReplace(_:)](<blurreplace(__).md>) — A transition that animates the insertion or removal of a view by combining blurring and scaling effects.
- [identity](identity.md) — A transition that returns the input view, unmodified, as the output view.
- [move(edge:)](<move(edge_).md>) — Returns a transition that moves the view away, towards the specified edge of the view.
- [offset(_:)](<offset(__).md>) — Returns a transition that offset the view by the specified amount.
- [offset(x:y:)](<offset(x_y_).md>) — Returns a transition that offset the view by the specified x and y values.
- [opacity](opacity.md) — A transition from transparent to opaque on insertion, and from opaque to transparent on removal.
- [push(from:)](<push(from_).md>) — Creates a transition that when added to a view will animate the view’s insertion by moving it in from the specified edge while fading it in, and animate its removal by moving it out towards the opposite edge and fading it out.
- [scale(_:anchor:)](<scale(__anchor_).md>) — Returns a transition that scales the view by the specified amount.
- [slide](slide.md) — A transition that inserts by moving in from the leading edge, and removes by moving out towards the trailing edge.
- [symbolEffect](symboleffect.md) — A transition that applies the default symbol effect transition to symbol images within the inserted or removed view hierarchy. Other views are unaffected by this transition.
- [symbolEffect(_:options:)](<symboleffect(__options_).md>) — Creates a transition that applies the provided effect to symbol images within the inserted or removed view hierarchy. Other views are unaffected by this transition.
