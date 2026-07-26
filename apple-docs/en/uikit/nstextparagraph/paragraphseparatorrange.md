---
title: paragraphSeparatorRange
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextparagraph/paragraphseparatorrange
source_url: 'https://developer.apple.com/documentation/uikit/nstextparagraph/paragraphseparatorrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextparagraph/paragraphseparatorrange.json'
content_hash: 'sha256:78ab943288b0050e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextParagraph](../nstextparagraph.md)

# paragraphSeparatorRange

<sub>Instance Property</sub>

Returns the range of the paragraph separator in the containing text’s attributed string.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var paragraphSeparatorRange: NSTextRange? { get }
```

## Discussion

The containing text is [NSTextContentStorage](../nstextcontentstorage.md)’s [attributedString](../nstextcontentstorage/attributedstring.md).

## See Also

### Getting paragraph characteristics

- [attributedString](attributedstring.md) — Returns the source attributed string.
- [paragraphContentRange](paragraphcontentrange.md) — Returns the range of the paragraph in the containing text’s attributed string.
