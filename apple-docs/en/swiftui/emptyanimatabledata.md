---
title: EmptyAnimatableData
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/emptyanimatabledata
source_url: 'https://developer.apple.com/documentation/swiftui/emptyanimatabledata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/emptyanimatabledata.json'
content_hash: 'sha256:6857efbd40d5de80'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# EmptyAnimatableData

<sub>Structure</sub>

An empty type for animatable data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct EmptyAnimatableData
```

## Overview

This type is suitable for use as the `animatableData` property of types that do not have any animatable properties.

## Relationships

- **Conforms To**: [AdditiveArithmetic](../swift/additivearithmetic.md), [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [VectorArithmetic](vectorarithmetic.md)

## Topics

### Creating the data

- [init()](<emptyanimatabledata/init().md>)

### Manipulating the data

- [magnitudeSquared](emptyanimatabledata/magnitudesquared.md) — The dot-product of this animatable data instance with itself.

## See Also

### Making data animatable

- [Animatable](animatable.md) — A type that describes how to animate a property of a view.
- [AnimatableValues](animatablevalues.md)
- [AnimatablePair](animatablepair.md) — A pair of animatable values, which is itself animatable.
- [VectorArithmetic](vectorarithmetic.md) — A type that can serve as the animatable data of an animatable type.
