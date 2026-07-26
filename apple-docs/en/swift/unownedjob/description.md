---
title: description
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unownedjob/description
source_url: 'https://developer.apple.com/documentation/swift/unownedjob/description'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unownedjob/description.json'
content_hash: 'sha256:f9912d29a1de4188'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnownedJob](../unownedjob.md)

# description

<sub>Instance Property</sub>

A textual representation of this instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var description: String { get }
```

## Discussion

Calling this property directly is discouraged. Instead, convert an instance of any type to a string by using the `String(describing:)` initializer. This initializer works with any type, and uses the custom `description` property for types that conform to `CustomStringConvertible`:

```swift
struct Point: CustomStringConvertible {
    let x: Int, y: Int

    var description: String {
        return "(\(x), \(y))"
    }
}

let p = Point(x: 21, y: 30)
let s = String(describing: p)
print(s)
// Prints "(21, 30)"
```

The conversion of `p` to a string in the assignment to `s` uses the `Point` type’s `description` property.
