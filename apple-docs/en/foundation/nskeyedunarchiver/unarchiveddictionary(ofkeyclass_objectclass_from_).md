---
title: 'unarchivedDictionary(ofKeyClass:objectClass:from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyedunarchiver/unarchiveddictionary(ofkeyclass:objectclass:from:)'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedunarchiver/unarchiveddictionary(ofkeyclass:objectclass:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedunarchiver/unarchiveddictionary%28ofkeyclass%3Aobjectclass%3Afrom%3A%29.json'
content_hash: 'sha256:f59af772f6273a12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedUnarchiver](../nskeyedunarchiver.md)

# unarchivedDictionary(ofKeyClass:objectClass:from:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@nonobjc static func unarchivedDictionary<DecodedKey, DecodedObject>(ofKeyClass keyClass: DecodedKey.Type, objectClass: DecodedObject.Type, from data: Data) throws -> [DecodedKey : DecodedObject]? where DecodedKey : NSObject, DecodedKey : NSCopying, DecodedKey : NSSecureCoding, DecodedObject : NSObject, DecodedObject : NSSecureCoding
```
