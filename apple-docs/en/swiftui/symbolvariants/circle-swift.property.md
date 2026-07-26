---
title: circle
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/symbolvariants/circle-swift.property
source_url: 'https://developer.apple.com/documentation/swiftui/symbolvariants/circle-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/symbolvariants/circle-swift.property.json'
content_hash: 'sha256:860e5c39b8c29e9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SymbolVariants](../symbolvariants.md)

# circle

<sub>Instance Property</sub>

A version of the variant that’s encapsulated in a circle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var circle: SymbolVariants { get }
```

## Discussion

Use this property to modify a variant like [fill](fill-swift.property.md) so that it’s also contained in a circle:

```swift
Label("Fill Circle", systemImage: "bolt")
    .symbolVariant(.fill.circle)
```

![A screenshot of a label that shows a bolt in a filled circle](../../../../attachments/d867d29d80f41d3901708b97ef22d158/SymbolVariants-circle-2@2x.png)

## See Also

### Modifying a variant

- [square](square-swift.property.md) — A version of the variant that’s encapsulated in a square.
- [rectangle](rectangle-swift.property.md) — A version of the variant that’s encapsulated in a rectangle.
- [fill](fill-swift.property.md) — A filled version of the variant.
- [slash](slash-swift.property.md) — A slashed version of the variant.
