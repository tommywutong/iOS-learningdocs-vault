---
title: 'decodeArrayOfObjects(ofClass:forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/decodearrayofobjects(ofclass:forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/decodearrayofobjects(ofclass:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/decodearrayofobjects%28ofclass%3Aforkey%3A%29.json'
content_hash: 'sha256:4b799210664ef3b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# decodeArrayOfObjects(ofClass:forKey:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@nonobjc func decodeArrayOfObjects<DecodedObject>(ofClass cls: DecodedObject.Type, forKey key: String) -> [DecodedObject]? where DecodedObject : NSObject, DecodedObject : NSSecureCoding
```
