---
title: paragraphSpacing
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsmutableparagraphstyle/paragraphspacing
source_url: 'https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/paragraphspacing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsmutableparagraphstyle/paragraphspacing.json'
content_hash: 'sha256:64cfb034e1f37313'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSMutableParagraphStyle](../nsmutableparagraphstyle.md)

# paragraphSpacing

<sub>Instance Property</sub>

The space after the end of the paragraph.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var paragraphSpacing: CGFloat { get set }
```

## Discussion

This property contains the space (measured in points) added at the end of the paragraph to separate it from the following paragraph. This value must be nonnegative. The space between paragraphs is determined by adding the previous paragraph’s `paragraphSpacing` and the current paragraph’s [paragraphSpacingBefore](paragraphspacingbefore.md).

## See Also

### Setting style information

- [- setParagraphStyle:](<setparagraphstyle(__).md>) — Replaces the subattributes of the paragraph with those in the specified paragraph style object.
- [alignment](alignment.md) — The text alignment of the paragraph.
- [firstLineHeadIndent](firstlineheadindent.md) — The indentation of the first line of the paragraph.
- [headIndent](headindent.md) — The indentation of the paragraph’s lines other than the first.
- [tailIndent](tailindent.md) — The trailing indentation of the paragraph.
- [lineHeightMultiple](lineheightmultiple.md) — The line height multiple.
- [maximumLineHeight](maximumlineheight.md) — The paragraph’s maximum line height.
- [minimumLineHeight](minimumlineheight.md) — The paragraph’s minimum line height.
- [lineSpacing](linespacing.md) — The distance in points between the bottom of one line fragment and the top of the next.
- [paragraphSpacingBefore](paragraphspacingbefore.md) — The distance between the paragraph’s top and the beginning of its text content.
- [baseWritingDirection](basewritingdirection.md) — The base writing direction for the paragraph.
