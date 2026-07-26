---
title: 'canBeConverted(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/stringprotocol/canbeconverted(to:)'
source_url: 'https://developer.apple.com/documentation/swift/stringprotocol/canbeconverted(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stringprotocol/canbeconverted%28to%3A%29.json'
content_hash: 'sha256:67386c57e60c4c5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StringProtocol](../stringprotocol.md)

# canBeConverted(to:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the string can be converted to the specified encoding without loss of information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func canBeConverted(to encoding: String.Encoding) -> Bool
```

## Parameters

- `encoding` — A string encoding.

## Return Value

`true` if the string can be encoded in `encoding` without loss of information; otherwise, `false`.
