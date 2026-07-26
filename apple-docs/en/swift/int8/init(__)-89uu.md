---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int8/init(_:)-89uu'
source_url: 'https://developer.apple.com/documentation/swift/int8/init(_:)-89uu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int8/init%28_%3A%29-89uu.json'
content_hash: 'sha256:36bf7205ba9f7eea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int8](../int8.md)

# init(_:)

<sub>Initializer</sub>

Creates a new integer value from the given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(_ description: String)
```

## Parameters

- `description` — The ASCII representation of a number.

## Discussion

The string passed as `description` may begin with a plus or minus sign character (`+` or `-`), followed by one or more numeric digits (`0-9`).

```swift
let x = Int("123")
// x == 123
```

If `description` is in an invalid format, or if the value it denotes in base 10 is not representable, the result is `nil`. For example, the following conversions result in `nil`:

```swift
Int(" 100")                       // Includes whitespace
Int("21-50")                      // Invalid format
Int("ff6600")                     // Characters out of bounds
Int("10000000000000000000000000") // Out of range
```
