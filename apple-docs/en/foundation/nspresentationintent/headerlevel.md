---
title: headerLevel
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspresentationintent/headerlevel
source_url: 'https://developer.apple.com/documentation/foundation/nspresentationintent/headerlevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspresentationintent/headerlevel.json'
content_hash: 'sha256:ef61d7c82eb66893'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPresentationIntent](../nspresentationintent.md)

# headerLevel

<sub>Instance Property</sub>

The level of a header section.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (readonly) NSInteger headerLevel;
```

## Discussion

This value corresponds to the number of hash marks (`#`) associated with the header. If the intent is not a header, the value of this property is `0`.
