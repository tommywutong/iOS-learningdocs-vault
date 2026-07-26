---
title: NSRegularExpression.MatchingOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsregularexpression/matchingoptions
source_url: 'https://developer.apple.com/documentation/foundation/nsregularexpression/matchingoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsregularexpression/matchingoptions.json'
content_hash: 'sha256:b37903125776c2d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSRegularExpression](../nsregularexpression.md)

# NSRegularExpression.MatchingOptions

<sub>Structure</sub>

The matching options constants specify the reporting, completion and matching rules to the expression matching methods. These constants are used by all methods that search for, or replace values, using a regular expression.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MatchingOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [NSMatchingReportProgress](matchingoptions/reportprogress.md) — Call the Block periodically during long-running match operations. This option has no effect for methods other than [- enumerateMatchesInString:options:range:usingBlock:](<enumeratematches(in_options_range_using_).md>). See [- enumerateMatchesInString:options:range:usingBlock:](<enumeratematches(in_options_range_using_).md>) for a description of the constant in context.
- [NSMatchingReportCompletion](matchingoptions/reportcompletion.md) — Call the Block once after the completion of any matching. This option has no effect for methods other than [- enumerateMatchesInString:options:range:usingBlock:](<enumeratematches(in_options_range_using_).md>). See [- enumerateMatchesInString:options:range:usingBlock:](<enumeratematches(in_options_range_using_).md>) for a description of the constant in context.
- [NSMatchingAnchored](matchingoptions/anchored.md) — Specifies that matches are limited to those at the start of the search range. See [- enumerateMatchesInString:options:range:usingBlock:](<enumeratematches(in_options_range_using_).md>) for a description of the constant in context.
- [NSMatchingWithTransparentBounds](matchingoptions/withtransparentbounds.md) — Specifies that matching may examine parts of the string beyond the bounds of the search range, for purposes such as word boundary detection, lookahead, etc. This constant has no effect if the search range contains the entire string. See [- enumerateMatchesInString:options:range:usingBlock:](<enumeratematches(in_options_range_using_).md>) for a description of the constant in context.
- [NSMatchingWithoutAnchoringBounds](matchingoptions/withoutanchoringbounds.md) — Specifies that `^` and `$` will not automatically match the beginning and end of the search range, but will still match the beginning and end of the entire string. This constant has no effect if the search range contains the entire string. See [- enumerateMatchesInString:options:range:usingBlock:](<enumeratematches(in_options_range_using_).md>) for a description of the constant in context.

### Initializers

- [init(rawValue:)](<matchingoptions/init(rawvalue_).md>)

## See Also

### Constants

- [Options](options-swift.struct.md) — These constants define the regular expression options. These constants are used by the property [options](options-swift.property.md), [regularExpressionWithPattern:options:error:](regularexpressionwithpattern_options_error_.md), and [- initWithPattern:options:error:](<init(pattern_options_).md>).
- [MatchingFlags](matchingflags.md) — Set by the Block as the matching progresses, completes, or fails. Used by the method [- enumerateMatchesInString:options:range:usingBlock:](<enumeratematches(in_options_range_using_).md>).
