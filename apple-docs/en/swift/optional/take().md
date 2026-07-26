---
title: take()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/optional/take()
source_url: 'https://developer.apple.com/documentation/swift/optional/take()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/optional/take%28%29.json'
content_hash: 'sha256:1dd0b08261a49eeb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Optional](../optional.md)

# take()

<sub>Instance Method</sub>

Takes the wrapped value being stored in this instance and returns it while also setting the instance to `nil`. If there is no value being stored in this instance, this returns `nil` instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func take() -> Optional<Wrapped>
```

## Return Value

The wrapped value being stored in this instance. If this instance is `nil`, returns `nil`.

## Discussion

```swift
var numberOfShoes: Int? = 34

if let numberOfShoes = numberOfShoes.take() {
  print(numberOfShoes)
  // Prints "34"
}

print(numberOfShoes)
// Prints "nil"
```
