---
title: 'init(exactly:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/binaryfloatingpoint/init(exactly:)-6fobm'
source_url: 'https://developer.apple.com/documentation/swift/binaryfloatingpoint/init(exactly:)-6fobm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/binaryfloatingpoint/init%28exactly%3A%29-6fobm.json'
content_hash: 'sha256:9efa9c289ca1ed47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BinaryFloatingPoint](../binaryfloatingpoint.md)

# init(exactly:)

<sub>Initializer</sub>

Creates a new instance from the given value, if it can be represented exactly.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?<Source>(exactly value: Source) where Source : BinaryFloatingPoint
```

## Parameters

- `value` — A floating-point value to be converted.

## Discussion

If the given floating-point value cannot be represented exactly, the result is `nil`.
