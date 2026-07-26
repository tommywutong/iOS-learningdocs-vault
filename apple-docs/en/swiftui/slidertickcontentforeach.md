---
title: SliderTickContentForEach
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/slidertickcontentforeach
source_url: 'https://developer.apple.com/documentation/swiftui/slidertickcontentforeach'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/slidertickcontentforeach.json'
content_hash: 'sha256:00ad47b1797a60a8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SliderTickContentForEach

<sub>Structure</sub>

A type of slider content that creates content by iterating over a collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
struct SliderTickContentForEach<Data, ID, Content> where Data : RandomAccessCollection, ID : Hashable, Content : SliderTickContent
```

## Relationships

- **Conforms To**: [SliderTickContent](slidertickcontent.md)

## Topics

### Initializers

- [init(_:content:)](<slidertickcontentforeach/init(__content_).md>) — Creates an instance that uniquely identifies and creates slider ticks across updates based on the identity of the underlying data.
- [init(_:id:content:)](<slidertickcontentforeach/init(__id_content_).md>) — Creates an instance that uniquely identifies and creates slider ticks across updates based on the provided key path to the underlying data’s identifier.

## See Also

### Adding ticks to a slider

- [SliderTick](slidertick.md) — A representation of a tick in a slider, with associated value and optional label.
- [SliderTickBuilder](slidertickbuilder.md) — A result builder that constructs `SliderTick`s for use when creating a `Slider`.
- [TupleSliderTickContent](tupleslidertickcontent.md) — Slider content created from a Swift tuple of slider content.
- [SliderTickContent](slidertickcontent.md) — A type that provides content for a `SliderTickBuilder`.
