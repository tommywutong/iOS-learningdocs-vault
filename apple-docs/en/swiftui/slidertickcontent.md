---
title: SliderTickContent
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/slidertickcontent
source_url: 'https://developer.apple.com/documentation/swiftui/slidertickcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/slidertickcontent.json'
content_hash: 'sha256:94354838a4279a0b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SliderTickContent

<sub>Protocol</sub>

A type that provides content for a `SliderTickBuilder`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
protocol SliderTickContent<Value>
```

## Relationships

- **Conforming Types**: [SliderTick](slidertick.md), [SliderTickContentForEach](slidertickcontentforeach.md), [TupleSliderTickContent](tupleslidertickcontent.md)

## Topics

### Associated Types

- [Body](slidertickcontent/body-swift.associatedtype.md)
- [Value](slidertickcontent/value.md)

### Instance Properties

- [body](slidertickcontent/body-swift.property.md) — The value of this type’s content.

## See Also

### Adding ticks to a slider

- [SliderTick](slidertick.md) — A representation of a tick in a slider, with associated value and optional label.
- [SliderTickBuilder](slidertickbuilder.md) — A result builder that constructs `SliderTick`s for use when creating a `Slider`.
- [SliderTickContentForEach](slidertickcontentforeach.md) — A type of slider content that creates content by iterating over a collection.
- [TupleSliderTickContent](tupleslidertickcontent.md) — Slider content created from a Swift tuple of slider content.
