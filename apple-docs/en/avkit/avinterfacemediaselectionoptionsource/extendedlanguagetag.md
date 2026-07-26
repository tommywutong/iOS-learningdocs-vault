---
title: extendedLanguageTag
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avinterfacemediaselectionoptionsource/extendedlanguagetag
source_url: 'https://developer.apple.com/documentation/avkit/avinterfacemediaselectionoptionsource/extendedlanguagetag'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinterfacemediaselectionoptionsource/extendedlanguagetag.json'
content_hash: 'sha256:db6a9e195746e7f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVInterfaceMediaSelectionOptionSource](../avinterfacemediaselectionoptionsource.md)

# extendedLanguageTag

<sub>Instance Property</sub>

IETF BCP 47 language identifier (e.g., “en-US”, “es-419”, “zh-Hans-CN”) indicating the primary language and locale of this option. This standardized tag provides detailed language information including region, script, and variants. May be empty for language-neutral content such as music-only audio tracks, sound effects, or visual-only subtitles without spoken content.

<sub>tvOS, visionOS</sub>

```objc
@property (nonatomic, copy, readonly, nullable) NSString * extendedLanguageTag;
```
