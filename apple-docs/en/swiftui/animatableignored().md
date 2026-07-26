---
title: AnimatableIgnored()
framework: SwiftUI
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/animatableignored()
source_url: 'https://developer.apple.com/documentation/swiftui/animatableignored()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animatableignored%28%29.json'
content_hash: 'sha256:3517dd11a95d5924'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AnimatableIgnored()

<sub>Macro</sub>

An accessor macro that marks a property of a type to be excluded from the `animatableData` synthesis:

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@attached(accessor, names: named(willSet)) macro AnimatableIgnored()
```

## Overview

```swift
@Animatable
struct CoolShape: Shape {
    var width: CGFloat
    var height: CGFloat
    @AnimatableIgnored var isVisible: Bool

    // ...
}
```

In the above example, the `isVisible` property of `CoolShape` will not be participating in the synthesis of `animatableData`.

## See Also

### Animating data

- [Animatable()](<animatable().md>) — A member and extension macro that, when applied to a struct, class or enum declaration, synthesizes the conformance to `Animatable` and its requirement, the `animatableData` property using the existing animatable properties of the type this macro is applied to.
- [animatableData](animatable/animatabledata-6nydg.md) — The data to animate.
- [AnimatableData](animatable/animatabledata-swift.associatedtype.md) — The type defining the data to animate.
