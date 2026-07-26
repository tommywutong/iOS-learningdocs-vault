---
title: 'linguisticTags(in:scheme:options:orthography:tokenRanges:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsstring/linguistictags(in:scheme:options:orthography:tokenranges:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/linguistictags(in:scheme:options:orthography:tokenranges:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/linguistictags%28in%3Ascheme%3Aoptions%3Aorthography%3Atokenranges%3A%29.json'
content_hash: 'sha256:14393a1d9c817523'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# linguisticTags(in:scheme:options:orthography:tokenRanges:)

<sub>Instance Method</sub>

Returns an array of linguistic tags for the specified range and requested tags within the receiving string.

> [!warning] Deprecated
> All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func linguisticTags(in range: NSRange, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options = [], orthography: NSOrthography?, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [NSLinguisticTag]
```

## Parameters

- `range` — The range of the string to analyze.

- `scheme` — The tag scheme to use. See Linguistic Tag Schemes for supported values.

- `options` — The linguistic tagger options to use. See [Options](../nslinguistictagger/options.md) for the constants. These constants can be combined using the C-Bitwise OR operator.

- `orthography` — The orthography of the string. If `nil`, the linguistic tagger will attempt to determine the orthography from the string content.

- `tokenRanges` — An array returned by-reference containing the token ranges of the linguistic tags wrapped in `NSValue` objects.

## Return Value

Returns an array containing the linguistic tags for the `tokenRanges` within the receiving string.

## Discussion

This is a convenience method.  It is the equivalent of creating an instance of [NSLinguisticTagger](../nslinguistictagger.md), specifying the receiver as the string to be analyzed, and the orthography (or `nil`) and then invoking the [NSLinguisticTagger](../nslinguistictagger.md) method or [- linguisticTagsInRange:scheme:options:orthography:tokenRanges:](<linguistictags(in_scheme_options_orthography_tokenranges_).md>).

## See Also

### Performing Linguistic Analysis

- [- enumerateLinguisticTagsInRange:scheme:options:orthography:usingBlock:](<enumeratelinguistictags(in_scheme_options_orthography_using_).md>) — Performs linguistic analysis on the specified string by enumerating the specific range of the string, providing the Block with the located tags. _(deprecated)_
- [EnumerationOptions](enumerationoptions.md) — Constants to specify kinds of substrings and styles of enumeration.
