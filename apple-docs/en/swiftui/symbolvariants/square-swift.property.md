---
title: square
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/symbolvariants/square-swift.property
source_url: 'https://developer.apple.com/documentation/swiftui/symbolvariants/square-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/symbolvariants/square-swift.property.json'
content_hash: 'sha256:419405b61d3930be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SymbolVariants](../symbolvariants.md)

# square

<sub>Instance Property</sub>

A version of the variant that’s encapsulated in a square.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var square: SymbolVariants { get }
```

## Discussion

Use this property to modify a variant like [fill](fill-swift.property.md) so that it’s also contained in a square:

```swift
Label("Fill Square", systemImage: "star")
    .symbolVariant(.fill.square)
```

![A screenshot of a label that shows a star in a filled square](../../../../attachments/591d44c3cb28ab6dd1362093cff5fbd7/SymbolVariants-square-2@2x.png)

## See Also

### Modifying a variant

- [circle](circle-swift.property.md) — A version of the variant that’s encapsulated in a circle.
- [rectangle](rectangle-swift.property.md) — A version of the variant that’s encapsulated in a rectangle.
- [fill](fill-swift.property.md) — A filled version of the variant.
- [slash](slash-swift.property.md) — A slashed version of the variant.
