---
title: 'initWithDisplayName:identifier:extendedLanguageTag:mediaCharacteristics:'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [occ, occ, occ]
beta: true
deprecated: false
doc_path: '/documentation/avkit/avplaybackuserinterfacemediaselectionoption/initwithdisplayname:identifier:extendedlanguagetag:mediacharacteristics:'
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemediaselectionoption/initwithdisplayname:identifier:extendedlanguagetag:mediacharacteristics:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacemediaselectionoption/initwithdisplayname%3Aidentifier%3Aextendedlanguagetag%3Amediacharacteristics%3A.json'
content_hash: 'sha256:634889de902a2de9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfaceMediaSelectionOption](../avplaybackuserinterfacemediaselectionoption.md)

# initWithDisplayName:identifier:extendedLanguageTag:mediaCharacteristics:

<sub>Instance Method</sub>

Initializes a new media selection option with the specified attributes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```objc
- (instancetype) initWithDisplayName:(NSString *) displayName identifier:(NSString *) identifier extendedLanguageTag:(NSString *) extendedLanguageTag mediaCharacteristics:(NSArray<NSString *> *) mediaCharacteristics;
```

## Parameters

- `displayName` — Human-readable name displayed in user interfaces.

- `identifier` — Unique system identifier for programmatic selection.

- `extendedLanguageTag` — IETF BCP 47 language identifier, or `nil` for language-neutral content.

- `mediaCharacteristics` — The media characteristics describing accessibility features and content properties of this option.
