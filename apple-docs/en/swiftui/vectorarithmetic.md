---
title: VectorArithmetic
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/vectorarithmetic
source_url: 'https://developer.apple.com/documentation/swiftui/vectorarithmetic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/vectorarithmetic.json'
content_hash: 'sha256:f4029cea9042e0c8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# VectorArithmetic

<sub>Protocol</sub>

A type that can serve as the animatable data of an animatable type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol VectorArithmetic : AdditiveArithmetic
```

## Overview

`VectorArithmetic` extends the `AdditiveArithmetic` protocol with scalar multiplication and a way to query the vector magnitude of the value. Use this type as the `animatableData` associated type of a type that conforms to the [Animatable](animatable.md) protocol.

## Relationships

- **Inherits From**: [AdditiveArithmetic](../swift/additivearithmetic.md), [Equatable](../swift/equatable.md)

- **Conforming Types**: [AnimatablePair](animatablepair.md), [AnimatableValues](animatablevalues.md), [EmptyAnimatableData](emptyanimatabledata.md)

## Topics

### Manipulating values

- [magnitudeSquared](vectorarithmetic/magnitudesquared.md) — Returns the dot-product of this vector arithmetic instance with itself.
- [scale(by:)](<vectorarithmetic/scale(by_).md>) — Multiplies each component of this value by the given value.
- [scaled(by:)](<vectorarithmetic/scaled(by_).md>) — Returns a value with each component of this value multiplied by the given value.
- [interpolate(towards:amount:)](<vectorarithmetic/interpolate(towards_amount_).md>) — Interpolates this value with `other` by the specified `amount`.
- [interpolated(towards:amount:)](<vectorarithmetic/interpolated(towards_amount_).md>) — Returns this value interpolated with `other` by the specified `amount`.

## See Also

### Making data animatable

- [Animatable](animatable.md) — A type that describes how to animate a property of a view.
- [AnimatableValues](animatablevalues.md)
- [AnimatablePair](animatablepair.md) — A pair of animatable values, which is itself animatable.
- [EmptyAnimatableData](emptyanimatabledata.md) — An empty type for animatable data.
