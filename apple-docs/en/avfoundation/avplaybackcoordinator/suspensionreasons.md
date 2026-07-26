---
title: suspensionReasons
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplaybackcoordinator/suspensionreasons
source_url: 'https://developer.apple.com/documentation/avfoundation/avplaybackcoordinator/suspensionreasons'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplaybackcoordinator/suspensionreasons.json'
content_hash: 'sha256:8a673a7c6a00baf1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlaybackCoordinator](../avplaybackcoordinator.md)

# suspensionReasons

<sub>Instance Property</sub>

The reasons a coordinator is currently unable to participate in a group playback activity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var suspensionReasons: [AVCoordinatedPlaybackSuspension.Reason] { get }
```

## Discussion

The coordinator doesn’t respond to changes in group playback state when this property value contains suspension reasons.

> [!note] Note
> To observe changes to this property value, register for notifications of type [AVPlaybackCoordinatorSuspensionReasonsDidChangeNotification](suspensionreasonsdidchangenotification.md).

## See Also

### Observing suspension reasons

- [AVPlaybackCoordinatorSuspensionReasonsDidChangeNotification](suspensionreasonsdidchangenotification.md) — A notification that the coordinator posts when its suspension reasons change.
