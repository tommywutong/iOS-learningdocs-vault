---
title: suspensionReasonsDidChangeNotification
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplaybackcoordinator/suspensionreasonsdidchangenotification
source_url: 'https://developer.apple.com/documentation/avfoundation/avplaybackcoordinator/suspensionreasonsdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplaybackcoordinator/suspensionreasonsdidchangenotification.json'
content_hash: 'sha256:ac4243488051223e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlaybackCoordinator](../avplaybackcoordinator.md)

# suspensionReasonsDidChangeNotification

<sub>Type Property</sub>

A notification that the coordinator posts when its suspension reasons change.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class let suspensionReasonsDidChangeNotification: NSNotification.Name
```

## See Also

### Observing suspension reasons

- [suspensionReasons](suspensionreasons.md) — The reasons a coordinator is currently unable to participate in a group playback activity.
