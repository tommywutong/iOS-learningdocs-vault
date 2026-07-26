---
title: 'init(stringValue:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/codingkey/init(stringvalue:)'
source_url: 'https://developer.apple.com/documentation/swift/codingkey/init(stringvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/codingkey/init%28stringvalue%3A%29.json'
content_hash: 'sha256:b1fe89d7b1ac26c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [CodingKey](../codingkey.md)

# init(stringValue:)

<sub>Initializer</sub>

Creates a new instance from the given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(stringValue: String)
```

## Parameters

- `stringValue` — The string value of the desired key.

## Discussion

If the string passed as `stringValue` does not correspond to any instance of this type, the result is `nil`.
