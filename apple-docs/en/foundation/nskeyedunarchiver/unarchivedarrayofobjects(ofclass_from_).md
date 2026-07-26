---
title: 'unarchivedArrayOfObjects(ofClass:from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyedunarchiver/unarchivedarrayofobjects(ofclass:from:)'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedunarchiver/unarchivedarrayofobjects(ofclass:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedunarchiver/unarchivedarrayofobjects%28ofclass%3Afrom%3A%29.json'
content_hash: 'sha256:d27ef9dabad994d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedUnarchiver](../nskeyedunarchiver.md)

# unarchivedArrayOfObjects(ofClass:from:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@nonobjc static func unarchivedArrayOfObjects<DecodedObject>(ofClass cls: DecodedObject.Type, from data: Data) throws -> [DecodedObject]? where DecodedObject : NSObject, DecodedObject : NSSecureCoding
```
