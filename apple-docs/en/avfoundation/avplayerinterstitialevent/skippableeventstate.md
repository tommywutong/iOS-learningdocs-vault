---
title: AVPlayerInterstitialEvent.SkippableEventState
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialevent/skippableeventstate
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/skippableeventstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialevent/skippableeventstate.json'
content_hash: 'sha256:98e799469cd4b197'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEvent](../avplayerinterstitialevent.md)

# AVPlayerInterstitialEvent.SkippableEventState

<sub>Enumeration</sub>

These constants describe the state for a skippable AVPlayerInterstitialEvent.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum SkippableEventState
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Event states

- [AVPlayerInterstitialEventSkippableEventStateEligible](skippableeventstate/eligible.md) — Indicates that the interstitial event is currently skippable.
- [AVPlayerInterstitialEventSkippableEventStateNoLongerEligible](skippableeventstate/nolongereligible.md) — Indicates that the interstitial event is no longer eligible to be skipped.
- [AVPlayerInterstitialEventSkippableEventStateNotSkippable](skippableeventstate/notskippable.md) — Indicates that the interstitial event is not skippable.
- [AVPlayerInterstitialEventSkippableEventStateNotYetEligible](skippableeventstate/notyeteligible.md) — Indicates that the interstitial event will eventually become eligible to be skipped.

### Initializers

- [init(rawValue:)](<skippableeventstate/init(rawvalue_).md>)

## See Also

### Managing skipping behavior

- [skipControlLocalizedLabelBundleKey](skipcontrollocalizedlabelbundlekey.md) — The key defined in the AVPlayerInterstitialEventController’s localizedStringsBundle that points to the localized label for the skip button.
- [skipControlTimeRange](skipcontroltimerange.md) — The time range within the duration of the interstitial event for which a skip button should be displayed.
