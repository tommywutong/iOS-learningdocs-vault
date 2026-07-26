---
title: UIEvent.EventSubtype
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uievent/eventsubtype
source_url: 'https://developer.apple.com/documentation/uikit/uievent/eventsubtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uievent/eventsubtype.json'
content_hash: 'sha256:07e33153c5d2b848'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEvent](../uievent.md)

# UIEvent.EventSubtype

<sub>Enumeration</sub>

Constants that specify the subtype of the event in relation to its general type.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum EventSubtype
```

## Overview

You can obtain the subtype of an event from the [subtype](subtype.md) property.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIEventSubtypeNone](eventsubtype/none.md) — The event has no subtype.
- [UIEventSubtypeMotionShake](eventsubtype/motionshake.md) — The event is related to a person shaking the device.
- [UIEventSubtypeRemoteControlPlay](eventsubtype/remotecontrolplay.md) — A remote-control event for playing audio or video.
- [UIEventSubtypeRemoteControlPause](eventsubtype/remotecontrolpause.md) — A remote-control event for pausing audio or video.
- [UIEventSubtypeRemoteControlStop](eventsubtype/remotecontrolstop.md) — A remote-control event for stopping audio or video from playing.
- [UIEventSubtypeRemoteControlTogglePlayPause](eventsubtype/remotecontroltoggleplaypause.md) — A remote-control event for toggling audio or video between play and pause.
- [UIEventSubtypeRemoteControlNextTrack](eventsubtype/remotecontrolnexttrack.md) — A remote-control event for skipping to the next audio or video track.
- [UIEventSubtypeRemoteControlPreviousTrack](eventsubtype/remotecontrolprevioustrack.md) — A remote-control event for skipping to the previous audio or video track.
- [UIEventSubtypeRemoteControlBeginSeekingBackward](eventsubtype/remotecontrolbeginseekingbackward.md) — A remote-control event to start seeking backward through the audio or video medium.
- [UIEventSubtypeRemoteControlEndSeekingBackward](eventsubtype/remotecontrolendseekingbackward.md) — A remote-control event to end seeking backward through the audio or video medium.
- [UIEventSubtypeRemoteControlBeginSeekingForward](eventsubtype/remotecontrolbeginseekingforward.md) — A remote-control event to start seeking forward through the audio or video medium.
- [UIEventSubtypeRemoteControlEndSeekingForward](eventsubtype/remotecontrolendseekingforward.md) — A remote-control event to end seeking forward through the audio or video medium.

### Initializers

- [init(rawValue:)](<eventsubtype/init(rawvalue_).md>)

## See Also

### Getting the event type

- [type](type.md) — Returns the type of the event.
- [EventType](eventtype.md) — Constants that specify the general type of an event.
- [subtype](subtype.md) — Returns the subtype of the event.
