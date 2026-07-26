---
title: 'appendInterpolation(_:default:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/defaultstringinterpolation/appendinterpolation(_:default:)-64wk7'
source_url: 'https://developer.apple.com/documentation/swift/defaultstringinterpolation/appendinterpolation(_:default:)-64wk7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/defaultstringinterpolation/appendinterpolation%28_%3Adefault%3A%29-64wk7.json'
content_hash: 'sha256:905c9ec59551f7ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [DefaultStringInterpolation](../defaultstringinterpolation.md)

# appendInterpolation(_:default:)

<sub>Instance Method</sub>

Interpolates the given optional value’s textual representation, or the specified default string, into the string literal being created.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation<T>(_ value: T?, default: @autoclosure () -> some StringProtocol) where T : TextOutputStreamable
```

## Parameters

- `value` — The value to include in a string interpolation, if non-`nil`.

- `default` — The string to include if `value` is `nil`.

## Discussion

You don’t need to call this method directly. It’s used by the compiler when interpreting string interpolations where you provide a `default` parameter. For example, the following code implicitly calls this method, using the value of the `default` parameter when `value` is `nil`:

```swift
var age: Int? = 48
print("Your age is \(age, default: "unknown")")
// Prints: Your age is 48
age = nil
print("Your age is \(age, default: "unknown")")
// Prints: Your age is unknown
```
