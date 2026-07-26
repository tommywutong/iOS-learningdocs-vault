---
title: SliderTick
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/slidertick
source_url: 'https://developer.apple.com/documentation/swiftui/slidertick'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/slidertick.json'
content_hash: 'sha256:d2b8472be5b59260'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SliderTick

<sub>Structure</sub>

A representation of a tick in a slider, with associated value and optional label.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
struct SliderTick<V> where V : BinaryFloatingPoint
```

## Overview

The following example shows a slider bound to the value `percentage`. As the slider updates the `currentValueLabel`. The slider also renders marks at a `0.25` step interval.

```swift
@State private var percentage = 0.5

Slider(value: $percentage) {
    Text("Percentage")
} currentValueLabel: {
    Text("\(percentage)%")
} ticks: {
    SliderTickContentForEach(
        stride(from: 0.0, through: 1.0, by: 0.25).map { $0 },
        id: \.self
    ) { value in
        SliderTick(value) {
            label(for: value)
        }
    }
}
```

## Relationships

- **Conforms To**: [Comparable](../swift/comparable.md), [Equatable](../swift/equatable.md), [Identifiable](../swift/identifiable.md), [SliderTickContent](slidertickcontent.md)

## Topics

### Structures

- [ID](slidertick/id-swift.struct.md) — The identity of a tick.

### Initializers

- [init(_:)](<slidertick/init(__).md>) — Create a labeled slider tick at a specific value.
- [init(_:_:)](<slidertick/init(____).md>) — Create a slider tick with a label from a localized string key.
- [init(_:label:)](<slidertick/init(__label_).md>) — Create a labeled slider tick at a specific value.

### Instance Properties

- [id](slidertick/id-swift.property.md) — The identity of a tick, which is derived from its value.

## See Also

### Adding ticks to a slider

- [SliderTickBuilder](slidertickbuilder.md) — A result builder that constructs `SliderTick`s for use when creating a `Slider`.
- [SliderTickContentForEach](slidertickcontentforeach.md) — A type of slider content that creates content by iterating over a collection.
- [TupleSliderTickContent](tupleslidertickcontent.md) — Slider content created from a Swift tuple of slider content.
- [SliderTickContent](slidertickcontent.md) — A type that provides content for a `SliderTickBuilder`.
