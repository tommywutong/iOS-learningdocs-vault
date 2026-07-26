---
title: 'tags(for:range:unit:scheme:options:orthography:tokenRanges:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）, tvOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 4.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nslinguistictagger/tags(for:range:unit:scheme:options:orthography:tokenranges:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslinguistictagger/tags(for:range:unit:scheme:options:orthography:tokenranges:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslinguistictagger/tags%28for%3Arange%3Aunit%3Ascheme%3Aoptions%3Aorthography%3Atokenranges%3A%29.json'
content_hash: 'sha256:e5a0248ccd412a25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLinguisticTagger](../nslinguistictagger.md)

# tags(for:range:unit:scheme:options:orthography:tokenRanges:)

<sub>Type Method</sub>

Returns an array of linguistic tags and token ranges for a given string and linguistic unit.

> [!warning] Deprecated
> All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func tags(for string: String, range: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options = [], orthography: NSOrthography?, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [NSLinguisticTag]
```

## Parameters

- `string` — The range from which to return tags.

- `range` — The linguistic unit. See [NSLinguisticTaggerUnit](../nslinguistictaggerunit.md) for possible values.

- `unit` — The tag scheme. See [NSLinguisticTagScheme](../nslinguistictagscheme.md) for possible values.

- `scheme` — The linguistic tagger options to use. See [Options](options.md) for possible values.

- `options` — Returns by reference an array of token ranges.

## Return Value

An array of the tags in the requested range.

## Discussion

When the returned array contains an entry that doesn’t have a corresponding tag scheme, that entry is an empty string (`""`).

This is a convenience method for initializing a linguistic tagger, setting the [string](string.md) property, and calling the [- tagsInRange:unit:scheme:options:tokenRanges:](<tags(in_unit_scheme_options_tokenranges_).md>) method. If you analyze the same string more than once, you should create a linguistic tagger object instead of calling this method.

## See Also

### Getting Linguistic Tags

- [- tagAtIndex:unit:scheme:tokenRange:](<tag(at_unit_scheme_tokenrange_).md>) — Returns a tag for a single scheme, for a given linguistic unit, at the specified character position. _(deprecated)_
- [- tagAtIndex:scheme:tokenRange:sentenceRange:](<tag(at_scheme_tokenrange_sentencerange_).md>) — Returns a tag for a single scheme at the specified character position. _(deprecated)_
- [+ tagForString:atIndex:unit:scheme:orthography:tokenRange:](<tag(for_at_unit_scheme_orthography_tokenrange_).md>) — Returns a tag for a single scheme, for a given linguistic unit, at the specified character position in a string. _(deprecated)_
- [- tagsInRange:unit:scheme:options:tokenRanges:](<tags(in_unit_scheme_options_tokenranges_).md>) — Returns an array of linguistic tags and token ranges for a given string range and linguistic unit. _(deprecated)_
- [- tagsInRange:scheme:options:tokenRanges:](<tags(in_scheme_options_tokenranges_).md>) — Returns an array of linguistic tags and token ranges for a given string range. _(deprecated)_
