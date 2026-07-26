---
title: circle
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/symbolvariants/circle-swift.type.property
source_url: 'https://developer.apple.com/documentation/swiftui/symbolvariants/circle-swift.type.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/symbolvariants/circle-swift.type.property.json'
content_hash: 'sha256:dcef20768b49f072'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SymbolVariants](../symbolvariants.md)

# circle

<sub>Type Property</sub>

A variant that encapsulates the symbol in a circle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let circle: SymbolVariants
```

## Discussion

Use this variant with a call to the [symbolVariant(_:)](<../view/symbolvariant(__).md>) modifier to draw symbols in a circle, for those symbols that have a circle variant:

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
    .symbolVariant(.circle)
}
```

![A screenshot showing two rows of four symbols each. Both rows contain](../../../../attachments/313716351d351d7abf80e497e3bbe91b/SymbolVariants-circle-1@2x.png)

## See Also

### Getting symbol variants

- [none](none.md) — No variant for a symbol.
- [square](square-swift.type.property.md) — A variant that encapsulates the symbol in a square.
- [rectangle](rectangle-swift.type.property.md) — A variant that encapsulates the symbol in a rectangle.
- [fill](fill-swift.type.property.md) — A variant that fills the symbol.
- [slash](slash-swift.type.property.md) — A variant that draws a slash through the symbol.
