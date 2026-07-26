---
title: 'init(rawValue:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/floatingpointsign/init(rawvalue:)'
source_url: 'https://developer.apple.com/documentation/swift/floatingpointsign/init(rawvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpointsign/init%28rawvalue%3A%29.json'
content_hash: 'sha256:99ca340fb4e8d311'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPointSign](../floatingpointsign.md)

# init(rawValue:)

<sub>Initializer</sub>

Creates a new instance with the specified raw value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(rawValue: Int)
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
