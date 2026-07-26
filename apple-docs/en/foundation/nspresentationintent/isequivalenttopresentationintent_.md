---
title: 'isEquivalentToPresentationIntent:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nspresentationintent/isequivalenttopresentationintent:'
source_url: 'https://developer.apple.com/documentation/foundation/nspresentationintent/isequivalenttopresentationintent:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspresentationintent/isequivalenttopresentationintent%3A.json'
content_hash: 'sha256:2284a8171ce5a259'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPresentationIntent](../nspresentationintent.md)

# isEquivalentToPresentationIntent:

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the current intent is equivalent to the specified intent.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (BOOL) isEquivalentToPresentationIntent:(NSPresentationIntent *) other;
```

## Parameters

- `other` — The other intent to use in the comparison.

## Return Value

[true](../../swift/true.md) if the current intent is equivalent to the specified intent, or [false](../../swift/false.md) if it isn’t.

## Discussion

Two intents are equivalent if their attributes match. This method doesn’t consider the [identity](identity.md) property of the intents when determining their equivalence.

## See Also

### Getting the intent identity

- [identity](identity.md) — A unique identifier for the intent in the document.
- [intentKind](intentkind.md) — The type of the intent.
- [parentIntent](parentintent.md) — The parent of the current intent.
