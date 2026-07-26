---
title: AVNavigationMarkersGroup
framework: AVKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [tvOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avnavigationmarkersgroup
source_url: 'https://developer.apple.com/documentation/avkit/avnavigationmarkersgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avnavigationmarkersgroup.json'
content_hash: 'sha256:b5e0695c23a9bde3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVNavigationMarkersGroup

<sub>Class</sub>

A set of markers for navigating playback of an audiovisual presentation.

<sub>tvOS</sub>

```swift
class AVNavigationMarkersGroup
```

## Overview

The most common form of a navigation markers group is a chapter list; however, you can also provide other sets of markers to allow a user to jump to significant events in the presentation. For example, a “Goals Scored” markers group might summarize key moments in a recorded sporting event. When you associate navigation markers with an [AVPlayerItem](../avfoundation/avplayeritem.md) object you present with an [AVPlayerViewController](avplayerviewcontroller.md), the user interface provides options for navigating each group.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a Navigation Marker Group

- [- initWithTitle:timedNavigationMarkers:](<avnavigationmarkersgroup/init(title_timednavigationmarkers_).md>) — Initializes a navigation markers group with the specified title and array of timed navigation markers.
- [- initWithTitle:dateRangeNavigationMarkers:](<avnavigationmarkersgroup/init(title_daterangenavigationmarkers_).md>) — Initializes a navigation markers group with the specified title and array of date range navigation markers.

### Inspecting Navigation Metadata

- [title](avnavigationmarkersgroup/title.md) — The title of the marker group.
- [timedNavigationMarkers](avnavigationmarkersgroup/timednavigationmarkers.md) — The array of timed navigation markers for which the group provides navigation.
- [dateRangeNavigationMarkers](avnavigationmarkersgroup/daterangenavigationmarkers.md) — The array of date range navigation markers for which the group provides navigation.

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
- [AVContentProposalViewController](avcontentproposalviewcontroller.md) — A view controller that proposes content to watch next.
- [AVDisplayManager](avdisplaymanager.md) — A tvOS management object that controls whether a TV switches modes to match the video’s native mode.
- [AVContinuityDevicePickerViewController](avcontinuitydevicepickerviewcontroller.md) — A view controller that provides an interface to a person so they can select and connect a continuity device to the system.
- [AVContinuityDevicePickerViewControllerDelegate](avcontinuitydevicepickerviewcontrollerdelegate.md) — An interface that responds to events from a continuity device picker view controller.
- [Third-party casting support](third-party-casting-support.md) — Provide custom playback controls for third-party casting services and other media sources.
