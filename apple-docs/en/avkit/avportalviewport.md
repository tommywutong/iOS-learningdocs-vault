---
title: AVPortalViewport
framework: AVKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [visionOS 27.0+ beta]
languages: [swift, swift, swift, swift, swift, occ, occ, occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/avkit/avportalviewport
source_url: 'https://developer.apple.com/documentation/avkit/avportalviewport'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avportalviewport.json'
content_hash: 'sha256:6255397e89dacaf9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPortalViewport

<sub>Class</sub>

A viewport configuration used when displaying content in portals.

<sub>visionOS</sub>

```swift
class AVPortalViewport
```

## Overview

Defines the visual parameters for content displayed within a portal frame. Use this configuration to create cinematic viewing experiences with custom framing.

Portal viewports allow you to control how immersive content is framed and presented to users. You can specify the aspect ratio of the portal frame to achieve the desired visual effect.

When properties are not explicitly set, the system provides sensible defaults:

- Aspect Ratio: Defaults to 16:9 (1.78) for standard widescreen content

> [!note] Note
> Spatial videos do not support portal viewport settings.

```swift
let portalViewport = AVPortalViewport()
portalViewport.aspectRatio = 2.39
playerViewController.viewport.portal = portalViewport
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring the aspect ratio

- [aspectRatio](avportalviewport/aspectratio-4drnq.md) — The aspect ratio of the portal frame. _(beta)_

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
- [AVGroupExperienceCoordinator](avgroupexperiencecoordinator.md) — An object that synchronizes viewing environment state across participants in a SharePlay session.
- [AVViewport](avviewport.md) — A configuration object that manages viewport settings for different presentation modes. _(beta)_
- [Third-party casting support](third-party-casting-support.md) — Provide custom playback controls for third-party casting services and other media sources.
