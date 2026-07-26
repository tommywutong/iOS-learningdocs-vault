---
title: identity
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspresentationintent/identity
source_url: 'https://developer.apple.com/documentation/foundation/nspresentationintent/identity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspresentationintent/identity.json'
content_hash: 'sha256:4a6676ebe343693a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPresentationIntent](../nspresentationintent.md)

# identity

<sub>Instance Property</sub>

A unique identifier for the intent in the document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (readonly) NSInteger identity;
```

## Discussion

Use the value in this property to disambiguate attributes that apply to contiguous text. For example, you might use it to differentiate between two headers in a row with the same level.

## See Also

### Getting the intent identity

- [intentKind](intentkind.md) — The type of the intent.
- [parentIntent](parentintent.md) — The parent of the current intent.
- [isEquivalentToPresentationIntent:](isequivalenttopresentationintent_.md) — Returns a Boolean value that indicates whether the current intent is equivalent to the specified intent.
