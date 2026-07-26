---
title: Void
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/void
source_url: 'https://developer.apple.com/documentation/swift/void'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/void.json'
content_hash: 'sha256:be72b1a03c3c54e9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Void

<sub>Type Alias</sub>

The return type of functions that don’t explicitly specify a return type, that is, an empty tuple `()`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Void = ()
```

## Discussion

When declaring a function or method, you don’t need to specify a return type if no value will be returned. However, the type of a function, method, or closure always includes a return type, which is `Void` if otherwise unspecified.

Use `Void` or an empty tuple as the return type when declaring a closure, function, or method that doesn’t return a value.

```swift
// No return type declared:
func logMessage(_ s: String) {
    print("Message: \(s)")
}

let logger: (String) -> Void = logMessage
logger("This is a void function")
// Prints "Message: This is a void function"
```
