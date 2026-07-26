---
title: 'coordinateWithSession(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplaybackcoordinator/coordinatewithsession(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplaybackcoordinator/coordinatewithsession(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplaybackcoordinator/coordinatewithsession%28_%3A%29.json'
content_hash: 'sha256:3296c7858184b22e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlaybackCoordinator](../avplaybackcoordinator.md)

# coordinateWithSession(_:)

<sub>Instance Method</sub>

Begins coordination of a player with a group session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func coordinateWithSession<T>(_ session: GroupSession<T>) where T : GroupActivity
```

## Parameters

- `session` — The group session with which to coordinate playback.
