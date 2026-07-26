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
doc_path: '/documentation/swift/objectidentifier/init(_:)-223xw'
source_url: 'https://developer.apple.com/documentation/swift/objectidentifier/init(_:)-223xw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/objectidentifier/init%28_%3A%29-223xw.json'
content_hash: 'sha256:a98b878fdbf0fc0a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ObjectIdentifier](../objectidentifier.md)

# init(_:)

<sub>Initializer</sub>

Creates an instance that uniquely identifies the given class instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ x: AnyObject)
```

## Parameters

- `x` — An instance of a class.

## Discussion

The following example creates an example class `IntegerRef` and compares instances of the class using their object identifiers and the identical-to operator (`===`):

```swift
class IntegerRef {
    let value: Int
    init(_ value: Int) {
        self.value = value
    }
}

let x = IntegerRef(10)
let y = x

print(ObjectIdentifier(x) == ObjectIdentifier(y))
// Prints "true"
print(x === y)
// Prints "true"

let z = IntegerRef(10)
print(ObjectIdentifier(x) == ObjectIdentifier(z))
// Prints "false"
print(x === z)
// Prints "false"
```
