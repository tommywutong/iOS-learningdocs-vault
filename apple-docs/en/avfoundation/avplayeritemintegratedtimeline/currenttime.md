---
title: currentTime
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemintegratedtimeline/currenttime
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimeline/currenttime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemintegratedtimeline/currenttime.json'
content_hash: 'sha256:99aceb1073b9c961'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemIntegratedTimeline](../avplayeritemintegratedtimeline.md)

# currentTime

<sub>Instance Property</sub>

The current time on the integrated timeline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var currentTime: CMTime { get }
```

## Discussion

During playback of interstitial events that occupy a single point, this value doesn’t change.

## See Also

### Inspecting the time and date

- [currentDate](currentdate.md) — The current date of playback.
