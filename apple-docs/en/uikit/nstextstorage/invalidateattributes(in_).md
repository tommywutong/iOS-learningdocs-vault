---
title: 'invalidateAttributes(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextstorage/invalidateattributes(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextstorage/invalidateattributes(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextstorage/invalidateattributes%28in%3A%29.json'
content_hash: 'sha256:841994ba43753797'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextStorage](../nstextstorage.md)

# invalidateAttributes(in:)

<sub>Instance Method</sub>

Invalidates attributes in the specified range.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func invalidateAttributes(in range: NSRange)
```

## Parameters

- `range` — The range of characters whose attributes the method should invalidate.

## Discussion

Called from [- processEditing](<processediting().md>) to invalidate attributes when the text storage changes. If the receiver isn’t lazy, this method calls [fixAttributes(in:)](<../../foundation/nsmutableattributedstring/fixattributes(in_).md>). If lazy attribute fixing is in effect, this method instead records the range needing fixing.

## See Also

### Fixing the string attributes

- [- ensureAttributesAreFixedInRange:](<ensureattributesarefixed(in_).md>) — Ensures that attribute fixing occurs in the specified range.
- [fixesAttributesLazily](fixesattributeslazily.md) — A Boolean value that indicates whether the text storage object fixes attributes lazily.
