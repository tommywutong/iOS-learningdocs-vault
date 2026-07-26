---
title: 'encode(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networkencoder/encode(_:)'
source_url: 'https://developer.apple.com/documentation/network/networkencoder/encode(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkencoder/encode%28_%3A%29.json'
content_hash: 'sha256:9f63007704f9b685'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkEncoder](../networkencoder.md)

# encode(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func encode<T>(_ value: T) throws -> Data where T : Encodable
```

## Parameters

- `value` — An encodable value to encode

## Return Value

Encoded data or throws an error if unable to encode
