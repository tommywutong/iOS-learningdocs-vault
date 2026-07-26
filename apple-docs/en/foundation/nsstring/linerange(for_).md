---
title: 'lineRange(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/linerange(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/linerange(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/linerange%28for%3A%29.json'
content_hash: 'sha256:2c199103b8ab19eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# lineRange(for:)

<sub>Instance Method</sub>

Returns the range of characters representing the line or lines containing a given range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func lineRange(for range: NSRange) -> NSRange
```

## Parameters

- `range` — A range within the receiver. The value must not exceed the bounds of the receiver.

## Return Value

The range of characters representing the line or lines containing `aRange`, including the line termination characters. See [- getLineStart:end:contentsEnd:forRange:](<getlinestart(__end_contentsend_for_).md>) for a discussion of line terminators.

## See Also

### Related Documentation

- [- substringWithRange:](<substring(with_).md>) — Returns a string object containing the characters of the receiver that lie within a given range.

### Determining Line and Paragraph Ranges

- [- getLineStart:end:contentsEnd:forRange:](<getlinestart(__end_contentsend_for_).md>) — Returns by reference the beginning of the first line and the end of the last line touched by the given range.
- [- getParagraphStart:end:contentsEnd:forRange:](<getparagraphstart(__end_contentsend_for_).md>) — Returns by reference the beginning of the first paragraph and the end of the last paragraph touched by the given range.
- [- paragraphRangeForRange:](<paragraphrange(for_).md>) — Returns the range of characters representing the paragraph or paragraphs containing a given range.
