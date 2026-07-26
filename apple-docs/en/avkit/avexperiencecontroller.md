---
title: AVExperienceController
framework: AVKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avexperiencecontroller
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller.json'
content_hash: 'sha256:6f77f7e78860f4b3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVExperienceController

<sub>Class</sub>

An object that controls video experiences.

<sub>visionOS</sub>

```swift
@MainActor final class AVExperienceController
```

## Overview

Use this class to control, observe, and respond to experience changes for an [AVPlayerViewController](avplayerviewcontroller.md). A player view controller’s presentation APIs will no longer be honored after attaching an experience controller. Using the other presentation APIs may preclude the use of this class.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Configuring the experience

- [allowedExperiences](avexperiencecontroller/allowedexperiences.md) — The set of experiences the application supports.
- [availableExperiences](avexperiencecontroller/availableexperiences.md) — The allowed experiences that are available to use on the device at this time.
- [Experiences](avexperiencecontroller/experiences.md) — A structure that represents a collection of experiences to use with an experience controller.
- [experience](avexperiencecontroller/experience-swift.property.md) — The current experience.
- [Experience](avexperiencecontroller/experience-swift.enum.md) — The types of experiences the system supports.
- [configuration](avexperiencecontroller/configuration-swift.property.md) — The configuration options per experience.
- [Configuration](avexperiencecontroller/configuration-swift.struct.md) — A structure that stores per-experience configuration.

### Transitioning experiences

- [TransitionGroup](avexperiencecontroller/transitiongroup.md) — A group of experience transitions that prepare concurrently and run simultaneously as a single visual transition. _(beta)_
- [withTransitionGroup(body:)](<avexperiencecontroller/withtransitiongroup(body_).md>) — Coordinates multiple experience transitions to perform together as a single visual transition. _(beta)_
- [transition(to:)](<avexperiencecontroller/transition(to_).md>) — Transitions the video to a different experience.

### Configuring a delegate

- [delegate](avexperiencecontroller/delegate-swift.property.md) — A delegate object for the experience controller.
- [Delegate](avexperiencecontroller/delegate-swift.protocol.md) — A protocol that defines the methods to implement to respond to experience changes.

### Structures

- [ExpandedConfiguration](avexperiencecontroller/expandedconfiguration.md) — A structure that specifies options for an expanded experience.
- [TransitionContext](avexperiencecontroller/transitioncontext.md) — The state of the transition provided to the delegate object.

## See Also

### visionOS playback

- [Playing immersive media with AVKit](playing-immersive-media-with-avkit.md) — Adopt the system playback interface to provide an immersive video watching experience.
- [Creating a multiview video playback experience in visionOS](creating-a-multiview-video-playback-experience-in-visionos.md) — Build an interface that plays multiple videos simultaneously and handles transitions to different experience types gracefully.
- [Adopting the system player interface in visionOS](adopting-the-system-player-interface-in-visionos.md) — Provide an optimized viewing experience for watching 3D video content.
- [Trimming and exporting media in visionOS](trimming-and-exporting-media-in-visionos.md) — Display standard controls in your app to edit the timeline of the currently playing media.
- [AVPlayerViewController](avplayerviewcontroller.md) — A view controller that displays content from a player and presents a native user interface to control playback.
- [AVPlayerViewControllerDelegate](avplayerviewcontrollerdelegate.md) — A protocol that defines the methods to implement to respond to player view controller events.
- [AVMultiviewManager](avmultiviewmanager.md) — An object that manages viewing multiple videos at once.
- [AVGroupExperienceCoordinator](avgroupexperiencecoordinator.md) — An object that synchronizes viewing environment state across participants in a SharePlay session.
- [AVViewport](avviewport.md) — A configuration object that manages viewport settings for different presentation modes. _(beta)_
- [AVPortalViewport](avportalviewport.md) — A viewport configuration used when displaying content in portals. _(beta)_
- [Third-party casting support](third-party-casting-support.md) — Provide custom playback controls for third-party casting services and other media sources.
