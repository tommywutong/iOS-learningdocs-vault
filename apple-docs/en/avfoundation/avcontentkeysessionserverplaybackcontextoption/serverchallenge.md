---
title: serverChallenge
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 17.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeysessionserverplaybackcontextoption/serverchallenge
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysessionserverplaybackcontextoption/serverchallenge'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysessionserverplaybackcontextoption/serverchallenge.json'
content_hash: 'sha256:f7bfab1d85ddb046'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySessionServerPlaybackContextOption](../avcontentkeysessionserverplaybackcontextoption.md)

# serverChallenge

<sub>Type Property</sub>

Specifies a nonce to include in the secure server playback context (SPC) to prevent replay attacks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let serverChallenge: AVContentKeySessionServerPlaybackContextOption
```

## Discussion

Specify this value as an 8-byte [NSData](../../foundation/nsdata.md) object. If you don’t specify a value for this key, the system assumes a default server challenge of `0`.

## See Also

### Server playback context options

- [AVContentKeySessionServerPlaybackContextOptionProtocolVersions](protocolversions.md) — Specifies the versions of the content protection protocols supported by the application.
