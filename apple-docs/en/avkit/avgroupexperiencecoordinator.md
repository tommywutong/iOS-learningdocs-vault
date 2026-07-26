---
title: AVGroupExperienceCoordinator
framework: AVKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avgroupexperiencecoordinator
source_url: 'https://developer.apple.com/documentation/avkit/avgroupexperiencecoordinator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avgroupexperiencecoordinator.json'
content_hash: 'sha256:b02f2bf04a45fad8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVGroupExperienceCoordinator

<sub>Class</sub>

An object that synchronizes viewing environment state across participants in a SharePlay session.

<sub>visionOS</sub>

```swift
@objc(AVGroupExperienceCoordinator) class AVGroupExperienceCoordinator
```

## Overview

Access an experience coordinator by querying a player view controller for its [groupExperienceCoordinator](avplayerviewcontroller/groupexperiencecoordinator.md) object.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Coordinating state changes

- [coordinateWithSession(_:)](<avgroupexperiencecoordinator/coordinatewithsession(__).md>) — Begins coordinating viewing environment state with a group session.

## See Also

### visionOS playback

- [Playing immersive media with AVKit](playing-immersive-media-with-avkit.md) — Adopt the system playback interface to provide an immersive video watching experience.
- [Creating a multiview video playback experience in visionOS](creating-a-multiview-video-playback-experience-in-visionos.md) — Build an interface that plays multiple videos simultaneously and handles transitions to different experience types gracefully.
- [Adopting the system player interface in visionOS](adopting-the-system-player-interface-in-visionos.md) — Provide an optimized viewing experience for watching 3D video content.
- [Trimming and exporting media in visionOS](trimming-and-exporting-media-in-visionos.md) — Display standard controls in your app to edit the timeline of the currently playing media.
- [AVPlayerViewController](avplayerviewcontroller.md) — A view controller that displays content from a player and presents a native user interface to control playback.
- [AVPlayerViewControllerDelegate](avplayerviewcontrollerdelegate.md) — A protocol that defines the methods to implement to respond to player view controller events.
- [AVExperienceController](avexperiencecontroller.md) — An object that controls video experiences.
- [AVMultiviewManager](avmultiviewmanager.md) — An object that manages viewing multiple videos at once.
- [AVViewport](avviewport.md) — A configuration object that manages viewport settings for different presentation modes. _(beta)_
- [AVPortalViewport](avportalviewport.md) — A viewport configuration used when displaying content in portals. _(beta)_
- [Third-party casting support](third-party-casting-support.md) — Provide custom playback controls for third-party casting services and other media sources.
