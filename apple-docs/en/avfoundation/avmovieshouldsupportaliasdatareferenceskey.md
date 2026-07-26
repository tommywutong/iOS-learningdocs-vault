---
title: AVMovieShouldSupportAliasDataReferencesKey
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.12+, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avmovieshouldsupportaliasdatareferenceskey
source_url: 'https://developer.apple.com/documentation/avfoundation/avmovieshouldsupportaliasdatareferenceskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmovieshouldsupportaliasdatareferenceskey.json'
content_hash: 'sha256:90a33a79def63825'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMovieShouldSupportAliasDataReferencesKey

<sub>Global Variable</sub>

A key that specifies a Boolean value that indicates whether the system parses and resolves alias data references in the movie.

> [!warning] Deprecated
> AVMovieShouldSupportAliasDataReferencesKey is not supported on this platform

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
let AVMovieShouldSupportAliasDataReferencesKey: String
```

## Discussion

The default value is [false](../swift/false.md). Most QuickTime movie files contain all of the media data they require, but some contain references to media stored in other files. While AVFoundation and CoreMedia typically use a URL reference for this purpose, older implementations such as QuickTime 7 have commonly used a Macintosh alias instead, as documented in the QuickTime File Format specification. If your app must work with legacy QuickTime movie files containing alias-based references to media data stored in other files, set this value to [true](../swift/true.md).

If you provide a value for [AVMovieReferenceRestrictionsKey](avmoviereferencerestrictionskey.md), the movie observes these restrictions for resolved alias references just as they’re for URL references.

## See Also

### Options

- [AVMovieReferenceRestrictionsKey](avmoviereferencerestrictionskey.md) — A key that specifies restrictions for a movie to use when it resolves references to external media data.
