---
title: protocolVersions
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 17.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeysessionserverplaybackcontextoption/protocolversions
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysessionserverplaybackcontextoption/protocolversions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysessionserverplaybackcontextoption/protocolversions.json'
content_hash: 'sha256:6ea9496356536e0d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySessionServerPlaybackContextOption](../avcontentkeysessionserverplaybackcontextoption.md)

# protocolVersions

<sub>Type Property</sub>

Specifies the versions of the content protection protocols supported by the application.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let protocolVersions: AVContentKeySessionServerPlaybackContextOption
```

## Discussion

If you don’t specify a value for this key, the system assumes a default protocol version of `1`.

## See Also

### Server playback context options

- [AVContentKeySessionServerPlaybackContextOptionServerChallenge](serverchallenge.md) — Specifies a nonce to include in the secure server playback context (SPC) to prevent replay attacks.
