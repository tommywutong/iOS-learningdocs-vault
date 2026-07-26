---
title: AnimatablePair
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/animatablepair
source_url: 'https://developer.apple.com/documentation/swiftui/animatablepair'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animatablepair.json'
content_hash: 'sha256:65f2c2f5c5a0bb00'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AnimatablePair

<sub>Structure</sub>

A pair of animatable values, which is itself animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct AnimatablePair<First, Second> where First : VectorArithmetic, Second : VectorArithmetic
```

## Relationships

- **Conforms To**: [AdditiveArithmetic](../swift/additivearithmetic.md), [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [VectorArithmetic](vectorarithmetic.md)

## Topics

### Creating an animatable pair

- [init(_:_:)](<animatablepair/init(____).md>) — Creates an animated pair with the provided values.

### Getting the constituent animations

- [first](animatablepair/first.md) — The first value.
- [second](animatablepair/second.md) — The second value.

### Manipulating values

- [magnitudeSquared](animatablepair/magnitudesquared.md) — The dot-product of this animated pair with itself.

## See Also

### Making data animatable

- [Animatable](animatable.md) — A type that describes how to animate a property of a view.
- [AnimatableValues](animatablevalues.md)
- [VectorArithmetic](vectorarithmetic.md) — A type that can serve as the animatable data of an animatable type.
- [EmptyAnimatableData](emptyanimatabledata.md) — An empty type for animatable data.
