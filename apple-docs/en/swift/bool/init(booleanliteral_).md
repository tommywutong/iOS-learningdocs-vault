---
title: 'init(booleanLiteral:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/bool/init(booleanliteral:)'
source_url: 'https://developer.apple.com/documentation/swift/bool/init(booleanliteral:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/bool/init%28booleanliteral%3A%29.json'
content_hash: 'sha256:2660b7694c07f1c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Bool](../bool.md)

# init(booleanLiteral:)

<sub>Initializer</sub>

Creates an instance initialized to the specified Boolean literal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(booleanLiteral value: Bool)
```

## Parameters

- `value` — The value of the new instance.

## Discussion

Do not call this initializer directly. It is used by the compiler when you use a Boolean literal. Instead, create a new `Bool` instance by using one of the Boolean literals `true` or `false`.

```swift
var printedMessage = false

if !printedMessage {
    print("You look nice today!")
    printedMessage = true
}
// Prints "You look nice today!"
```

In this example, both assignments to the `printedMessage` variable call this Boolean literal initializer behind the scenes.

## See Also

### Infrequently Used Intializers

- [init()](<init().md>) — Creates an instance initialized to `false`.
