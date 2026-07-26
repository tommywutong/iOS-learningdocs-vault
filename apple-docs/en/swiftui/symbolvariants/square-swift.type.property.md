---
title: square
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/symbolvariants/square-swift.type.property
source_url: 'https://developer.apple.com/documentation/swiftui/symbolvariants/square-swift.type.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/symbolvariants/square-swift.type.property.json'
content_hash: 'sha256:c42b74b175f96a9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SymbolVariants](../symbolvariants.md)

# square

<sub>Type Property</sub>

A variant that encapsulates the symbol in a square.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let square: SymbolVariants
```

## Discussion

Use this variant with a call to the [symbolVariant(_:)](<../view/symbolvariant(__).md>) modifier to draw symbols in a square, for those symbols that have a square variant:

```swift
VStack(spacing: 20) {
    HStack(spacing: 20) {
        Image(systemName: "flag")
        Image(systemName: "heart")
        Image(systemName: "bolt")
        Image(systemName: "star")
    }
    HStack(spacing: 20) {
        Image(systemName: "flag")
        Image(systemName: "heart")
        Image(systemName: "bolt")
        Image(systemName: "star")
    }
    .symbolVariant(.square)
}
```

![A screenshot showing two rows of four symbols each. Both rows contain](../../../../attachments/b7f04f50126637808d0319b25fa43b61/SymbolVariants-square-1@2x.png)

## See Also

### Getting symbol variants

- [none](none.md) — No variant for a symbol.
- [circle](circle-swift.type.property.md) — A variant that encapsulates the symbol in a circle.
- [rectangle](rectangle-swift.type.property.md) — A variant that encapsulates the symbol in a rectangle.
- [fill](fill-swift.type.property.md) — A variant that fills the symbol.
- [slash](slash-swift.type.property.md) — A variant that draws a slash through the symbol.
