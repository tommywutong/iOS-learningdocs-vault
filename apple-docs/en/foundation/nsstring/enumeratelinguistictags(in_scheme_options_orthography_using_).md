---
title: 'enumerateLinguisticTags(in:scheme:options:orthography:using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsstring/enumeratelinguistictags(in:scheme:options:orthography:using:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/enumeratelinguistictags(in:scheme:options:orthography:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/enumeratelinguistictags%28in%3Ascheme%3Aoptions%3Aorthography%3Ausing%3A%29.json'
content_hash: 'sha256:361acdeb202ff1af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# enumerateLinguisticTags(in:scheme:options:orthography:using:)

<sub>Instance Method</sub>

Performs linguistic analysis on the specified string by enumerating the specific range of the string, providing the Block with the located tags.

> [!warning] Deprecated
> All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func enumerateLinguisticTags(in range: NSRange, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options = [], orthography: NSOrthography?, using block: (NSLinguisticTag?, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)
```

## Parameters

- `range` — The range of the string to analyze.

- `scheme` — The tag scheme to use. See Linguistic Tag Schemes for supported values.

- `options` — The linguistic tagger options to use. See [Options](../nslinguistictagger/options.md)for the constants. These constants can be combined using the C-Bitwise OR operator.

- `orthography` — The orthography of the string. If `nil`, the linguistic tagger will attempt to determine the orthography from the string content.

- `block` — The Block to apply to the string. The block takes four arguments: - **tag** — The tag scheme for the token. The opts parameter specifies the types of tagger options that are located. - **tokenRange** — The range of a string matching the tag scheme. - **sentenceRange** — The range of the sentence in which the token is found. - **stop** — A reference to a Boolean value. The block can set the value to [true](../../swift/true.md) to stop further processing of the array. The `stop` argument is an out-only argument. You should only ever set this Boolean to [true](../../swift/true.md) within the Block.

## Discussion

This is a convenience method.  It is the equivalent of creating an instance of `NSLinguisticTagger`, specifying the receiver as the string to be analyzed, and the orthography (or `nil`) and then invoking the [NSLinguisticTagger](../nslinguistictagger.md) method or [- enumerateTagsInRange:scheme:options:usingBlock:](<../nslinguistictagger/enumeratetags(in_scheme_options_using_).md>).

## See Also

### Performing Linguistic Analysis

- [- linguisticTagsInRange:scheme:options:orthography:tokenRanges:](<linguistictags(in_scheme_options_orthography_tokenranges_).md>) — Returns an array of linguistic tags for the specified range and requested tags within the receiving string. _(deprecated)_
- [EnumerationOptions](enumerationoptions.md) — Constants to specify kinds of substrings and styles of enumeration.
