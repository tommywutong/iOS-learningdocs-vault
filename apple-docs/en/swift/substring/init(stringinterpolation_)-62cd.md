---
title: 'init(stringInterpolation:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/substring/init(stringinterpolation:)-62cd'
source_url: 'https://developer.apple.com/documentation/swift/substring/init(stringinterpolation:)-62cd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/init%28stringinterpolation%3A%29-62cd.json'
content_hash: 'sha256:8ce33da150404596'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Substring](../substring.md)

# init(stringInterpolation:)

<sub>Initializer</sub>

Creates a new instance from an interpolated string literal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(stringInterpolation: DefaultStringInterpolation)
```

## Discussion

Don’t call this initializer directly. It’s used by the compiler when you create a string using string interpolation. Instead, use string interpolation to create a new string by including values, literals, variables, or expressions enclosed in parentheses, prefixed by a backslash (`\(`…`)`).

```swift
let price = 2
let number = 3
let message = """
              If one cookie costs \(price) dollars, \
              \(number) cookies cost \(price * number) dollars.
              """
// message == "If one cookie costs 2 dollars, 3 cookies cost 6 dollars."
```
