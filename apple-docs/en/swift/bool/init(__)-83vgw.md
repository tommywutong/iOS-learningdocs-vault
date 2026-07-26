---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/bool/init(_:)-83vgw'
source_url: 'https://developer.apple.com/documentation/swift/bool/init(_:)-83vgw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/bool/init%28_%3A%29-83vgw.json'
content_hash: 'sha256:26bbaacc4b7c39f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Bool](../bool.md)

# init(_:)

<sub>Initializer</sub>

Creates a new Boolean value from the given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(_ description: String)
```

## Parameters

- `description` — A string representation of the Boolean value.

## Discussion

If the `description` value is any string other than `"true"` or `"false"`, the result is `nil`. This initializer is case sensitive.

## See Also

### Creating a Boolean From Another Value

- [init(_:)](<init(__)-25sp9.md>) — Creates an instance equal to the given Boolean value.
