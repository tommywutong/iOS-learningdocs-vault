---
title: AnimatableValues
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/animatablevalues
source_url: 'https://developer.apple.com/documentation/swiftui/animatablevalues'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animatablevalues.json'
content_hash: 'sha256:94cbee72fbffc8c2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AnimatableValues

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct AnimatableValues<each Value> where repeat each Value : VectorArithmetic
```

## Relationships

- **Conforms To**: [AdditiveArithmetic](../swift/additivearithmetic.md), [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [VectorArithmetic](vectorarithmetic.md)

## Topics

### Initializers

- [init(_:)](<animatablevalues/init(__).md>) — Creates a tuple of animatable values.

### Instance Properties

- [magnitudeSquared](animatablevalues/magnitudesquared.md) — The dot-product of the tuple of animatable values with itself.
- [value](animatablevalues/value.md) — The tuple of values.

## See Also

### Making data animatable

- [Animatable](animatable.md) — A type that describes how to animate a property of a view.
- [AnimatablePair](animatablepair.md) — A pair of animatable values, which is itself animatable.
- [VectorArithmetic](vectorarithmetic.md) — A type that can serve as the animatable data of an animatable type.
- [EmptyAnimatableData](emptyanimatabledata.md) — An empty type for animatable data.
