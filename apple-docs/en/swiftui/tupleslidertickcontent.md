---
title: TupleSliderTickContent
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tupleslidertickcontent
source_url: 'https://developer.apple.com/documentation/swiftui/tupleslidertickcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tupleslidertickcontent.json'
content_hash: 'sha256:e78db3ce7261e3b1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TupleSliderTickContent

<sub>Structure</sub>

Slider content created from a Swift tuple of slider content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@frozen struct TupleSliderTickContent<V, T> where V : BinaryFloatingPoint
```

## Relationships

- **Conforms To**: [SliderTickContent](slidertickcontent.md)

## Topics

### Instance Properties

- [value](tupleslidertickcontent/value.md)

### Type Aliases

- [TicksCollection](tupleslidertickcontent/tickscollection.md)

## See Also

### Adding ticks to a slider

- [SliderTick](slidertick.md) — A representation of a tick in a slider, with associated value and optional label.
- [SliderTickBuilder](slidertickbuilder.md) — A result builder that constructs `SliderTick`s for use when creating a `Slider`.
- [SliderTickContentForEach](slidertickcontentforeach.md) — A type of slider content that creates content by iterating over a collection.
- [SliderTickContent](slidertickcontent.md) — A type that provides content for a `SliderTickBuilder`.
