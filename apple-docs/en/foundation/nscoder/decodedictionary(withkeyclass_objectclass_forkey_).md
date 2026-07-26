---
title: 'decodeDictionary(withKeyClass:objectClass:forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/decodedictionary(withkeyclass:objectclass:forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/decodedictionary(withkeyclass:objectclass:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/decodedictionary%28withkeyclass%3Aobjectclass%3Aforkey%3A%29.json'
content_hash: 'sha256:6e9b9f8bf5e9c05a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# decodeDictionary(withKeyClass:objectClass:forKey:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@nonobjc func decodeDictionary<DecodedKey, DecodedObject>(withKeyClass keyClass: DecodedKey.Type, objectClass: DecodedObject.Type, forKey key: String) -> [DecodedKey : DecodedObject]? where DecodedKey : NSObject, DecodedKey : NSCopying, DecodedKey : NSSecureCoding, DecodedObject : NSObject, DecodedObject : NSSecureCoding
```
