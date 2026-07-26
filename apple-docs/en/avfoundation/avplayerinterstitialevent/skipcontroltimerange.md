---
title: skipControlTimeRange
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialevent/skipcontroltimerange
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/skipcontroltimerange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialevent/skipcontroltimerange.json'
content_hash: 'sha256:65849add6632e94d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEvent](../avplayerinterstitialevent.md)

# skipControlTimeRange

<sub>Instance Property</sub>

The time range within the duration of the interstitial event for which a skip button should be displayed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var skipControlTimeRange: CMTimeRange { get set }
```

## Discussion

The start of the time range should indicate at which point the skip button should appear. The duration of the time range should indicate how long the skip button should be available. If this value is set to kCMTimePositiveInfinity, then the skip button will be available for the remainder of the interstitial’s duration after appearing. If either the start or duration of the time range is kCMTimeInvalid, then the interstitial will NOT be eligible to be skipped.

## See Also

### Managing skipping behavior

- [skipControlLocalizedLabelBundleKey](skipcontrollocalizedlabelbundlekey.md) — The key defined in the AVPlayerInterstitialEventController’s localizedStringsBundle that points to the localized label for the skip button.
- [SkippableEventState](skippableeventstate.md) — These constants describe the state for a skippable AVPlayerInterstitialEvent.
