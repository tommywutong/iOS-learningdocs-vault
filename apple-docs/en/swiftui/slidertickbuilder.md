---
title: SliderTickBuilder
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/slidertickbuilder
source_url: 'https://developer.apple.com/documentation/swiftui/slidertickbuilder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/slidertickbuilder.json'
content_hash: 'sha256:f0c4a58d1b6530f4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SliderTickBuilder

<sub>Structure</sub>

A result builder that constructs `SliderTick`s for use when creating a `Slider`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@resultBuilder struct SliderTickBuilder<V> where V : BinaryFloatingPoint
```

## Topics

### Type Methods

- [buildBlock()](<slidertickbuilder/buildblock().md>) — Creates a single slider content result.
- [buildBlock(_:)](<slidertickbuilder/buildblock(__).md>) — Creates a single slider content result.
- [buildBlock(_:_:)](<slidertickbuilder/buildblock(____).md>)
- [buildBlock(_:_:_:)](<slidertickbuilder/buildblock(______).md>)
- [buildBlock(_:_:_:_:)](<slidertickbuilder/buildblock(________).md>)
- [buildBlock(_:_:_:_:_:)](<slidertickbuilder/buildblock(__________).md>)
- [buildBlock(_:_:_:_:_:_:)](<slidertickbuilder/buildblock(____________).md>)
- [buildBlock(_:_:_:_:_:_:_:)](<slidertickbuilder/buildblock(______________).md>)
- [buildBlock(_:_:_:_:_:_:_:_:)](<slidertickbuilder/buildblock(________________).md>)
- [buildBlock(_:_:_:_:_:_:_:_:_:)](<slidertickbuilder/buildblock(__________________).md>)
- [buildBlock(_:_:_:_:_:_:_:_:_:_:)](<slidertickbuilder/buildblock(____________________).md>)
- [buildEither(first:)](<slidertickbuilder/buildeither(first_).md>) — Produces content for a conditional statement in a multi-statement closure when the condition is true.
- [buildEither(second:)](<slidertickbuilder/buildeither(second_).md>) — Produces content for a conditional statement in a multi-statement closure when the condition is false.
- [buildExpression(_:)](<slidertickbuilder/buildexpression(__).md>) — Creates a single slider content expression.
- [buildIf(_:)](<slidertickbuilder/buildif(__).md>) — Produces an optional slider content for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.

## See Also

### Adding ticks to a slider

- [SliderTick](slidertick.md) — A representation of a tick in a slider, with associated value and optional label.
- [SliderTickContentForEach](slidertickcontentforeach.md) — A type of slider content that creates content by iterating over a collection.
- [TupleSliderTickContent](tupleslidertickcontent.md) — Slider content created from a Swift tuple of slider content.
- [SliderTickContent](slidertickcontent.md) — A type that provides content for a `SliderTickBuilder`.
