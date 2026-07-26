---
title: 'init(rawValue:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unicode/utf8/validationerror/kind-swift.struct/init(rawvalue:)'
source_url: 'https://developer.apple.com/documentation/swift/unicode/utf8/validationerror/kind-swift.struct/init(rawvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/utf8/validationerror/kind-swift.struct/init%28rawvalue%3A%29.json'
content_hash: 'sha256:b4c83e77387fe440'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Swift](../../../../../swift.md) · [Unicode](../../../../unicode.md) · [UTF8](../../../utf8.md) · [ValidationError](../../validationerror.md) · [Kind](../kind-swift.struct.md)

# init(rawValue:)

<sub>Initializer</sub>

Creates a new instance with the specified raw value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(rawValue: UInt8)
```

## Parameters

- `rawValue` — The raw value to use for the new instance.

## Discussion

If there is no value of the type that corresponds with the specified raw value, this initializer returns `nil`. For example:

```swift
enum PaperSize: String {
    case A4, A5, Letter, Legal
}

print(PaperSize(rawValue: "Legal"))
// Prints "Optional(PaperSize.Legal)"

print(PaperSize(rawValue: "Tabloid"))
// Prints "nil"
```
