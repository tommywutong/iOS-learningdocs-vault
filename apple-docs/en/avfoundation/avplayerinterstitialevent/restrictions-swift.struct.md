---
title: AVPlayerInterstitialEvent.Restrictions
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialevent/restrictions-swift.struct
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/restrictions-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialevent/restrictions-swift.struct.json'
content_hash: 'sha256:9c9a0c527202356e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEvent](../avplayerinterstitialevent.md)

# AVPlayerInterstitialEvent.Restrictions

<sub>Structure</sub>

Constants that define restrictions on the playback of interstitial content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Restrictions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Configure

- [AVPlayerInterstitialEventRestrictionConstrainsSeekingForwardInPrimaryContent](restrictions-swift.struct/constrainsseekingforwardinprimarycontent.md) — A restriction that indicates the event doesn’t allow seeking forward within an interstitial item.
- [AVPlayerInterstitialEventRestrictionRequiresPlaybackAtPreferredRateForAdvancement](restrictions-swift.struct/requiresplaybackatpreferredrateforadvancement.md) — A restriction that indicates the event doesn’t allow advancing the current time within an interstitial item.

### Initializing a restriction

- [init(rawValue:)](<restrictions-swift.struct/init(rawvalue_).md>) — Creates a restriction with an integer.

## See Also

### Managing restrictions

- [restrictions](restrictions-swift.property.md) — The restrictions the event imposes on the playback of interstitial content.
