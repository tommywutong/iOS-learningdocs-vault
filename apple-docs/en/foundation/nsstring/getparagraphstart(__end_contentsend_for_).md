---
title: 'getParagraphStart(_:end:contentsEnd:for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/getparagraphstart(_:end:contentsend:for:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/getparagraphstart(_:end:contentsend:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/getparagraphstart%28_%3Aend%3Acontentsend%3Afor%3A%29.json'
content_hash: 'sha256:6375875cfd5511bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# getParagraphStart(_:end:contentsEnd:for:)

<sub>Instance Method</sub>

Returns by reference the beginning of the first paragraph and the end of the last paragraph touched by the given range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getParagraphStart(_ startPtr: UnsafeMutablePointer<Int>?, end parEndPtr: UnsafeMutablePointer<Int>?, contentsEnd contentsEndPtr: UnsafeMutablePointer<Int>?, for range: NSRange)
```

## Parameters

- `startPtr` — Upon return, contains the index of the first character of the paragraph containing the beginning of `aRange`. Pass `NULL` if you do not need this value (in which case the work to compute the value isn’t performed).

- `parEndPtr` — Upon return, contains the index of the first character past the terminator of the paragraph containing the end of `aRange`. Pass `NULL` if you do not need this value (in which case the work to compute the value isn’t performed).

- `contentsEndPtr` — Upon return, contains the index of the first character of the terminator of the paragraph containing the end of `aRange`. Pass `NULL` if you do not need this value (in which case the work to compute the value isn’t performed).

- `range` — A range within the receiver. The value must not exceed the bounds of the receiver.

## Discussion

A paragraph is any segment of text delimited by a carriage return (`U+000D`), newline (`U+000A`), or paragraph separator (`U+2029`).

If `aRange` is contained with a single paragraph, of course, the returned indexes all belong to that paragraph. Similar to [- getLineStart:end:contentsEnd:forRange:](<getlinestart(__end_contentsend_for_).md>), you can use the results of this method to construct the ranges for paragraphs.

## See Also

### Determining Line and Paragraph Ranges

- [- getLineStart:end:contentsEnd:forRange:](<getlinestart(__end_contentsend_for_).md>) — Returns by reference the beginning of the first line and the end of the last line touched by the given range.
- [- lineRangeForRange:](<linerange(for_).md>) — Returns the range of characters representing the line or lines containing a given range.
- [- paragraphRangeForRange:](<paragraphrange(for_).md>) — Returns the range of characters representing the paragraph or paragraphs containing a given range.
