---
title: currentDate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemintegratedtimeline/currentdate
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimeline/currentdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemintegratedtimeline/currentdate.json'
content_hash: 'sha256:d55dd3219c07a04e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemIntegratedTimeline](../avplayeritemintegratedtimeline.md)

# currentDate

<sub>Instance Property</sub>

The current date of playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var currentDate: Date? { get }
```

## Discussion

This value is `nil` if playback doesn’t map to a date.

## See Also

### Inspecting the time and date

- [currentTime](currenttime.md) — The current time on the integrated timeline.
