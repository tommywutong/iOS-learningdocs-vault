---
title: tailIndent
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsparagraphstyle/tailindent
source_url: 'https://developer.apple.com/documentation/uikit/nsparagraphstyle/tailindent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsparagraphstyle/tailindent.json'
content_hash: 'sha256:e80ddd2b462caa9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSParagraphStyle](../nsparagraphstyle.md)

# tailIndent

<sub>Instance Property</sub>

The trailing indentation of the paragraph.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var tailIndent: CGFloat { get }
```

## Discussion

If positive, this value is the distance from the leading margin (for example, the left margin in left-to-right text). If `0` or negative, it’s the distance from the trailing margin.

For example, a paragraph style designed to fit exactly in a two-inch wide container has a head indent of `0.0` and a tail indent of `0.0`. One designed to fit with a quarter-inch margin has a head indent of `0.25` and a tail indent of `–0.25`.

## See Also

### Accessing style information

- [alignment](alignment.md) — The text alignment of the paragraph.
- [NSTextAlignment](../nstextalignment.md) — Constants that specify text alignment.
- [firstLineHeadIndent](firstlineheadindent.md) — The indentation of the first line of the paragraph.
- [headIndent](headindent.md) — The indentation of the paragraph’s lines other than the first.
- [lineHeightMultiple](lineheightmultiple.md) — The line height multiple.
- [maximumLineHeight](maximumlineheight.md) — The paragraph’s maximum line height.
- [minimumLineHeight](minimumlineheight.md) — The paragraph’s minimum line height.
- [lineSpacing](linespacing.md) — The distance in points between the bottom of one line fragment and the top of the next.
- [paragraphSpacing](paragraphspacing.md) — Distance between the bottom of this paragraph and top of next.
- [paragraphSpacingBefore](paragraphspacingbefore.md) — The distance between the paragraph’s top and the beginning of its text content.
