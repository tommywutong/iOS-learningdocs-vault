---
title: reportProgress
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsregularexpression/matchingoptions/reportprogress
source_url: 'https://developer.apple.com/documentation/foundation/nsregularexpression/matchingoptions/reportprogress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsregularexpression/matchingoptions/reportprogress.json'
content_hash: 'sha256:e2bd86b28f5578bd'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSRegularExpression](../../nsregularexpression.md) · [MatchingOptions](../matchingoptions.md)

# reportProgress

<sub>Type Property</sub>

Call the Block periodically during long-running match operations. This option has no effect for methods other than [- enumerateMatchesInString:options:range:usingBlock:](<../enumeratematches(in_options_range_using_).md>). See [- enumerateMatchesInString:options:range:usingBlock:](<../enumeratematches(in_options_range_using_).md>) for a description of the constant in context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var reportProgress: NSRegularExpression.MatchingOptions { get }
```

## See Also

### Constants

- [NSMatchingReportCompletion](reportcompletion.md) — Call the Block once after the completion of any matching. This option has no effect for methods other than [- enumerateMatchesInString:options:range:usingBlock:](<../enumeratematches(in_options_range_using_).md>). See [- enumerateMatchesInString:options:range:usingBlock:](<../enumeratematches(in_options_range_using_).md>) for a description of the constant in context.
- [NSMatchingAnchored](anchored.md) — Specifies that matches are limited to those at the start of the search range. See [- enumerateMatchesInString:options:range:usingBlock:](<../enumeratematches(in_options_range_using_).md>) for a description of the constant in context.
- [NSMatchingWithTransparentBounds](withtransparentbounds.md) — Specifies that matching may examine parts of the string beyond the bounds of the search range, for purposes such as word boundary detection, lookahead, etc. This constant has no effect if the search range contains the entire string. See [- enumerateMatchesInString:options:range:usingBlock:](<../enumeratematches(in_options_range_using_).md>) for a description of the constant in context.
- [NSMatchingWithoutAnchoringBounds](withoutanchoringbounds.md) — Specifies that `^` and `$` will not automatically match the beginning and end of the search range, but will still match the beginning and end of the entire string. This constant has no effect if the search range contains the entire string. See [- enumerateMatchesInString:options:range:usingBlock:](<../enumeratematches(in_options_range_using_).md>) for a description of the constant in context.
