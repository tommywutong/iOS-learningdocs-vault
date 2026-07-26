---
title: 'ensureAttributesAreFixed(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextstorage/ensureattributesarefixed(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextstorage/ensureattributesarefixed(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextstorage/ensureattributesarefixed%28in%3A%29.json'
content_hash: 'sha256:0b17a13c144a6fb2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextStorage](../nstextstorage.md)

# ensureAttributesAreFixed(in:)

<sub>Instance Method</sub>

Ensures that attribute fixing occurs in the specified range.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func ensureAttributesAreFixed(in range: NSRange)
```

## Parameters

- `range` — The range of characters to examine.

## Discussion

An `NSTextStorage` object using lazy attribute fixing is required to call this method before accessing any attributes within `range`. This method gives attribute fixing a chance to occur if necessary. `NSTextStorage` subclasses wishing to support laziness must call this method from all attribute accessors they implement.

## See Also

### Fixing the string attributes

- [- invalidateAttributesInRange:](<invalidateattributes(in_).md>) — Invalidates attributes in the specified range.
- [fixesAttributesLazily](fixesattributeslazily.md) — A Boolean value that indicates whether the text storage object fixes attributes lazily.
