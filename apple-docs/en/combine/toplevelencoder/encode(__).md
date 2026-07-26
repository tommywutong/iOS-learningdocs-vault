---
title: 'encode(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/toplevelencoder/encode(_:)'
source_url: 'https://developer.apple.com/documentation/combine/toplevelencoder/encode(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/toplevelencoder/encode%28_%3A%29.json'
content_hash: 'sha256:d6ad95b862055f4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [TopLevelEncoder](../toplevelencoder.md)

# encode(_:)

<sub>Instance Method</sub>

Encodes an instance of the indicated type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func encode<T>(_ value: T) throws -> Self.Output where T : Encodable
```

## Parameters

- `value` — The instance to encode.
