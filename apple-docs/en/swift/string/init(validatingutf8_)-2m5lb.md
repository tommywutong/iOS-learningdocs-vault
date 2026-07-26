---
title: 'init(validatingUTF8:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+, Swift（6.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/swift/string/init(validatingutf8:)-2m5lb'
source_url: 'https://developer.apple.com/documentation/swift/string/init(validatingutf8:)-2m5lb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/init%28validatingutf8%3A%29-2m5lb.json'
content_hash: 'sha256:a82b46140d3537cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# init(validatingUTF8:)

<sub>Initializer</sub>

Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(validatingUTF8 cString: [CChar])
```

## Parameters

- `cString` — An array containing a null-terminated sequence of UTF-8 code units.

## Discussion

This initializer does not try to repair ill-formed UTF-8 code unit sequences. If any are found, the result of the initializer is `nil`.

> [!note] Note
> This initializer is deprecated. Use the initializer `String.init?(validating: array, as: UTF8.self)` instead, remembering that “\\0” is a valid character in Swift.
