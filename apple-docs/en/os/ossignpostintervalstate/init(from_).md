---
title: 'init(from:)'
framework: os
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/ossignpostintervalstate/init(from:)'
source_url: 'https://developer.apple.com/documentation/os/ossignpostintervalstate/init(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignpostintervalstate/init%28from%3A%29.json'
content_hash: 'sha256:5034d53c08623bae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSSignpostIntervalState](../ossignpostintervalstate.md)

# init(from:)

<sub>Initializer</sub>

Decodes the interval state from the provided decoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
required init(from decoder: any Decoder) throws
```

## Parameters

- `decoder` — The decoder to read data from.

## Discussion

> [!important] Important
> You don’t call this method directly. Instead, the object you’re using to decode the interval state, which must adopt the [Decoder](../../swift/decoder.md) protocol, calls it on your behalf as part of the serialization process.

The initializer throws an error if reading from the decoder fails, or if the decoder’s data is corrupt or invalid.
