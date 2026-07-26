---
title: AVContinuityDevicePickerViewController
framework: AVKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [tvOS 17.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avcontinuitydevicepickerviewcontroller
source_url: 'https://developer.apple.com/documentation/avkit/avcontinuitydevicepickerviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcontinuitydevicepickerviewcontroller.json'
content_hash: 'sha256:1e47fec00f00d9c5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVContinuityDevicePickerViewController

<sub>Class</sub>

A view controller that provides an interface to a person so they can select and connect a continuity device to the system.

<sub>tvOS</sub>

```swift
class AVContinuityDevicePickerViewController
```

## Overview

The view controller presents an interface on an Apple TV that lets a person choose a nearby continuity device ([AVContinuityDevice](../avfoundation/avcontinuitydevice.md)). Your app can then connect to that device’s cameras and microphones (see [AVCaptureDevice](../avfoundation/avcapturedevice.md) and [AVAudioSessionPortDescription](../avfaudio/avaudiosessionportdescription.md), respectively).

> [!important] Important
> The continuity device picker presents any devices near the Apple TV that use the same Apple ID.

To respond to the various outcome events from the picker, your app needs to implement the [AVContinuityDevicePickerViewControllerDelegate](avcontinuitydevicepickerviewcontrollerdelegate.md) and assign it to the picker’s [delegate](avcontinuitydevicepickerviewcontroller/delegate.md) property.

> [!note] Note
> SwiftUI apps can present the same interface with the [continuityDevicePicker(isPresented:onDidConnect:)](<../swiftui/view/continuitydevicepicker(ispresented_ondidconnect_).md>) view modifier.

## Relationships

- **Inherits From**: [UIViewController](../uikit/uiviewcontroller.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md), [UIAppearanceContainer](../uikit/uiappearancecontainer.md), [UIContentContainer](../uikit/uicontentcontainer.md), [UIFocusEnvironment](../uikit/uifocusenvironment.md), [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md), [UIStateRestoring](../uikit/uistaterestoring.md), [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md), [UITraitEnvironment](../uikit/uitraitenvironment.md), [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## Topics

### Checking for feature support

- [supported](avcontinuitydevicepickerviewcontroller/issupported.md) — A Boolean value that indicates whether the system supports connecting to a continuity device.

### Designating a delegate

- [delegate](avcontinuitydevicepickerviewcontroller/delegate.md) — The delegate that responds to events from the continuity device picker view controller.

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
- [AVContinuityDevicePickerViewControllerDelegate](avcontinuitydevicepickerviewcontrollerdelegate.md) — An interface that responds to events from a continuity device picker view controller.
- [Third-party casting support](third-party-casting-support.md) — Provide custom playback controls for third-party casting services and other media sources.
