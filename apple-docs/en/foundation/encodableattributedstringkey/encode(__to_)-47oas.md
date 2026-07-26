---
title: 'encode(_:to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/encodableattributedstringkey/encode(_:to:)-47oas'
source_url: 'https://developer.apple.com/documentation/foundation/encodableattributedstringkey/encode(_:to:)-47oas'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/encodableattributedstringkey/encode%28_%3Ato%3A%29-47oas.json'
content_hash: 'sha256:04d24de411cee147'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [EncodableAttributedStringKey](../encodableattributedstringkey.md)

# encode(_:to:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func encode(_ value: Self.Value, to encoder: any Encoder) throws
```

## Parameters

- `value` — The value to encode.

- `encoder` — The encoder to write data to.

## Discussion

The default implementation calls down to the value’s [encode(to:)](<../../swift/encodable/encode(to_).md>) method.

This method throws an error if writing the encoder fails.
