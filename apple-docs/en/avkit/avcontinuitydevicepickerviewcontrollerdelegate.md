---
title: AVContinuityDevicePickerViewControllerDelegate
framework: AVKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [tvOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avcontinuitydevicepickerviewcontrollerdelegate
source_url: 'https://developer.apple.com/documentation/avkit/avcontinuitydevicepickerviewcontrollerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcontinuitydevicepickerviewcontrollerdelegate.json'
content_hash: 'sha256:f5f679b73ca52984'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVContinuityDevicePickerViewControllerDelegate

<sub>Protocol</sub>

An interface that responds to events from a continuity device picker view controller.

<sub>tvOS</sub>

```swift
protocol AVContinuityDevicePickerViewControllerDelegate : NSObjectProtocol
```

## Overview

Your app can respond to the various outcome events from an [AVContinuityDevicePickerViewController](avcontinuitydevicepickerviewcontroller.md) instance with the following steps:

1. Adopt the [AVContinuityDevicePickerViewControllerDelegate](avcontinuitydevicepickerviewcontrollerdelegate.md) protocol with one of the app’s classes.
2. Create an instance of that class.
3. Assign that instance to the view controller’s [delegate](avcontinuitydevicepickerviewcontroller/delegate.md) property.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Responding to continuity device events

- [- continuityDevicePickerWillBeginPresenting:](<avcontinuitydevicepickerviewcontrollerdelegate/continuitydevicepickerwillbeginpresenting(__).md>) — Informs the delegate that a continuity device picker is about to present its UI so that a person can select and connect a continuity device.
- [- continuityDevicePickerDidCancel:](<avcontinuitydevicepickerviewcontrollerdelegate/continuitydevicepickerdidcancel(__).md>) — Informs the delegate when a person declines to select a continuity device by dismissing an app’s continuity device picker.
- [- continuityDevicePicker:didConnectDevice:](<avcontinuitydevicepickerviewcontrollerdelegate/continuitydevicepicker(__didconnect_).md>) — Informs the delegate when a person selects and connects a continuity device to the system with a continuity device picker.
- [- continuityDevicePickerDidEndPresenting:](<avcontinuitydevicepickerviewcontrollerdelegate/continuitydevicepickerdidendpresenting(__).md>) — Informs the delegate that a continuity device picker is no longer presenting its UI to a person.

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
- [AVDisplayManager](avdisplaymanager.md) — A tvOS management object that controls whether a TV switches modes to match the video’s native mode.
- [AVContinuityDevicePickerViewController](avcontinuitydevicepickerviewcontroller.md) — A view controller that provides an interface to a person so they can select and connect a continuity device to the system.
- [Third-party casting support](third-party-casting-support.md) — Provide custom playback controls for third-party casting services and other media sources.
