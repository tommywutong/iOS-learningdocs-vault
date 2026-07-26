---
title: none
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/symbolvariants/none
source_url: 'https://developer.apple.com/documentation/swiftui/symbolvariants/none'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/symbolvariants/none.json'
content_hash: 'sha256:f16d9cc5a92a0536'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SymbolVariants](../symbolvariants.md)

# none

<sub>Type Property</sub>

No variant for a symbol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let none: SymbolVariants
```

## Discussion

Using this variant with the [symbolVariant(_:)](<../view/symbolvariant(__).md>) modifier doesn’t have any effect. Instead, to show a symbol that ignores the current variant, directly set the [symbolVariants](../environmentvalues/symbolvariants.md) environment value to `none` using the [environment(_:_:)](<../view/environment(____).md>) modifer:

```swift
HStack {
    Image(systemName: "heart")
    Image(systemName: "heart")
        .environment(\.symbolVariants, .none)
}
.symbolVariant(.fill)
```

![A screenshot of two heart symbols. The first is filled while the](../../../../attachments/0071b4dbd1f82a57559c954e321a4709/SymbolVariants-none-1@2x.png)

## See Also

### Getting symbol variants

- [circle](circle-swift.type.property.md) — A variant that encapsulates the symbol in a circle.
- [square](square-swift.type.property.md) — A variant that encapsulates the symbol in a square.
- [rectangle](rectangle-swift.type.property.md) — A variant that encapsulates the symbol in a rectangle.
- [fill](fill-swift.type.property.md) — A variant that fills the symbol.
- [slash](slash-swift.type.property.md) — A variant that draws a slash through the symbol.
