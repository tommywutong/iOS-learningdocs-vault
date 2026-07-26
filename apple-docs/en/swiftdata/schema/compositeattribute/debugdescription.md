---
title: debugDescription
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/schema/compositeattribute/debugdescription
source_url: 'https://developer.apple.com/documentation/swiftdata/schema/compositeattribute/debugdescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/schema/compositeattribute/debugdescription.json'
content_hash: 'sha256:55c4b6f0e969c02e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftData](../../../swiftdata.md) · [Schema](../../schema.md) · [CompositeAttribute](../compositeattribute.md)

# debugDescription

<sub>Instance Property</sub>

A textual representation of this instance, suitable for debugging.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
override final var debugDescription: String { get }
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
