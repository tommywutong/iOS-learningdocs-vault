---
title: AVVariantPreferences
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, macOS 11.3+, tvOS 14.5+, visionOS 1.0+, watchOS 7.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvariantpreferences
source_url: 'https://developer.apple.com/documentation/avfoundation/avvariantpreferences'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvariantpreferences.json'
content_hash: 'sha256:b30820a22cc9b318'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVVariantPreferences

<sub>Structure</sub>

Defines the preferences the player item uses when selecting variant playlists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AVVariantPreferences
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Preference settings

- [AVVariantPreferenceScalabilityToLosslessAudio](avvariantpreferences/scalabilitytolosslessaudio.md) — A preference that indicates the player item supports variant playlists that contain losslessly encoded audio when sufficient bandwidth is available.

### Initializers

- [init(rawValue:)](<avvariantpreferences/init(rawvalue_).md>) — Creates a variant preferences structure with an integer value.

## See Also

### Setting variant behavior

- [variantPreferences](avplayeritem/variantpreferences.md) — The preferences the player item uses when selecting variant playlists.
- [startsOnFirstEligibleVariant](avplayeritem/startsonfirsteligiblevariant.md) — A Boolean value that indicates whether playback starts with the first eligible variant that appears in the stream’s main playlist.
