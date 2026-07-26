---
title: 'EncodingError.invalidValue(_:_:)'
framework: Swift
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/encodingerror/invalidvalue(_:_:)'
source_url: 'https://developer.apple.com/documentation/swift/encodingerror/invalidvalue(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/encodingerror/invalidvalue%28_%3A_%3A%29.json'
content_hash: 'sha256:92ac18bbd6e40f6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [EncodingError](../encodingerror.md)

# EncodingError.invalidValue(_:_:)

<sub>Case</sub>

An indication that an encoder or its containers could not encode the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case invalidValue(Any, EncodingError.Context)
```

## Discussion

As associated values, this case contains the attempted value and context for debugging.
