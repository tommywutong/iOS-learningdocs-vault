---
title: 'tag(for:at:unit:scheme:orthography:tokenRange:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）, tvOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 4.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nslinguistictagger/tag(for:at:unit:scheme:orthography:tokenrange:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslinguistictagger/tag(for:at:unit:scheme:orthography:tokenrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslinguistictagger/tag%28for%3Aat%3Aunit%3Ascheme%3Aorthography%3Atokenrange%3A%29.json'
content_hash: 'sha256:de5717a656e3f16e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLinguisticTagger](../nslinguistictagger.md)

# tag(for:at:unit:scheme:orthography:tokenRange:)

<sub>Type Method</sub>

Returns a tag for a single scheme, for a given linguistic unit, at the specified character position in a string.

> [!warning] Deprecated
> All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func tag(for string: String, at charIndex: Int, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, orthography: NSOrthography?, tokenRange: NSRangePointer?) -> NSLinguisticTag?
```

## Parameters

- `string` — The position of the initial character.

- `charIndex` — The linguistic unit. See [NSLinguisticTaggerUnit](../nslinguistictaggerunit.md) for possible values.

- `unit` — The tag scheme. See [NSLinguisticTagScheme](../nslinguistictagscheme.md) for possible values.

- `scheme` — A pointer to the token range.

## Return Value

Returns the tag for the requested tag scheme and linguistic unit, or `nil`. If a tag is returned, this function returns by reference the range of the token to `tokenRange`.

## Discussion

This is a convenience method for initializing a linguistic tagger, setting the [string](string.md) property, and calling the [+ tagForString:atIndex:unit:scheme:orthography:tokenRange:](<tag(for_at_unit_scheme_orthography_tokenrange_).md>) method. If you analyze the same string more than once, you should create a linguistic tagger object instead of calling this method.

## See Also

### Getting Linguistic Tags

- [- tagAtIndex:unit:scheme:tokenRange:](<tag(at_unit_scheme_tokenrange_).md>) — Returns a tag for a single scheme, for a given linguistic unit, at the specified character position. _(deprecated)_
- [- tagAtIndex:scheme:tokenRange:sentenceRange:](<tag(at_scheme_tokenrange_sentencerange_).md>) — Returns a tag for a single scheme at the specified character position. _(deprecated)_
- [- tagsInRange:unit:scheme:options:tokenRanges:](<tags(in_unit_scheme_options_tokenranges_).md>) — Returns an array of linguistic tags and token ranges for a given string range and linguistic unit. _(deprecated)_
- [- tagsInRange:scheme:options:tokenRanges:](<tags(in_scheme_options_tokenranges_).md>) — Returns an array of linguistic tags and token ranges for a given string range. _(deprecated)_
- [+ tagsForString:range:unit:scheme:options:orthography:tokenRanges:](<tags(for_range_unit_scheme_options_orthography_tokenranges_).md>) — Returns an array of linguistic tags and token ranges for a given string and linguistic unit. _(deprecated)_
