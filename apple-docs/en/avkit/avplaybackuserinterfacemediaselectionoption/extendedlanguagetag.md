---
title: extendedLanguageTag
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacemediaselectionoption/extendedlanguagetag
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemediaselectionoption/extendedlanguagetag'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacemediaselectionoption/extendedlanguagetag.json'
content_hash: 'sha256:d4e54e7620cf4594'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfaceMediaSelectionOption](../avplaybackuserinterfacemediaselectionoption.md)

# extendedLanguageTag

<sub>Instance Property</sub>

IETF BCP 47 language identifier (e.g., “en-US”, “es-419”, “zh-Hans-CN”) indicating the primary language and locale of this option. This standardized tag provides detailed language information including region, script, and variants. May be empty for language-neutral content such as music-only audio tracks, sound effects, or visual-only subtitles without spoken content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```objc
@property (nonatomic, copy, readonly, nullable) NSString * extendedLanguageTag;
```
