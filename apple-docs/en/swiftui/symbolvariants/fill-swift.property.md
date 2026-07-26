---
title: fill
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/symbolvariants/fill-swift.property
source_url: 'https://developer.apple.com/documentation/swiftui/symbolvariants/fill-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/symbolvariants/fill-swift.property.json'
content_hash: 'sha256:e43184b92b59ab2d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SymbolVariants](../symbolvariants.md)

# fill

<sub>Instance Property</sub>

A filled version of the variant.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var fill: SymbolVariants { get }
```

## Discussion

Use this property to modify a shape variant like [circle](circle-swift.type.property.md) so that it’s also filled:

```swift
Label("Circle Fill", systemImage: "flag")
    .symbolVariant(.circle.fill)
```

![A screenshot of a label that shows a flag in a filled circle](../../../../attachments/bfe960b3acc307e9c52f35cbe25c29c7/SymbolVariants-fill-2@2x.png)

## See Also

### Modifying a variant

- [circle](circle-swift.property.md) — A version of the variant that’s encapsulated in a circle.
- [square](square-swift.property.md) — A version of the variant that’s encapsulated in a square.
- [rectangle](rectangle-swift.property.md) — A version of the variant that’s encapsulated in a rectangle.
- [slash](slash-swift.property.md) — A slashed version of the variant.
