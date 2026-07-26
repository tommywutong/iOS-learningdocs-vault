---
title: debugDescription
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/staticbigint/debugdescription
source_url: 'https://developer.apple.com/documentation/swift/staticbigint/debugdescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/staticbigint/debugdescription.json'
content_hash: 'sha256:e90b989018d38717'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StaticBigInt](../staticbigint.md)

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
