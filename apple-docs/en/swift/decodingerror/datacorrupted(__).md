---
title: 'DecodingError.dataCorrupted(_:)'
framework: Swift
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/decodingerror/datacorrupted(_:)'
source_url: 'https://developer.apple.com/documentation/swift/decodingerror/datacorrupted(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/decodingerror/datacorrupted%28_%3A%29.json'
content_hash: 'sha256:7325a57062579e89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [DecodingError](../decodingerror.md)

# DecodingError.dataCorrupted(_:)

<sub>Case</sub>

An indication that the data is corrupted or otherwise invalid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case dataCorrupted(DecodingError.Context)
```

## Discussion

As an associated value, this case contains the context for debugging.
