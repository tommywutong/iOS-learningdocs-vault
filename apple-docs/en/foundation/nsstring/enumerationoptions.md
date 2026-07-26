---
title: NSString.EnumerationOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsstring/enumerationoptions
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/enumerationoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/enumerationoptions.json'
content_hash: 'sha256:cd1b5238a210a9fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# NSString.EnumerationOptions

<sub>Structure</sub>

Constants to specify kinds of substrings and styles of enumeration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct EnumerationOptions
```

## Overview

These options are used with the [- enumerateSubstringsInRange:options:usingBlock:](<enumeratesubstrings(in_options_using_).md>) method. Pass in one `NSStringEnumerationBy...` option and combine with any of the remaining enumeration style constants using the C bitwise `OR` operator.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [NSStringEnumerationByLines](enumerationoptions/bylines.md)
- [NSStringEnumerationByParagraphs](enumerationoptions/byparagraphs.md)
- [NSStringEnumerationByComposedCharacterSequences](enumerationoptions/bycomposedcharactersequences.md)
- [NSStringEnumerationByWords](enumerationoptions/bywords.md)
- [NSStringEnumerationBySentences](enumerationoptions/bysentences.md)
- [NSStringEnumerationReverse](enumerationoptions/reverse.md)
- [NSStringEnumerationSubstringNotRequired](enumerationoptions/substringnotrequired.md)
- [NSStringEnumerationLocalized](enumerationoptions/localized.md)

### Initializers

- [init(_:)](<enumerationoptions/init(__).md>)
- [init(rawValue:)](<enumerationoptions/init(rawvalue_).md>)

### Instance Methods

- [contains(_:)](<enumerationoptions/contains(__).md>)
- [formIntersection(_:)](<enumerationoptions/formintersection(__).md>)
- [formSymmetricDifference(_:)](<enumerationoptions/formsymmetricdifference(__).md>)
- [formUnion(_:)](<enumerationoptions/formunion(__).md>)
- [insert(_:)](<enumerationoptions/insert(__).md>)
- [isSubset(of:)](<enumerationoptions/issubset(of_).md>)
- [remove(_:)](<enumerationoptions/remove(__).md>)

### Type Properties

- [NSStringEnumerationByCaretPositions](enumerationoptions/bycaretpositions.md)
- [NSStringEnumerationByDeletionClusters](enumerationoptions/bydeletionclusters.md)

## See Also

### Performing Linguistic Analysis

- [- enumerateLinguisticTagsInRange:scheme:options:orthography:usingBlock:](<enumeratelinguistictags(in_scheme_options_orthography_using_).md>) — Performs linguistic analysis on the specified string by enumerating the specific range of the string, providing the Block with the located tags. _(deprecated)_
- [- linguisticTagsInRange:scheme:options:orthography:tokenRanges:](<linguistictags(in_scheme_options_orthography_tokenranges_).md>) — Returns an array of linguistic tags for the specified range and requested tags within the receiving string. _(deprecated)_
