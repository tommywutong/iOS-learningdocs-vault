---
title: NSKeyedArchiveRootObjectKey
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nskeyedarchiverootobjectkey
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedarchiverootobjectkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedarchiverootobjectkey.json'
content_hash: 'sha256:8a38d493ee46c9b4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSKeyedArchiveRootObjectKey

<sub>Global Variable</sub>

Archives created using the class method [+ archivedDataWithRootObject:](<nskeyedarchiver/archiveddata(withrootobject_).md>) use this key for the root object in the hierarchy of encoded objects. The [NSKeyedUnarchiver](nskeyedunarchiver.md) class method [+ unarchiveObjectWithData:](<nskeyedunarchiver/unarchiveobject(with_).md>) looks for this root key as well.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSKeyedArchiveRootObjectKey: String
```
