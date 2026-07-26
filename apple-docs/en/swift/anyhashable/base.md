---
title: base
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/anyhashable/base
source_url: 'https://developer.apple.com/documentation/swift/anyhashable/base'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anyhashable/base.json'
content_hash: 'sha256:6211c986903bd784'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AnyHashable](../anyhashable.md)

# base

<sub>Instance Property</sub>

The value wrapped by this instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var base: Any { get }
```

## Discussion

The `base` property can be cast back to its original type using one of the type casting operators (`as?`, `as!`, or `as`).

```swift
let anyMessage = AnyHashable("Hello world!")
if let unwrappedMessage = anyMessage.base as? String {
    print(unwrappedMessage)
}
// Prints "Hello world!"
```
