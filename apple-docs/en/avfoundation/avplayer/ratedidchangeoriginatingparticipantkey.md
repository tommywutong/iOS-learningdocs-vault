---
title: rateDidChangeOriginatingParticipantKey
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/ratedidchangeoriginatingparticipantkey
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/ratedidchangeoriginatingparticipantkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/ratedidchangeoriginatingparticipantkey.json'
content_hash: 'sha256:52f8ced536c906f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# rateDidChangeOriginatingParticipantKey

<sub>Type Property</sub>

A key to retrieve the identifier of the participant that originates the rate change.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class let rateDidChangeOriginatingParticipantKey: String
```

## Discussion

The associated value is a UUID of a participant in the playback coordinator’s [otherParticipants](../avplaybackcoordinator/otherparticipants.md) array.

## See Also

### User information keys

- [AVPlayerRateDidChangeReasonKey](ratedidchangereasonkey.md) — A key to retrieve the reason for the rate change.
- [RateDidChangeReason](ratedidchangereason.md) — A structure that represents a rate change reason.
