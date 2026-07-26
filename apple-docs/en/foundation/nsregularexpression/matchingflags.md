---
title: NSRegularExpression.MatchingFlags
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsregularexpression/matchingflags
source_url: 'https://developer.apple.com/documentation/foundation/nsregularexpression/matchingflags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsregularexpression/matchingflags.json'
content_hash: 'sha256:7e3b58d32a236e1a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSRegularExpression](../nsregularexpression.md)

# NSRegularExpression.MatchingFlags

<sub>Structure</sub>

Set by the Block as the matching progresses, completes, or fails. Used by the method [- enumerateMatchesInString:options:range:usingBlock:](<enumeratematches(in_options_range_using_).md>).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MatchingFlags
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [NSMatchingProgress](matchingflags/progress.md) — Set when the Block is called to report progress during a long-running match operation.
- [NSMatchingCompleted](matchingflags/completed.md) — Set when the Block is called after matching has completed.
- [NSMatchingHitEnd](matchingflags/hitend.md) — Set when the current match operation reached the end of the search range.
- [NSMatchingRequiredEnd](matchingflags/requiredend.md) — Set when the current match depended on the location of the end of the search range.
- [NSMatchingInternalError](matchingflags/internalerror.md) — Set when matching failed due to an internal error.

### Initializers

- [init(rawValue:)](<matchingflags/init(rawvalue_).md>)

## See Also

### Constants

- [Options](options-swift.struct.md) — These constants define the regular expression options. These constants are used by the property [options](options-swift.property.md), [regularExpressionWithPattern:options:error:](regularexpressionwithpattern_options_error_.md), and [- initWithPattern:options:error:](<init(pattern_options_).md>).
- [MatchingOptions](matchingoptions.md) — The matching options constants specify the reporting, completion and matching rules to the expression matching methods. These constants are used by all methods that search for, or replace values, using a regular expression.
