---
title: localizedStringsBundle
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialeventcontroller/localizedstringsbundle
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventcontroller/localizedstringsbundle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialeventcontroller/localizedstringsbundle.json'
content_hash: 'sha256:cc8f20bfe3af47c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEventController](../avplayerinterstitialeventcontroller.md)

# localizedStringsBundle

<sub>Instance Property</sub>

The bundle that contains the localized strings to be used by the AVPlayerInterstitialEventController.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var localizedStringsBundle: Bundle? { get set }
```

## Discussion

If the value of the property is nil, any UI elements triggered by the AVPlayerInterstitialEventController, such as the skip button, may contain a generic label based on the implementation of the UI that’s in use. To ensure the best available user experience in various playback configurations, including external playback, set a value for this property that provides localized translations of skip control labels.

## See Also

### Accessing strings

- [localizedStringsTableName](localizedstringstablename.md) — The name of the table in the bundle that contains the localized strings to be used by the AVPlayerInterstitialEventController.
