---
title: slash
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/symbolvariants/slash-swift.property
source_url: 'https://developer.apple.com/documentation/swiftui/symbolvariants/slash-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/symbolvariants/slash-swift.property.json'
content_hash: 'sha256:298bc4db3ba13895'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SymbolVariants](../symbolvariants.md)

# slash

<sub>Instance Property</sub>

A slashed version of the variant.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var slash: SymbolVariants { get }
```

## Discussion

Use this property to modify a shape variant like [circle](circle-swift.type.property.md) so that it’s also covered by a slash:

```swift
Label("Circle Slash", systemImage: "flag")
    .symbolVariant(.circle.slash)
```

![A screenshot of a label that shows a flag in a circle with a](../../../../attachments/1c6f71949288c728089e2dd937cb61dd/SymbolVariants-slash-2@2x.png)

## See Also

### Modifying a variant

- [circle](circle-swift.property.md) — A version of the variant that’s encapsulated in a circle.
- [square](square-swift.property.md) — A version of the variant that’s encapsulated in a square.
- [rectangle](rectangle-swift.property.md) — A version of the variant that’s encapsulated in a rectangle.
- [fill](fill-swift.property.md) — A filled version of the variant.
