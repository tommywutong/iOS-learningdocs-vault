---
title: toggle()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/bool/toggle()
source_url: 'https://developer.apple.com/documentation/swift/bool/toggle()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/bool/toggle%28%29.json'
content_hash: 'sha256:b7b753d21fa3c658'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Bool](../bool.md)

# toggle()

<sub>Instance Method</sub>

Toggles the Boolean variable’s value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func toggle()
```

## Discussion

Use this method to toggle a Boolean value from `true` to `false` or from `false` to `true`.

```swift
var bools = [true, false]

bools[0].toggle()
// bools == [false, false]
```

## See Also

### Transforming a Boolean

- [!(_:)](<!(__).md>) — Performs a logical NOT operation on a Boolean value.
- [||(_:_:)](<__(____).md>) — Performs a logical OR operation on two Boolean values.
- [&&(_:_:)](<&&(____).md>) — Performs a logical AND operation on two Boolean values.
