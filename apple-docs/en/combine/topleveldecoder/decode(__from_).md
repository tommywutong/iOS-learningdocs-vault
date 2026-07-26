---
title: 'decode(_:from:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/topleveldecoder/decode(_:from:)'
source_url: 'https://developer.apple.com/documentation/combine/topleveldecoder/decode(_:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/topleveldecoder/decode%28_%3Afrom%3A%29.json'
content_hash: 'sha256:19906c7de05d4967'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [TopLevelDecoder](../topleveldecoder.md)

# decode(_:from:)

<sub>Instance Method</sub>

Decodes an instance of the indicated type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decode<T>(_ type: T.Type, from: Self.Input) throws -> T where T : Decodable
```
