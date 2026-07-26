---
title: variantPreferences
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, macOS 11.3+, tvOS 14.5+, visionOS 1.0+, watchOS 7.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/variantpreferences
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/variantpreferences'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/variantpreferences.json'
content_hash: 'sha256:ec1c5d55adb68c77'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# variantPreferences

<sub>Instance Property</sub>

The preferences the player item uses when selecting variant playlists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var variantPreferences: AVVariantPreferences { get set }
```

## Discussion

The default value is [AVVariantPreferenceNone](../avvariantpreferences/avvariantpreferencenone.md).

> [!note] Note
> Changing variant preferences during playback might result in a variant switch.

## See Also

### Setting variant behavior

- [AVVariantPreferences](../avvariantpreferences.md) — Defines the preferences the player item uses when selecting variant playlists.
- [startsOnFirstEligibleVariant](startsonfirsteligiblevariant.md) — A Boolean value that indicates whether playback starts with the first eligible variant that appears in the stream’s main playlist.
