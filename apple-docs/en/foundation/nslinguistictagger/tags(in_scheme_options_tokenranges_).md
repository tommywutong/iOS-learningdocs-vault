---
title: 'tags(in:scheme:options:tokenRanges:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nslinguistictagger/tags(in:scheme:options:tokenranges:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslinguistictagger/tags(in:scheme:options:tokenranges:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslinguistictagger/tags%28in%3Ascheme%3Aoptions%3Atokenranges%3A%29.json'
content_hash: 'sha256:459818884da3af85'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLinguisticTagger](../nslinguistictagger.md)

# tags(in:scheme:options:tokenRanges:)

<sub>Instance Method</sub>

Returns an array of linguistic tags and token ranges for a given string range.

> [!warning] Deprecated
> All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func tags(in range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTagger.Options = [], tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [String]
```

## Parameters

- `range` — The range from which to return tags.

- `tagScheme` — The tag scheme. See [NSLinguisticTagScheme](../nslinguistictagscheme.md) for possible values.

- `opts` — The linguistic tagger options to use. See [Options](options.md) for possible values.

- `tokenRanges` — Returns by reference an array of token ranges.

## Return Value

An array of the tags in the requested range.

## Discussion

When the returned array contains an entry that doesn’t have a corresponding tag scheme, that entry is an empty string (`""`).

This is a convenience method for calling [- tagsInRange:unit:scheme:options:tokenRanges:](<tags(in_unit_scheme_options_tokenranges_).md>) and passing [NSLinguisticTaggerUnitWord](../nslinguistictaggerunit/word.md) as the linguistic unit.

## See Also

### Getting Linguistic Tags

- [- tagAtIndex:unit:scheme:tokenRange:](<tag(at_unit_scheme_tokenrange_).md>) — Returns a tag for a single scheme, for a given linguistic unit, at the specified character position. _(deprecated)_
- [- tagAtIndex:scheme:tokenRange:sentenceRange:](<tag(at_scheme_tokenrange_sentencerange_).md>) — Returns a tag for a single scheme at the specified character position. _(deprecated)_
- [+ tagForString:atIndex:unit:scheme:orthography:tokenRange:](<tag(for_at_unit_scheme_orthography_tokenrange_).md>) — Returns a tag for a single scheme, for a given linguistic unit, at the specified character position in a string. _(deprecated)_
- [- tagsInRange:unit:scheme:options:tokenRanges:](<tags(in_unit_scheme_options_tokenranges_).md>) — Returns an array of linguistic tags and token ranges for a given string range and linguistic unit. _(deprecated)_
- [+ tagsForString:range:unit:scheme:options:orthography:tokenRanges:](<tags(for_range_unit_scheme_options_orthography_tokenranges_).md>) — Returns an array of linguistic tags and token ranges for a given string and linguistic unit. _(deprecated)_
