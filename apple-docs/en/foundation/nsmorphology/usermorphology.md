---
title: userMorphology
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmorphology/usermorphology
source_url: 'https://developer.apple.com/documentation/foundation/nsmorphology/usermorphology'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmorphology/usermorphology.json'
content_hash: 'sha256:7a7942755dceeaa5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMorphology](../nsmorphology.md)

# userMorphology

<sub>Type Property</sub>

The addressing preferences of the current user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (class, readonly) NSMorphology * userMorphology;
```

## Discussion

If the user hasn’t specified preferences, or chose not to share them with this app, the [unspecified](unspecified.md) property is `true`.

This value doesn’t change throughout the lifetime of the process.
