---
title: debugDescription
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/customdebugstringconvertible/debugdescription
source_url: 'https://developer.apple.com/documentation/swift/customdebugstringconvertible/debugdescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/customdebugstringconvertible/debugdescription.json'
content_hash: 'sha256:d45cd0cb46fb4426'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [CustomDebugStringConvertible](../customdebugstringconvertible.md)

# debugDescription

<sub>Instance Property</sub>

A textual representation of this instance, suitable for debugging.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var debugDescription: String { get }
```

## Discussion

Calling this property directly is discouraged. Instead, convert an instance of any type to a string by using the `String(reflecting:)` initializer. This initializer works with any type, and uses the custom `debugDescription` property for types that conform to `CustomDebugStringConvertible`:

```swift
struct Point: CustomDebugStringConvertible {
    let x: Int, y: Int

    var debugDescription: String {
        return "(\(x), \(y))"
    }
}

let p = Point(x: 21, y: 30)
let s = String(reflecting: p)
print(s)
// Prints "(21, 30)"
```

The conversion of `p` to a string in the assignment to `s` uses the `Point` type’s `debugDescription` property.

## Default Implementations

### CustomDebugStringConvertible Implementations

- [debugDescription](debugdescription-1omzk.md) — A textual representation of this key, suitable for debugging.
