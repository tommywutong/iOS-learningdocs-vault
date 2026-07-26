---
title: 'encode(to:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/ossignpostintervalstate/encode(to:)'
source_url: 'https://developer.apple.com/documentation/os/ossignpostintervalstate/encode(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignpostintervalstate/encode%28to%3A%29.json'
content_hash: 'sha256:77889492aad172c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSSignpostIntervalState](../ossignpostintervalstate.md)

# encode(to:)

<sub>Instance Method</sub>

Encodes the interval state into the provided encoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func encode(to encoder: any Encoder) throws
```

## Parameters

- `encoder` — The encoder to write data to.

## Discussion

> [!important] Important
> You don’t call this method directly. Instead, the object you’re using to encode the interval state, which must adopt the [Encoder](../../swift/encoder.md) protocol, calls it on your behalf as part of the serialization process.

The method throws an error if the interval state is invalid for the specified encoder’s format.
