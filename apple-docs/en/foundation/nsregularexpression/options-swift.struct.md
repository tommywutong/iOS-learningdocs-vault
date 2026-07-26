---
title: NSRegularExpression.Options
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsregularexpression/options-swift.struct
source_url: 'https://developer.apple.com/documentation/foundation/nsregularexpression/options-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsregularexpression/options-swift.struct.json'
content_hash: 'sha256:fe93505df75b699b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSRegularExpression](../nsregularexpression.md)

# NSRegularExpression.Options

<sub>Structure</sub>

These constants define the regular expression options. These constants are used by the property [options](options-swift.property.md), [regularExpressionWithPattern:options:error:](regularexpressionwithpattern_options_error_.md), and [- initWithPattern:options:error:](<init(pattern_options_).md>).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Options
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [NSRegularExpressionCaseInsensitive](options-swift.struct/caseinsensitive.md) — Match letters in the pattern independent of case.
- [NSRegularExpressionAllowCommentsAndWhitespace](options-swift.struct/allowcommentsandwhitespace.md) — Ignore whitespace and #-prefixed comments in the pattern.
- [NSRegularExpressionIgnoreMetacharacters](options-swift.struct/ignoremetacharacters.md) — Treat the entire pattern as a literal string.
- [NSRegularExpressionDotMatchesLineSeparators](options-swift.struct/dotmatcheslineseparators.md) — Allow `.` to match any character, including line separators.
- [NSRegularExpressionAnchorsMatchLines](options-swift.struct/anchorsmatchlines.md) — Allow `^` and `$` to match the start and end of lines.
- [NSRegularExpressionUseUnixLineSeparators](options-swift.struct/useunixlineseparators.md) — Treat only `\n` as a line separator (otherwise, all standard line separators are used).
- [NSRegularExpressionUseUnicodeWordBoundaries](options-swift.struct/useunicodewordboundaries.md) — Use Unicode `TR#29` to specify word boundaries (otherwise, traditional regular expression word boundaries are used).

### Initializers

- [init(rawValue:)](<options-swift.struct/init(rawvalue_).md>)

## See Also

### Constants

- [MatchingFlags](matchingflags.md) — Set by the Block as the matching progresses, completes, or fails. Used by the method [- enumerateMatchesInString:options:range:usingBlock:](<enumeratematches(in_options_range_using_).md>).
- [MatchingOptions](matchingoptions.md) — The matching options constants specify the reporting, completion and matching rules to the expression matching methods. These constants are used by all methods that search for, or replace values, using a regular expression.
