---
title: 'init(displayName:identifier:language:mediaCharacteristics:)'
framework: AVKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/avkit/avplaybackuserinterfacemediaselectionoption/init(displayname:identifier:language:mediacharacteristics:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemediaselectionoption/init(displayname:identifier:language:mediacharacteristics:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacemediaselectionoption/init%28displayname%3Aidentifier%3Alanguage%3Amediacharacteristics%3A%29.json'
content_hash: 'sha256:7143323d40203c53'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfaceMediaSelectionOption](../avplaybackuserinterfacemediaselectionoption.md)

# init(displayName:identifier:language:mediaCharacteristics:)

<sub>Initializer</sub>

Creates a new media selection option.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
convenience init(displayName: String, identifier: String, language: Locale.Language? = nil, mediaCharacteristics: [AVMediaCharacteristic] = [])
```

## Parameters

- `displayName` — Human-readable name displayed in user interfaces.

- `identifier` — Unique system identifier for programmatic selection.

- `language` — The language of the media selection option, or `nil` for language-neutral content.

- `mediaCharacteristics` — The media characteristics describing accessibility features and content properties of this option.
