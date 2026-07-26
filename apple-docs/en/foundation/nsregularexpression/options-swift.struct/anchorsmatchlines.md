---
title: anchorsMatchLines
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsregularexpression/options-swift.struct/anchorsmatchlines
source_url: 'https://developer.apple.com/documentation/foundation/nsregularexpression/options-swift.struct/anchorsmatchlines'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsregularexpression/options-swift.struct/anchorsmatchlines.json'
content_hash: 'sha256:327b9d082eabeb62'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSRegularExpression](../../nsregularexpression.md) · [Options](../options-swift.struct.md)

# anchorsMatchLines

<sub>Type Property</sub>

Allow `^` and `$` to match the start and end of lines.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var anchorsMatchLines: NSRegularExpression.Options { get }
```

## See Also

### Constants

- [NSRegularExpressionCaseInsensitive](caseinsensitive.md) — Match letters in the pattern independent of case.
- [NSRegularExpressionAllowCommentsAndWhitespace](allowcommentsandwhitespace.md) — Ignore whitespace and #-prefixed comments in the pattern.
- [NSRegularExpressionIgnoreMetacharacters](ignoremetacharacters.md) — Treat the entire pattern as a literal string.
- [NSRegularExpressionDotMatchesLineSeparators](dotmatcheslineseparators.md) — Allow `.` to match any character, including line separators.
- [NSRegularExpressionUseUnixLineSeparators](useunixlineseparators.md) — Treat only `\n` as a line separator (otherwise, all standard line separators are used).
- [NSRegularExpressionUseUnicodeWordBoundaries](useunicodewordboundaries.md) — Use Unicode `TR#29` to specify word boundaries (otherwise, traditional regular expression word boundaries are used).
