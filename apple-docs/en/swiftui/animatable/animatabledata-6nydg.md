---
title: animatableData
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/animatable/animatabledata-6nydg
source_url: 'https://developer.apple.com/documentation/swiftui/animatable/animatabledata-6nydg'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animatable/animatabledata-6nydg.json'
content_hash: 'sha256:d2ce3b7a5d586454'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Animatable](../animatable.md)

# animatableData

<sub>Instance Property</sub>

The data to animate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var animatableData: Self.AnimatableData { get set }
```

## Discussion

SwiftUI reads this property to capture the current vector representation of the animatable state, and writes it back on each animation frame with an interpolated value. The default implementation returns [EmptyAnimatableData](../emptyanimatabledata.md), meaning nothing is animated.

Use the [Animatable()](<../animatable().md>) macro to synthesize this property automatically. Implement it by hand only when you need custom interpolation logic such as clamping, normalization, or mapping to a derived value.

## Default Implementations

### Animatable Implementations

- [animatableData](animatabledata-1gesb.md) — The data to animate.
- [animatableData](animatabledata-bqi8.md) — The data to animate.

## See Also

### Animating data

- [Animatable()](<../animatable().md>) — A member and extension macro that, when applied to a struct, class or enum declaration, synthesizes the conformance to `Animatable` and its requirement, the `animatableData` property using the existing animatable properties of the type this macro is applied to.
- [AnimatableIgnored()](<../animatableignored().md>) — An accessor macro that marks a property of a type to be excluded from the `animatableData` synthesis:
- [AnimatableData](animatabledata-swift.associatedtype.md) — The type defining the data to animate.
