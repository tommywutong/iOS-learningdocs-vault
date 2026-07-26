---
title: 'localeWithLocaleIdentifier:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nslocale/localewithlocaleidentifier:'
source_url: 'https://developer.apple.com/documentation/foundation/nslocale/localewithlocaleidentifier:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocale/localewithlocaleidentifier%3A.json'
content_hash: 'sha256:be0a7212f9e9245a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLocale](../nslocale.md)

# localeWithLocaleIdentifier:

<sub>Type Method</sub>

Returns a locale initialized using the given locale identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) localeWithLocaleIdentifier:(NSString *) ident;
```

## Parameters

- `ident` — The identifier for the new locale.

## Return Value

The initialized locale.

## See Also

### Initializing a Locale

- [- initWithLocaleIdentifier:](<init(localeidentifier_).md>) — Initializes a locale using a given locale identifier.
- [- initWithCoder:](<init(coder_).md>) — Returns a locale initialized from data in the given unarchiver.
