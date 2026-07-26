---
title: AVDisplayManager
framework: AVKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [tvOS 11.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avdisplaymanager
source_url: 'https://developer.apple.com/documentation/avkit/avdisplaymanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avdisplaymanager.json'
content_hash: 'sha256:edda7e512490b3de'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVDisplayManager

<sub>Class</sub>

A tvOS management object that controls whether a TV switches modes to match the video’s native mode.

<sub>tvOS, visionOS</sub>

```swift
class AVDisplayManager
```

## Overview

If you set the display manager’s [preferredDisplayCriteria](avdisplaymanager/preferreddisplaycriteria.md), when a user enables a Match Content setting, the TV attempts to change modes to match the currently playing video’s native display criteria.

> [!important] Important
> Don’t directly instantiate a display manager object. Instead, access the current instance from the key window’s [avDisplayManager](../uikit/uiwindow/avdisplaymanager.md) property.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Matching a Video’s Native Display Mode

- [preferredDisplayCriteria](avdisplaymanager/preferreddisplaycriteria.md) — A hint for the TV to set the display mode to best match the currently playing content’s display criteria.
- [displayCriteriaMatchingEnabled](avdisplaymanager/isdisplaycriteriamatchingenabled.md) — A Boolean value that indicates whether the user has enabled display critera matching.
- [displayModeSwitchInProgress](avdisplaymanager/isdisplaymodeswitchinprogress.md) — A Boolean value that indicates whether a display mode switch is in progress.

## See Also

### tvOS playback and capture

- [Customizing the tvOS Playback Experience](customizing-the-tvos-playback-experience.md) — Adopt the latest features of the redesigned tvOS player user interface to provide a more streamlined way to watch your content.
- [Presenting Navigation Markers](presenting-navigation-markers.md) — Present navigation markers in the Chapters panel to help users quickly navigate your content.
- [Working with Interstitial Content](working-with-interstitial-content.md) — Present additional content alongside your main media presentation using HTTP Live Streaming support.
- [Presenting Content Proposals in tvOS](presenting-content-proposals-in-tvos.md) — Display a preview of an upcoming media item at the conclusion of the currently playing media item.
- [Working with Overlays and Parental Controls in tvOS](working-with-overlays-and-parental-controls-in-tvos.md) — Add interactive overlays, parental controls, and livestream channel flipping using a player view controller.
- [Supporting Continuity Camera in your tvOS app](supporting-continuity-camera-in-your-tvos-app.md) — Capture high-quality photos, video, and audio in your Apple TV app by connecting an iPhone or iPad as a continuity device.
- [AVPlayerViewController](avplayerviewcontroller.md) — A view controller that displays content from a player and presents a native user interface to control playback.
- [AVPlayerViewControllerDelegate](avplayerviewcontrollerdelegate.md) — A protocol that defines the methods to implement to respond to player view controller events.
- [AVInterstitialTimeRange](avinterstitialtimerange.md) — A time range in an audiovisual presentation for content with an interstitial designation, such as advertisements or legal notices.
- [AVNavigationMarkersGroup](avnavigationmarkersgroup.md) — A set of markers for navigating playback of an audiovisual presentation.
- [AVContentProposalViewController](avcontentproposalviewcontroller.md) — A view controller that proposes content to watch next.
- [AVContinuityDevicePickerViewController](avcontinuitydevicepickerviewcontroller.md) — A view controller that provides an interface to a person so they can select and connect a continuity device to the system.
- [AVContinuityDevicePickerViewControllerDelegate](avcontinuitydevicepickerviewcontrollerdelegate.md) — An interface that responds to events from a continuity device picker view controller.
- [Third-party casting support](third-party-casting-support.md) — Provide custom playback controls for third-party casting services and other media sources.
