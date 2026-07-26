---
title: AVVariantPreferenceNone
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, macOS 11.3+, tvOS 14.5+, visionOS 1.0+, watchOS 7.4+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvariantpreferences/avvariantpreferencenone
source_url: 'https://developer.apple.com/documentation/avfoundation/avvariantpreferences/avvariantpreferencenone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvariantpreferences/avvariantpreferencenone.json'
content_hash: 'sha256:72677e7518d3bbc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVariantPreferences](../avvariantpreferences.md)

# AVVariantPreferenceNone

<sub>Enumeration Case</sub>

Indicates that the player item uses the default behavior for determining variant playlist selection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
AVVariantPreferenceNone
```

## Discussion

By default, a player item bases variant selection on the available bandwidth, compatibility of the indicated codec or codecs, dimensions of the visual output, and number of available audio output channels.

## See Also

### Preference settings

- [AVVariantPreferenceScalabilityToLosslessAudio](scalabilitytolosslessaudio.md) — A preference that indicates the player item supports variant playlists that contain losslessly encoded audio when sufficient bandwidth is available.
