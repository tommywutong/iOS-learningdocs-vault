---
title: CFStringCompareFlags
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstringcompareflags
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringcompareflags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringcompareflags.json'
content_hash: 'sha256:12819ea520b92749'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringCompareFlags

<sub>Structure</sub>

A [CFOptionFlags](cfoptionflags.md) type for specifying options for string comparison .

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFStringCompareFlags
```

## Overview

See [String Comparison Flags](string-comparison-flags.md) for values.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<cfstringcompareflags/init(rawvalue_).md>)

### Type Properties

- [kCFCompareAnchored](cfstringcompareflags/compareanchored.md) — Performs searching only on characters at the beginning or end of the range.
- [kCFCompareBackwards](cfstringcompareflags/comparebackwards.md) — Specifies that the comparison should start at the last elements of the entities being compared (for example, strings or arrays).
- [kCFCompareCaseInsensitive](cfstringcompareflags/comparecaseinsensitive.md) — Specifies that the comparison should ignore differences in case between alphabetical characters.
- [kCFCompareDiacriticInsensitive](cfstringcompareflags/comparediacriticinsensitive.md) — Specifies that the comparison should ignore diacritic markers.
- [kCFCompareForcedOrdering](cfstringcompareflags/compareforcedordering.md) — Specifies that the comparison is forced to return either `kCFCompareLessThan` or `kCFCompareGreaterThan` if the strings are equivalent but not strictly equal.
- [kCFCompareLocalized](cfstringcompareflags/comparelocalized.md) — Specifies that the comparison should take into account differences related to locale, such as the thousands separator character.
- [kCFCompareNonliteral](cfstringcompareflags/comparenonliteral.md) — Specifies that loose equivalence is acceptable, especially as pertains to diacritical marks.
- [kCFCompareNumerically](cfstringcompareflags/comparenumerically.md) — Specifies that represented numeric values should be used as the basis for comparison and not the actual character values.
- [kCFCompareWidthInsensitive](cfstringcompareflags/comparewidthinsensitive.md) — Specifies that the comparison should ignore width differences.

## See Also

### Data Types

- [CFStringEncoding](cfstringencoding.md) — An integer type for constants used to specify supported string encodings in various CFString functions.
- [CFStringEncodings](cfstringencodings.md) — Index type for constants used to specify external string encodings.
- [CFStringInlineBuffer](cfstringinlinebuffer.md) — Defines the buffer and related fields used for in-line buffer access of characters in CFString objects.
