---
title: 'encode(to:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/subscribers/demand/encode(to:)'
source_url: 'https://developer.apple.com/documentation/combine/subscribers/demand/encode(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subscribers/demand/encode%28to%3A%29.json'
content_hash: 'sha256:64138a56d259ab2a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Subscribers](../../subscribers.md) · [Demand](../demand.md)

# encode(to:)

<sub>Instance Method</sub>

Encodes the demand to the provide encoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func encode(to encoder: any Encoder) throws
```

## Parameters

- `encoder` — An encoder instance.

## See Also

### Encoding and decoding

- [init(from:)](<init(from_).md>) — Creates a demand instance from a decoder.
