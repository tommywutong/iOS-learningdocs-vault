---
title: tagSchemes
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nslinguistictagger/tagschemes
source_url: 'https://developer.apple.com/documentation/foundation/nslinguistictagger/tagschemes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslinguistictagger/tagschemes.json'
content_hash: 'sha256:37857c1edbbf9404'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLinguisticTagger](../nslinguistictagger.md)

# tagSchemes

<sub>Instance Property</sub>

Returns the tag schemes configured for this linguistic tagger. For possible values, see [NSLinguisticTagScheme](../nslinguistictagscheme.md).

> [!warning] Deprecated
> All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var tagSchemes: [NSLinguisticTagScheme] { get }
```

## See Also

### Getting the Tag Schemes

- [+ availableTagSchemesForUnit:language:](<availabletagschemes(for_language_).md>) — Returns the tag schemes available for a particular unit and language on the current device. _(deprecated)_
- [+ availableTagSchemesForLanguage:](<availabletagschemes(forlanguage_).md>) — Returns the tag schemes available for a particular language on the current device. _(deprecated)_
