---
title: rawValue
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/taskpriority/rawvalue-swift.property
source_url: 'https://developer.apple.com/documentation/swift/taskpriority/rawvalue-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/taskpriority/rawvalue-swift.property.json'
content_hash: 'sha256:a4d25d1af2171cb6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [TaskPriority](../taskpriority.md)

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
