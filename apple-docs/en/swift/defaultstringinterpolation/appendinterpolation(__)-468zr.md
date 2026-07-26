---
title: 'appendInterpolation(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/defaultstringinterpolation/appendinterpolation(_:)-468zr'
source_url: 'https://developer.apple.com/documentation/swift/defaultstringinterpolation/appendinterpolation(_:)-468zr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/defaultstringinterpolation/appendinterpolation%28_%3A%29-468zr.json'
content_hash: 'sha256:1efaf91800878105'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [DefaultStringInterpolation](../defaultstringinterpolation.md)

# appendInterpolation(_:)

<sub>Instance Method</sub>

Interpolates the given value’s textual representation into the string literal being created.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation<T>(_ value: T) where T : TextOutputStreamable
```

## Discussion

You don’t need to call this method directly. It’s used by the compiler when interpreting string interpolations. Instead, use string interpolation to create a new string by including values, literals, variables, or expressions enclosed in parentheses, prefixed by a backslash (`\(`…`)`).

```swift
let price = 2
let number = 3
let message = "If one cookie costs \(price) dollars, " +
              "\(number) cookies cost \(price * number) dollars."
print(message)
// Prints "If one cookie costs 2 dollars, 3 cookies cost 6 dollars."
```
