---
title: rawValue
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/utf8/validationerror/kind-swift.struct/rawvalue-swift.property
source_url: 'https://developer.apple.com/documentation/swift/unicode/utf8/validationerror/kind-swift.struct/rawvalue-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/utf8/validationerror/kind-swift.struct/rawvalue-swift.property.json'
content_hash: 'sha256:9a780ea7f879711c'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Swift](../../../../../swift.md) · [Unicode](../../../../unicode.md) · [UTF8](../../../utf8.md) · [ValidationError](../../validationerror.md) · [Kind](../kind-swift.struct.md)

# rawValue

<sub>Instance Property</sub>

The corresponding value of the raw type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var rawValue: UInt8
```

## Discussion

A new instance initialized with `rawValue` will be equivalent to this instance. For example:

```swift
enum PaperSize: String {
    case A4, A5, Letter, Legal
}

let selectedSize = PaperSize.Letter
print(selectedSize.rawValue)
// Prints "Letter"

print(selectedSize == PaperSize(rawValue: selectedSize.rawValue)!)
// Prints "true"
```
