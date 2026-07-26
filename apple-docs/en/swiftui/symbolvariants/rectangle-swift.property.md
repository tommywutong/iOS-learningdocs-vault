---
title: rectangle
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/symbolvariants/rectangle-swift.property
source_url: 'https://developer.apple.com/documentation/swiftui/symbolvariants/rectangle-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/symbolvariants/rectangle-swift.property.json'
content_hash: 'sha256:5515dc63db055973'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SymbolVariants](../symbolvariants.md)

# rectangle

<sub>Instance Property</sub>

A version of the variant that’s encapsulated in a rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var rectangle: SymbolVariants { get }
```

## Discussion

Use this property to modify a variant like [fill](fill-swift.property.md) so that it’s also contained in a rectangle:

```swift
Label("Fill Rectangle", systemImage: "plus")
    .symbolVariant(.fill.rectangle)
```

![A screenshot of a label that shows a plus sign in a filled rectangle](../../../../attachments/e149c895cf10d709dc7bd7c57ccddd00/SymbolVariants-rectangle-2@2x.png)

## See Also

### Modifying a variant

- [circle](circle-swift.property.md) — A version of the variant that’s encapsulated in a circle.
- [square](square-swift.property.md) — A version of the variant that’s encapsulated in a square.
- [fill](fill-swift.property.md) — A filled version of the variant.
- [slash](slash-swift.property.md) — A slashed version of the variant.
