---
title: 'decode(_:from:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/txtrecorddecoder/decode(_:from:)'
source_url: 'https://developer.apple.com/documentation/network/txtrecorddecoder/decode(_:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/txtrecorddecoder/decode%28_%3Afrom%3A%29.json'
content_hash: 'sha256:5915f347f64c2f18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [TXTRecordDecoder](../txtrecorddecoder.md)

# decode(_:from:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decode<T>(_ type: T.Type, from txtRecord: NWTXTRecord) throws -> T where T : Decodable
```
