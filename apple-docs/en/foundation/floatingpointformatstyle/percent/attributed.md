---
title: attributed
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/floatingpointformatstyle/percent/attributed
source_url: 'https://developer.apple.com/documentation/foundation/floatingpointformatstyle/percent/attributed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/floatingpointformatstyle/percent/attributed.json'
content_hash: 'sha256:ec5418c5002a56b7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [FloatingPointFormatStyle](../../floatingpointformatstyle.md) · [Percent](../percent.md)

# attributed

<sub>Instance Property</sub>

An attributed format style based on the floating-point percent format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var attributed: FloatingPointFormatStyle<Value>.Attributed { get }
```

## Discussion

Use this modifier to create an [Attributed](../attributed-swift.struct.md) instance, which formats values as [AttributedString](../../attributedstring.md) instances. These attributed strings contain attributes from the [NumberFormatAttributes](../../attributescopes/foundationattributes/numberformatattributes.md) attribute scope. Use these attributes to determine which runs of the attributed string represent different parts of the formatted value.

## See Also

### Creating attributed strings

- [Attributed](../attributed-swift.struct.md) — A format style that converts integers into attributed strings.
