---
title: 'paragraphRange(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/paragraphrange(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/paragraphrange(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/paragraphrange%28for%3A%29.json'
content_hash: 'sha256:fdf91f01749872be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# paragraphRange(for:)

<sub>Instance Method</sub>

Returns the range of characters representing the paragraph or paragraphs containing a given range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func paragraphRange(for range: NSRange) -> NSRange
```

## Parameters

- `range` — A range within the receiver. The range must not exceed the bounds of the receiver.

## Return Value

The range of characters representing the paragraph or paragraphs containing `aRange`, including the paragraph termination characters.

## Discussion

A paragraph is any segment of text delimited by a carriage return (`U+000D`), newline (`U+000A`), or paragraph separator (`U+2029`).

## See Also

### Determining Line and Paragraph Ranges

- [- getLineStart:end:contentsEnd:forRange:](<getlinestart(__end_contentsend_for_).md>) — Returns by reference the beginning of the first line and the end of the last line touched by the given range.
- [- lineRangeForRange:](<linerange(for_).md>) — Returns the range of characters representing the line or lines containing a given range.
- [- getParagraphStart:end:contentsEnd:forRange:](<getparagraphstart(__end_contentsend_for_).md>) — Returns by reference the beginning of the first paragraph and the end of the last paragraph touched by the given range.
