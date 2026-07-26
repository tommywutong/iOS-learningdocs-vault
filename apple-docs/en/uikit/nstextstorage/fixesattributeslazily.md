---
title: fixesAttributesLazily
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextstorage/fixesattributeslazily
source_url: 'https://developer.apple.com/documentation/uikit/nstextstorage/fixesattributeslazily'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextstorage/fixesattributeslazily.json'
content_hash: 'sha256:4a2b6c0b906638e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextStorage](../nstextstorage.md)

# fixesAttributesLazily

<sub>Instance Property</sub>

A Boolean value that indicates whether the text storage object fixes attributes lazily.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var fixesAttributesLazily: Bool { get }
```

## Discussion

When subclassing, the default value of this property is [false](../../swift/false.md), meaning that your subclass fixes attributes immediately when they change. The system’s concrete subclass overrides this property and sets it to [true](../../swift/true.md).

## See Also

### Fixing the string attributes

- [- invalidateAttributesInRange:](<invalidateattributes(in_).md>) — Invalidates attributes in the specified range.
- [- ensureAttributesAreFixedInRange:](<ensureattributesarefixed(in_).md>) — Ensures that attribute fixing occurs in the specified range.
