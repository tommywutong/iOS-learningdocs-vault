---
title: AVMultiviewManager
framework: AVKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avmultiviewmanager
source_url: 'https://developer.apple.com/documentation/avkit/avmultiviewmanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avmultiviewmanager.json'
content_hash: 'sha256:00351000e48b96f6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVMultiviewManager

<sub>Class</sub>

An object that manages viewing multiple videos at once.

<sub>visionOS</sub>

```swift
@MainActor final class AVMultiviewManager
```

## Overview

Watch multiple videos at the same time with [AVExperienceController.Experience.multiview](avexperiencecontroller/experience-swift.enum/multiview.md) using multiple [AVExperienceController](avexperiencecontroller.md) objects.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the default instance

- [default](avmultiviewmanager/default.md) — Use this default AVMultiviewManager to customize the multiview experience.

### Providing additional UI

- [contentSelectionViewController](avmultiviewmanager/contentselectionviewcontroller.md) — A view controller that presents a user interface to select additional video content to display.
- [AVContentSelectionViewController](avcontentselectionviewcontroller.md) — A view controller for providing additional UI to the multiview experience.

### Dismissing the multiview experience

- [dismiss()](<avmultiviewmanager/dismiss().md>) — Dismiss the multiview presentation.

## See Also

### visionOS playback

- [Playing immersive media with AVKit](playing-immersive-media-with-avkit.md) — Adopt the system playback interface to provide an immersive video watching experience.
- [Creating a multiview video playback experience in visionOS](creating-a-multiview-video-playback-experience-in-visionos.md) — Build an interface that plays multiple videos simultaneously and handles transitions to different experience types gracefully.
- [Adopting the system player interface in visionOS](adopting-the-system-player-interface-in-visionos.md) — Provide an optimized viewing experience for watching 3D video content.
- [Trimming and exporting media in visionOS](trimming-and-exporting-media-in-visionos.md) — Display standard controls in your app to edit the timeline of the currently playing media.
- [AVPlayerViewController](avplayerviewcontroller.md) — A view controller that displays content from a player and presents a native user interface to control playback.
- [AVPlayerViewControllerDelegate](avplayerviewcontrollerdelegate.md) — A protocol that defines the methods to implement to respond to player view controller events.
- [AVExperienceController](avexperiencecontroller.md) — An object that controls video experiences.
- [AVGroupExperienceCoordinator](avgroupexperiencecoordinator.md) — An object that synchronizes viewing environment state across participants in a SharePlay session.
- [AVViewport](avviewport.md) — A configuration object that manages viewport settings for different presentation modes. _(beta)_
- [AVPortalViewport](avportalviewport.md) — A viewport configuration used when displaying content in portals. _(beta)_
- [Third-party casting support](third-party-casting-support.md) — Provide custom playback controls for third-party casting services and other media sources.
