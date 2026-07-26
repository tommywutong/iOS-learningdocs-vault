---
title: localizedStringsTableName
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialeventcontroller/localizedstringstablename
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventcontroller/localizedstringstablename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialeventcontroller/localizedstringstablename.json'
content_hash: 'sha256:0f4366fc8646e6ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEventController](../avplayerinterstitialeventcontroller.md)

# localizedStringsTableName

<sub>Instance Property</sub>

The name of the table in the bundle that contains the localized strings to be used by the AVPlayerInterstitialEventController.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var localizedStringsTableName: String? { get set }
```

## Discussion

If the value of the property is nil, it will default to “Localizable”

## See Also

### Accessing strings

- [localizedStringsBundle](localizedstringsbundle.md) — The bundle that contains the localized strings to be used by the AVPlayerInterstitialEventController.
