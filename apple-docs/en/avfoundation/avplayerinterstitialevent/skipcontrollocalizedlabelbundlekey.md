---
title: skipControlLocalizedLabelBundleKey
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialevent/skipcontrollocalizedlabelbundlekey
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/skipcontrollocalizedlabelbundlekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialevent/skipcontrollocalizedlabelbundlekey.json'
content_hash: 'sha256:638d475347fdfee1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEvent](../avplayerinterstitialevent.md)

# skipControlLocalizedLabelBundleKey

<sub>Instance Property</sub>

The key defined in the AVPlayerInterstitialEventController’s localizedStringsBundle that points to the localized label for the skip button.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var skipControlLocalizedLabelBundleKey: String? { get set }
```

## Discussion

If the value of the property is nil, the skip button may contain a generic label depending on the implementation of the UI that’s in use. To ensure the best available user experience in various playback configurations, including external playback, set a value for this property that provides localized translations of skip control labels.

## See Also

### Managing skipping behavior

- [skipControlTimeRange](skipcontroltimerange.md) — The time range within the duration of the interstitial event for which a skip button should be displayed.
- [SkippableEventState](skippableeventstate.md) — These constants describe the state for a skippable AVPlayerInterstitialEvent.
