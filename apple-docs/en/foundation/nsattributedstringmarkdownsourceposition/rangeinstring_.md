---
title: 'rangeInString:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstringmarkdownsourceposition/rangeinstring:'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstringmarkdownsourceposition/rangeinstring:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstringmarkdownsourceposition/rangeinstring%3A.json'
content_hash: 'sha256:c37af67e7291338f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedStringMarkdownSourcePosition](../nsattributedstringmarkdownsourceposition.md)

# rangeInString:

<sub>Instance Method</sub>

Returns a range indicating the source portion within a Markdown string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (NSRange) rangeInString:(NSString *) string;
```

## Parameters

- `string` — The Markdown source string that this source position object refers to.

## Return Value

A range that represents the source portion within a source Markdown string.

## Discussion

Use this method to access the marked-up region of `string` with an NSRange, rather than making manual calculations based on row and column values.
