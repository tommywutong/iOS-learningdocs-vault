---
title: default
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsubiquitouskeyvaluestore/default
source_url: 'https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsubiquitouskeyvaluestore/default.json'
content_hash: 'sha256:ae577aa7537f42ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUbiquitousKeyValueStore](../nsubiquitouskeyvaluestore.md)

# default

<sub>Type Property</sub>

The shared iCloud key-value store object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var `default`: NSUbiquitousKeyValueStore { get }
```

## Discussion

Use this object to access the shared iCloud key-value store tied to your app and the current person. You must use this object to get and set stored values.
