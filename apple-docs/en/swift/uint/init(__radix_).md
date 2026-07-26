---
title: 'init(_:radix:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/uint/init(_:radix:)'
source_url: 'https://developer.apple.com/documentation/swift/uint/init(_:radix:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint/init%28_%3Aradix%3A%29.json'
content_hash: 'sha256:b670735ce762ffec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt](../uint.md)

# init(_:radix:)

<sub>Initializer</sub>

Creates a new integer value from the given string and radix.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?<S>(_ text: S, radix: Int = 10) where S : StringProtocol
```

## Parameters

- `text` — The ASCII representation of a number in the radix passed as `radix`.

- `radix` — The radix, or base, to use for converting `text` to an integer value. `radix` must be in the range `2...36`. The default is 10.

## Discussion

The string passed as `text` may begin with a plus or minus sign character (`+` or `-`), followed by one or more numeric digits (`0-9`) or letters (`a-z` or `A-Z`). Parsing of the string is case insensitive.

```swift
let x = Int("123")
// x == 123

let y = Int("-123", radix: 8)
// y == -83
let y = Int("+123", radix: 8)
// y == +83

let z = Int("07b", radix: 16)
// z == 123
```

If `text` is in an invalid format or contains characters that are out of bounds for the given `radix`, or if the value it denotes in the given `radix` is not representable, the result is `nil`. For example, the following conversions result in `nil`:

```swift
Int(" 100")                       // Includes whitespace
Int("21-50")                      // Invalid format
Int("ff6600")                     // Characters out of bounds
Int("zzzzzzzzzzzzz", radix: 36)   // Out of range
```
