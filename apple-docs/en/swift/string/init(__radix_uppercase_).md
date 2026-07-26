---
title: 'init(_:radix:uppercase:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/init(_:radix:uppercase:)'
source_url: 'https://developer.apple.com/documentation/swift/string/init(_:radix:uppercase:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/init%28_%3Aradix%3Auppercase%3A%29.json'
content_hash: 'sha256:17a7ef1cd1e116e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# init(_:radix:uppercase:)

<sub>Initializer</sub>

Creates a string representing the given value in base 10, or some other specified base.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<T>(_ value: T, radix: Int = 10, uppercase: Bool = false) where T : BinaryInteger
```

## Parameters

- `value` — The value to convert to a string.

- `radix` — The base to use for the string representation. `radix` must be at least 2 and at most 36. The default is 10.

- `uppercase` — Pass `true` to use uppercase letters to represent numerals greater than 9, or `false` to use lowercase letters. The default is `false`.

## Discussion

The following example converts the maximal `Int` value to a string and prints its length:

```swift
let max = String(Int.max)
print("\(max) has \(max.count) digits.")
// Prints "9223372036854775807 has 19 digits."
```

Numerals greater than 9 are represented as Roman letters. These letters start with `"A"` if `uppercase` is `true`; otherwise, with `"a"`.

```swift
let v = 999_999
print(String(v, radix: 2))
// Prints "11110100001000111111"

print(String(v, radix: 16))
// Prints "f423f"
print(String(v, radix: 16, uppercase: true))
// Prints "F423F"
```
