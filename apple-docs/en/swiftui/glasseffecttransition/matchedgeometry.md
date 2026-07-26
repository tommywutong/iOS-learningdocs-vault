---
title: matchedGeometry
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/glasseffecttransition/matchedgeometry
source_url: 'https://developer.apple.com/documentation/swiftui/glasseffecttransition/matchedgeometry'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/glasseffecttransition/matchedgeometry.json'
content_hash: 'sha256:fb75e7bf88b2c811'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GlassEffectTransition](../glasseffecttransition.md)

# matchedGeometry

<sub>Type Property</sub>

Returns the matched geometry glass effect transition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
static var matchedGeometry: GlassEffectTransition { get }
```

## Discussion

The matched geometry transition allows the geometries of glass shapes during an appearance or disappearance phase of a transition to be derived from the geometry of a nearby shape within the glass container.

For example, if a newly appearing shape is within the spacing of any existing shape, it will use that shapes geometry to transition out of.

When using the [default](../animation/default.md), this transition applies additional scale and offset effects to content when the identity of the shape does not change but its content does. Opt out of these additional animations by providing a specific animation like [spring](../animation/spring.md).
