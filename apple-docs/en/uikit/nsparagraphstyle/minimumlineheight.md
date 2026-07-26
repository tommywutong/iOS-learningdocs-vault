---
title: minimumLineHeight
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsparagraphstyle/minimumlineheight
source_url: 'https://developer.apple.com/documentation/uikit/nsparagraphstyle/minimumlineheight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsparagraphstyle/minimumlineheight.json'
content_hash: 'sha256:3029e853ba8de7af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSParagraphStyle](../nsparagraphstyle.md)

# minimumLineHeight

<sub>Instance Property</sub>

The paragraph’s minimum line height.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var minimumLineHeight: CGFloat { get }
```

## Discussion

This property contains the minimum height in points that any line in the receiver occupies, regardless of the font size or size of any attached graphic. This value is always nonnegative.

## See Also

### Accessing style information

- [alignment](alignment.md) — The text alignment of the paragraph.
- [NSTextAlignment](../nstextalignment.md) — Constants that specify text alignment.
- [firstLineHeadIndent](firstlineheadindent.md) — The indentation of the first line of the paragraph.
- [headIndent](headindent.md) — The indentation of the paragraph’s lines other than the first.
- [tailIndent](tailindent.md) — The trailing indentation of the paragraph.
- [lineHeightMultiple](lineheightmultiple.md) — The line height multiple.
- [maximumLineHeight](maximumlineheight.md) — The paragraph’s maximum line height.
- [lineSpacing](linespacing.md) — The distance in points between the bottom of one line fragment and the top of the next.
- [paragraphSpacing](paragraphspacing.md) — Distance between the bottom of this paragraph and top of next.
- [paragraphSpacingBefore](paragraphspacingbefore.md) — The distance between the paragraph’s top and the beginning of its text content.
