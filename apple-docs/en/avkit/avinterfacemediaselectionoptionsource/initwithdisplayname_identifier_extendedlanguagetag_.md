---
title: 'initWithDisplayName:identifier:extendedLanguageTag:'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avinterfacemediaselectionoptionsource/initwithdisplayname:identifier:extendedlanguagetag:'
source_url: 'https://developer.apple.com/documentation/avkit/avinterfacemediaselectionoptionsource/initwithdisplayname:identifier:extendedlanguagetag:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinterfacemediaselectionoptionsource/initwithdisplayname%3Aidentifier%3Aextendedlanguagetag%3A.json'
content_hash: 'sha256:6de99bc40cda4b14'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVInterfaceMediaSelectionOptionSource](../avinterfacemediaselectionoptionsource.md)

# initWithDisplayName:identifier:extendedLanguageTag:

<sub>Instance Method</sub>

Initializes a new media selection option with the specified attributes.

<sub>tvOS, visionOS</sub>

```objc
- (instancetype) initWithDisplayName:(NSString *) displayName identifier:(NSString *) identifier extendedLanguageTag:(NSString *) extendedLanguageTag;
```

## Parameters

- `displayName` — Human-readable name displayed in user interfaces.

- `identifier` — Unique system identifier for programmatic selection.

- `extendedLanguageTag` — IETF BCP 47 language identifier, or nil for language-neutral content.
