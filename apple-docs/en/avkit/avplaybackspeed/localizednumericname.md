---
title: localizedNumericName
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplaybackspeed/localizednumericname
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackspeed/localizednumericname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackspeed/localizednumericname.json'
content_hash: 'sha256:2e0f299ba8e59cd9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackSpeed](../avplaybackspeed.md)

# localizedNumericName

<sub>Instance Property</sub>

A localized numeric name for a speed that’s suitable for display in a user interface.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var localizedNumericName: String { get }
```

## Discussion

Use this value to represent the speed in a user interface where limited space is available. Represent the speed using its [localizedName](localizedname.md) value where space allows.

## See Also

### Inspecting Speed Details

- [rate](rate.md) — The playback rate to use when you select this speed.
- [localizedName](localizedname.md) — A localized name for a speed that’s suitable for display in a user interface.
