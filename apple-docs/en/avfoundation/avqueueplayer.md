---
title: AVQueuePlayer
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avqueueplayer
source_url: 'https://developer.apple.com/documentation/avfoundation/avqueueplayer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avqueueplayer.json'
content_hash: 'sha256:2daa8a7a698ac9fa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVQueuePlayer

<sub>Class</sub>

An object that plays a sequence of player items.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVQueuePlayer
```

## Overview

Use an instance of this class to manage a queue of player items.

## Relationships

- **Inherits From**: [AVPlayer](avplayer.md)

- **Conforms To**: [AVRoutingPlaybackParticipant](../avrouting/avroutingplaybackparticipant.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Observable](../observation/observable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a queue player

- [- initWithItems:](<avqueueplayer/init(items_).md>) — Creates an object that plays a queue of items.

### Managing the player queue

- [- items](<avqueueplayer/items().md>) — Returns an array of the currently enqueued items.
- [- advanceToNextItem](<avqueueplayer/advancetonextitem().md>) — Ends playback of the current item and starts playback of the next item in the player’s queue.
- [- canInsertItem:afterItem:](<avqueueplayer/caninsert(__after_).md>) — Returns a Boolean value that indicates whether you can insert a player item into the player’s queue.
- [- insertItem:afterItem:](<avqueueplayer/insert(__after_).md>) — Inserts a player item after another player item in the queue.
- [- removeItem:](<avqueueplayer/remove(__).md>) — Removes a given player item from the queue.
- [- removeAllItems](<avqueueplayer/removeallitems().md>) — Removes all player items from the queue.

## See Also

### Playback control

- [Observing playback state in SwiftUI](observing-playback-state-in-swiftui.md) — Keep your user interface in sync with state changes from playback objects.
- [Controlling the transport behavior of a player](controlling-the-transport-behavior-of-a-player.md) — Play, pause, and seek through a media presentation.
- [Creating a seamless multiview playback experience](creating-a-seamless-multiview-playback-experience.md) — Build advanced multiview playback experiences with the AVFoundation and AVRouting frameworks.
- [AVPlayer](avplayer.md) — An object that provides the interface to control the player’s transport behavior.
- [AVPlayerItem](avplayeritem.md) — An object that models the timing and presentation state of an asset during playback.
- [AVPlayerItemTrack](avplayeritemtrack.md) — An object that represents the presentation state of an asset track during playback.
- [AVPlayerLooper](avplayerlooper.md) — An object that loops media content using a queue player.
