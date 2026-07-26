---
title: 'init(rawValue:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/taskpriority/init(rawvalue:)'
source_url: 'https://developer.apple.com/documentation/swift/taskpriority/init(rawvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/taskpriority/init%28rawvalue%3A%29.json'
content_hash: 'sha256:9343bdb6959c881a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [TaskPriority](../taskpriority.md)

# init(rawValue:)

<sub>Initializer</sub>

Creates a new instance with the specified raw value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(rawValue: UInt8)
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
