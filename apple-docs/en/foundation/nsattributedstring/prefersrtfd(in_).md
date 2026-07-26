---
title: 'prefersRTFD(in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/prefersrtfd(in:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/prefersrtfd(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/prefersrtfd%28in%3A%29.json'
content_hash: 'sha256:cf0a0aa19592f7d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# prefersRTFD(in:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the specified range of text prefers RTFD formatting.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func prefersRTFD(in range: NSRange) -> Bool
```

## Parameters

- `range` — The range of text to test.

## Return Value

[true](../../swift/true.md) if the range of text prefers RTFD formatting, or [false](../../swift/false.md) if you can use the RTF format instead.

## Discussion

When an attributed string contains attachments, you must save it using the RTFD file format to preserve the attached files.

## See Also

### Getting the supported text-file formats

- [textTypes](texttypes.md) — An array of UTI strings that identify the file types that attributed strings support, either directly or through a user-installed filter service.
- [textUnfilteredTypes](textunfilteredtypes.md) — An array of UTI strings that identify the file types that attributed strings support directly.
