---
title: 'tag(at:scheme:tokenRange:sentenceRange:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nslinguistictagger/tag(at:scheme:tokenrange:sentencerange:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslinguistictagger/tag(at:scheme:tokenrange:sentencerange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslinguistictagger/tag%28at%3Ascheme%3Atokenrange%3Asentencerange%3A%29.json'
content_hash: 'sha256:4de3147191c3a5e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLinguisticTagger](../nslinguistictagger.md)

# tag(at:scheme:tokenRange:sentenceRange:)

<sub>Instance Method</sub>

Returns a tag for a single scheme at the specified character position.

> [!warning] Deprecated
> All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func tag(at charIndex: Int, scheme: NSLinguisticTagScheme, tokenRange: NSRangePointer?, sentenceRange: NSRangePointer?) -> NSLinguisticTag?
```

## Parameters

- `charIndex` — The position of the initial character.

- `scheme` — The tag scheme. See [NSLinguisticTagScheme](../nslinguistictagscheme.md) for the possible values.

- `tokenRange` — A pointer to the token range.

- `sentenceRange` — A pointer to the range of the sentence.

## Return Value

Returns the tag for the requested tag scheme, or `nil`. If a tag is returned, this function returns by reference the range of the token to `tokenRange`, and the range of the enclosing sentence to `sentenceRange`, if applicable.

## Discussion

This is a convenience method for calling [- tagAtIndex:unit:scheme:tokenRange:](<tag(at_unit_scheme_tokenrange_).md>) and passing [NSLinguisticTaggerUnitWord](../nslinguistictaggerunit/word.md) as the linguistic unit.

## See Also

### Getting Linguistic Tags

- [- tagAtIndex:unit:scheme:tokenRange:](<tag(at_unit_scheme_tokenrange_).md>) — Returns a tag for a single scheme, for a given linguistic unit, at the specified character position. _(deprecated)_
- [+ tagForString:atIndex:unit:scheme:orthography:tokenRange:](<tag(for_at_unit_scheme_orthography_tokenrange_).md>) — Returns a tag for a single scheme, for a given linguistic unit, at the specified character position in a string. _(deprecated)_
- [- tagsInRange:unit:scheme:options:tokenRanges:](<tags(in_unit_scheme_options_tokenranges_).md>) — Returns an array of linguistic tags and token ranges for a given string range and linguistic unit. _(deprecated)_
- [- tagsInRange:scheme:options:tokenRanges:](<tags(in_scheme_options_tokenranges_).md>) — Returns an array of linguistic tags and token ranges for a given string range. _(deprecated)_
- [+ tagsForString:range:unit:scheme:options:orthography:tokenRanges:](<tags(for_range_unit_scheme_options_orthography_tokenranges_).md>) — Returns an array of linguistic tags and token ranges for a given string and linguistic unit. _(deprecated)_
