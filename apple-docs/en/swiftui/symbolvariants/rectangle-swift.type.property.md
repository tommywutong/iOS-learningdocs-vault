---
title: rectangle
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/symbolvariants/rectangle-swift.type.property
source_url: 'https://developer.apple.com/documentation/swiftui/symbolvariants/rectangle-swift.type.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/symbolvariants/rectangle-swift.type.property.json'
content_hash: 'sha256:fbfda6c498b71142'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SymbolVariants](../symbolvariants.md)

# rectangle

<sub>Type Property</sub>

A variant that encapsulates the symbol in a rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let rectangle: SymbolVariants
```

## Discussion

Use this variant with a call to the [symbolVariant(_:)](<../view/symbolvariant(__).md>) modifier to draw symbols in a rectangle, for those symbols that have a rectangle variant:

```swift
VStack(spacing: 20) {
    HStack(spacing: 20) {
        Image(systemName: "plus")
        Image(systemName: "minus")
        Image(systemName: "xmark")
        Image(systemName: "checkmark")
    }
    HStack(spacing: 20) {
        Image(systemName: "plus")
        Image(systemName: "minus")
        Image(systemName: "xmark")
        Image(systemName: "checkmark")
    }
    .symbolVariant(.rectangle)
}
```

![A screenshot showing two rows of four symbols each. Both rows contain](../../../../attachments/2494a548c163c3f2b07cf16fdbad8fd1/SymbolVariants-rectangle-1@2x.png)

## See Also

### Getting symbol variants

- [none](none.md) — No variant for a symbol.
- [circle](circle-swift.type.property.md) — A variant that encapsulates the symbol in a circle.
- [square](square-swift.type.property.md) — A variant that encapsulates the symbol in a square.
- [fill](fill-swift.type.property.md) — A variant that fills the symbol.
- [slash](slash-swift.type.property.md) — A variant that draws a slash through the symbol.
