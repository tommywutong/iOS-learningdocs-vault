---
title: useUnicodeWordBoundaries
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsregularexpression/options-swift.struct/useunicodewordboundaries
source_url: 'https://developer.apple.com/documentation/foundation/nsregularexpression/options-swift.struct/useunicodewordboundaries'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsregularexpression/options-swift.struct/useunicodewordboundaries.json'
content_hash: 'sha256:7e07a25716b1798e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSRegularExpression](../../nsregularexpression.md) · [Options](../options-swift.struct.md)

# useUnicodeWordBoundaries

<sub>Type Property</sub>

Use Unicode `TR#29` to specify word boundaries (otherwise, traditional regular expression word boundaries are used).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var useUnicodeWordBoundaries: NSRegularExpression.Options { get }
```

## See Also

### Constants

- [NSRegularExpressionCaseInsensitive](caseinsensitive.md) — Match letters in the pattern independent of case.
- [NSRegularExpressionAllowCommentsAndWhitespace](allowcommentsandwhitespace.md) — Ignore whitespace and #-prefixed comments in the pattern.
- [NSRegularExpressionIgnoreMetacharacters](ignoremetacharacters.md) — Treat the entire pattern as a literal string.
- [NSRegularExpressionDotMatchesLineSeparators](dotmatcheslineseparators.md) — Allow `.` to match any character, including line separators.
- [NSRegularExpressionAnchorsMatchLines](anchorsmatchlines.md) — Allow `^` and `$` to match the start and end of lines.
- [NSRegularExpressionUseUnixLineSeparators](useunixlineseparators.md) — Treat only `\n` as a line separator (otherwise, all standard line separators are used).
