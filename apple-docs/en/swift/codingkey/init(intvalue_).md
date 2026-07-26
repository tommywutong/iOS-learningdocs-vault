---
title: 'init(intValue:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/codingkey/init(intvalue:)'
source_url: 'https://developer.apple.com/documentation/swift/codingkey/init(intvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/codingkey/init%28intvalue%3A%29.json'
content_hash: 'sha256:8506c835ce2ee2e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [CodingKey](../codingkey.md)

# init(intValue:)

<sub>Initializer</sub>

Creates a new instance from the specified integer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(intValue: Int)
```

## Parameters

- `intValue` — The integer value of the desired key.

## Discussion

If the value passed as `intValue` does not correspond to any instance of this type, the result is `nil`.
