---
title: AVInterfaceMediaSelectionOptionSource
framework: AVKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avinterfacemediaselectionoptionsource
source_url: 'https://developer.apple.com/documentation/avkit/avinterfacemediaselectionoptionsource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinterfacemediaselectionoptionsource.json'
content_hash: 'sha256:ab470542073a1c2f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVInterfaceMediaSelectionOptionSource

<sub>Class</sub>

Represents a media selection option for audio tracks or subtitle tracks.

<sub>tvOS, visionOS</sub>

```objc
@interface AVInterfaceMediaSelectionOptionSource : NSObject
```

## Overview

This class represents individual media options (such as audio tracks or subtitle tracks) that can be selected by the user in media playback interfaces. Each option provides display information and metadata for user selection.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [NSCopying](../foundation/nscopying.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Inspecting the option source

- [displayName](avinterfacemediaselectionoptionsource/displayname.md) — Human-readable name for this media option displayed in user interfaces (e.g., “English”, “Spanish (Latin America)”, “Director’s Commentary”).
- [identifier](avinterfacemediaselectionoptionsource/identifier.md) — Unique system identifier for this media option, used for programmatic selection and persistence across sessions.

### Instance Properties

- [extendedLanguageTag](avinterfacemediaselectionoptionsource/extendedlanguagetag.md) — IETF BCP 47 language identifier (e.g., “en-US”, “es-419”, “zh-Hans-CN”) indicating the primary language and locale of this option. This standardized tag provides detailed language information including region, script, and variants. May be empty for language-neutral content such as music-only audio tracks, sound effects, or visual-only subtitles without spoken content.

### Instance Methods

- [initWithDisplayName:identifier:extendedLanguageTag:](avinterfacemediaselectionoptionsource/initwithdisplayname_identifier_extendedlanguagetag_.md) — Initializes a new media selection option with the specified attributes.
