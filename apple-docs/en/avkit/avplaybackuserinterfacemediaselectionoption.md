---
title: AVPlaybackUserInterfaceMediaSelectionOption
framework: AVKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift, occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacemediaselectionoption
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemediaselectionoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacemediaselectionoption.json'
content_hash: 'sha256:329551e67427c686'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlaybackUserInterfaceMediaSelectionOption

<sub>Class</sub>

Represents a media selection option for audio tracks or subtitle tracks.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class AVPlaybackUserInterfaceMediaSelectionOption
```

## Overview

This class represents individual media options (such as audio tracks or subtitle tracks) that can be selected by the user in media playback interfaces. Each option provides display information and metadata for user selection.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(coder:)](<avplaybackuserinterfacemediaselectionoption/init(coder_).md>) _(beta)_
- [init(displayName:identifier:language:mediaCharacteristics:)](<avplaybackuserinterfacemediaselectionoption/init(displayname_identifier_language_mediacharacteristics_).md>) — Creates a new media selection option. _(beta)_

### Instance Properties

- [displayName](avplaybackuserinterfacemediaselectionoption/displayname.md) — Human-readable name for this media option displayed in user interfaces (e.g., “English”, “Spanish (Latin America)”, “Director’s Commentary”). _(beta)_
- [identifier](avplaybackuserinterfacemediaselectionoption/identifier.md) — Unique system identifier for this media option, used for programmatic selection and persistence across sessions. _(beta)_
- [language](avplaybackuserinterfacemediaselectionoption/language.md) — The language of this media selection option. _(beta)_
- [mediaCharacteristics](avplaybackuserinterfacemediaselectionoption/mediacharacteristics.md) — The media characteristics describing accessibility features and content properties of this option. Common values include `AVMediaCharacteristicContainsOnlyForcedSubtitles`, `AVMediaCharacteristicTranscribesSpokenDialogForAccessibility`, and `AVMediaCharacteristicDescribesMusicAndSoundForAccessibility`. May be empty if no characteristics apply. _(beta)_

## See Also

### Media selection

- [AVPlaybackUserInterfaceMediaSelectionControllable](avplaybackuserinterfacemediaselectioncontrollable-8ee5z.md) — Provides audio and subtitle selection capabilities for media content. _(beta)_
