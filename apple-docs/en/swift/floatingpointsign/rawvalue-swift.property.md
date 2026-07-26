---
title: rawValue
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floatingpointsign/rawvalue-swift.property
source_url: 'https://developer.apple.com/documentation/swift/floatingpointsign/rawvalue-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpointsign/rawvalue-swift.property.json'
content_hash: 'sha256:0bd32799b25adb83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPointSign](../floatingpointsign.md)

# rawValue

<sub>Instance Property</sub>

The corresponding value of the raw type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var rawValue: Int { get }
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
