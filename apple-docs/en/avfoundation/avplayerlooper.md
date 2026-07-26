---
title: AVPlayerLooper
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerlooper
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerlooper'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerlooper.json'
content_hash: 'sha256:333b07a0d4c800eb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerLooper

<sub>Class</sub>

An object that loops media content using a queue player.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVPlayerLooper
```

## Overview

You can manually implement looping playback in your app using [AVQueuePlayer](avqueueplayer.md), but `AVPlayerLooper` provides a much simpler interface to loop a single [AVPlayerItem](avplayeritem.md). You create a player looper by passing it a reference to your [AVQueuePlayer](avqueueplayer.md) and a template [AVPlayerItem](avplayeritem.md) and the looper automatically manages the looping playback of this content (see example).

```swift
let asset = // AVAsset with its 'duration' property value loaded
let playerItem = AVPlayerItem(asset: asset)
 
// Create a new player looper with the queue player and template item
playerLooper = AVPlayerLooper(player: queuePlayer, templateItem: playerItem)
 
// Begin looping playback
queuePlayer.play()
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a player looper

- [- initWithPlayer:templateItem:timeRange:existingItemsOrdering:](<avplayerlooper/init(player_templateitem_timerange_existingitemsordering_).md>) — Creates a player looper that continuously plays the full duration of a player item while adhering to the specified ordering of existing items in the queue.
- [+ playerLooperWithPlayer:templateItem:](<avplayerlooper/init(player_templateitem_).md>) — Creates a player looper that continuously plays the full duration of a player item.
- [- initWithPlayer:templateItem:timeRange:](<avplayerlooper/init(player_templateitem_timerange_).md>) — Creates a player looper that continuously plays the specified time range of a player item.

### Configuring looping

- [loopingPlayerItems](avplayerlooper/loopingplayeritems.md) — An array containing replicas of the template player item used to accomplish the looping.
- [- disableLooping](<avplayerlooper/disablelooping().md>) — Disables looping for the player queue.

### Observing looping state

- [loopCount](avplayerlooper/loopcount.md) — The number of times the object played the media.
- [status](avplayerlooper/status-swift.property.md) — A status that indicates the object’s ability to loop playback.
- [Status](avplayerlooper/status-swift.enum.md) — Status constants that indicate whether a looper can successfully perform looping playback.

### Monitoring errors

- [error](avplayerlooper/error.md) — An error that describes the reason looping failed.

## See Also

### Playback control

- [Observing playback state in SwiftUI](observing-playback-state-in-swiftui.md) — Keep your user interface in sync with state changes from playback objects.
- [Controlling the transport behavior of a player](controlling-the-transport-behavior-of-a-player.md) — Play, pause, and seek through a media presentation.
- [Creating a seamless multiview playback experience](creating-a-seamless-multiview-playback-experience.md) — Build advanced multiview playback experiences with the AVFoundation and AVRouting frameworks.
- [AVPlayer](avplayer.md) — An object that provides the interface to control the player’s transport behavior.
- [AVPlayerItem](avplayeritem.md) — An object that models the timing and presentation state of an asset during playback.
- [AVPlayerItemTrack](avplayeritemtrack.md) — An object that represents the presentation state of an asset track during playback.
- [AVQueuePlayer](avqueueplayer.md) — An object that plays a sequence of player items.
