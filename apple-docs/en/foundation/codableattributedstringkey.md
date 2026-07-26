---
title: CodableAttributedStringKey
framework: Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/codableattributedstringkey
source_url: 'https://developer.apple.com/documentation/foundation/codableattributedstringkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/codableattributedstringkey.json'
content_hash: 'sha256:5acccb640e3557b2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# CodableAttributedStringKey

<sub>Type Alias</sub>

A type alias used by attribute keys that are both encodable and decodable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CodableAttributedStringKey = DecodableAttributedStringKey & EncodableAttributedStringKey
```

## See Also

### Encoding and Decoding Keys

- [DecodableAttributedStringKey](decodableattributedstringkey.md) — A protocol that defines how an attribute key decodes its value.
- [EncodableAttributedStringKey](encodableattributedstringkey.md) — A protocol that defines how an attribute key encodes its value.
