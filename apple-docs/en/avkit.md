---
title: AVKit
framework: AVKit
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avkit
source_url: 'https://developer.apple.com/documentation/avkit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit.json'
content_hash: 'sha256:e4cace3ce4aafa16'
translated: false
---

> Navigation: [Technologies](technologies.md)

# AVKit

<sub>Framework</sub>

Create user interfaces for media playback, complete with transport controls, chapter navigation, picture-in-picture support, and display of subtitles and closed captions.

## Topics

### iOS playback and capture

- [Playing video content in a standard user interface](avkit/playing-video-content-in-a-standard-user-interface.md) — Play media full screen, embedded inline, or in a floating Picture in Picture (PiP) window using a player view controller.
- [AVPlayerViewController](avkit/avplayerviewcontroller.md) — A view controller that displays content from a player and presents a native user interface to control playback.
- [AVPlayerViewControllerDelegate](avkit/avplayerviewcontrollerdelegate.md) — A protocol that defines the methods to implement to respond to player view controller events.
- [AVCaptureEventInteraction](avkit/avcaptureeventinteraction.md) — An object that registers handlers to respond to capture events from system hardware buttons.
- [AVCaptureEvent](avkit/avcaptureevent.md) — An object that describes a user interaction with a system hardware button.
- [AVCaptureEventSound](avkit/avcaptureeventsound.md) — A sound object for a capture event.
- [AVInputPickerInteraction](avkit/avinputpickerinteraction.md) — Use `AVInputPickerInteraction` to present an input picker.
- [Third-party casting support](avkit/third-party-casting-support.md) — Provide custom playback controls for third-party casting services and other media sources.

### tvOS playback and capture

- [Customizing the tvOS Playback Experience](avkit/customizing-the-tvos-playback-experience.md) — Adopt the latest features of the redesigned tvOS player user interface to provide a more streamlined way to watch your content.
- [Presenting Navigation Markers](avkit/presenting-navigation-markers.md) — Present navigation markers in the Chapters panel to help users quickly navigate your content.
- [Working with Interstitial Content](avkit/working-with-interstitial-content.md) — Present additional content alongside your main media presentation using HTTP Live Streaming support.
- [Presenting Content Proposals in tvOS](avkit/presenting-content-proposals-in-tvos.md) — Display a preview of an upcoming media item at the conclusion of the currently playing media item.
- [Working with Overlays and Parental Controls in tvOS](avkit/working-with-overlays-and-parental-controls-in-tvos.md) — Add interactive overlays, parental controls, and livestream channel flipping using a player view controller.
- [Supporting Continuity Camera in your tvOS app](avkit/supporting-continuity-camera-in-your-tvos-app.md) — Capture high-quality photos, video, and audio in your Apple TV app by connecting an iPhone or iPad as a continuity device.
- [AVPlayerViewController](avkit/avplayerviewcontroller.md) — A view controller that displays content from a player and presents a native user interface to control playback.
- [AVPlayerViewControllerDelegate](avkit/avplayerviewcontrollerdelegate.md) — A protocol that defines the methods to implement to respond to player view controller events.
- [AVInterstitialTimeRange](avkit/avinterstitialtimerange.md) — A time range in an audiovisual presentation for content with an interstitial designation, such as advertisements or legal notices.
- [AVNavigationMarkersGroup](avkit/avnavigationmarkersgroup.md) — A set of markers for navigating playback of an audiovisual presentation.
- [AVContentProposalViewController](avkit/avcontentproposalviewcontroller.md) — A view controller that proposes content to watch next.
- [AVDisplayManager](avkit/avdisplaymanager.md) — A tvOS management object that controls whether a TV switches modes to match the video’s native mode.
- [AVContinuityDevicePickerViewController](avkit/avcontinuitydevicepickerviewcontroller.md) — A view controller that provides an interface to a person so they can select and connect a continuity device to the system.
- [AVContinuityDevicePickerViewControllerDelegate](avkit/avcontinuitydevicepickerviewcontrollerdelegate.md) — An interface that responds to events from a continuity device picker view controller.
- [Third-party casting support](avkit/third-party-casting-support.md) — Provide custom playback controls for third-party casting services and other media sources.

### visionOS playback

- [Playing immersive media with AVKit](avkit/playing-immersive-media-with-avkit.md) — Adopt the system playback interface to provide an immersive video watching experience.
- [Creating a multiview video playback experience in visionOS](avkit/creating-a-multiview-video-playback-experience-in-visionos.md) — Build an interface that plays multiple videos simultaneously and handles transitions to different experience types gracefully.
- [Adopting the system player interface in visionOS](avkit/adopting-the-system-player-interface-in-visionos.md) — Provide an optimized viewing experience for watching 3D video content.
- [Trimming and exporting media in visionOS](avkit/trimming-and-exporting-media-in-visionos.md) — Display standard controls in your app to edit the timeline of the currently playing media.
- [AVPlayerViewController](avkit/avplayerviewcontroller.md) — A view controller that displays content from a player and presents a native user interface to control playback.
- [AVPlayerViewControllerDelegate](avkit/avplayerviewcontrollerdelegate.md) — A protocol that defines the methods to implement to respond to player view controller events.
- [AVExperienceController](avkit/avexperiencecontroller.md) — An object that controls video experiences.
- [AVMultiviewManager](avkit/avmultiviewmanager.md) — An object that manages viewing multiple videos at once.
- [AVGroupExperienceCoordinator](avkit/avgroupexperiencecoordinator.md) — An object that synchronizes viewing environment state across participants in a SharePlay session.
- [AVViewport](avkit/avviewport.md) — A configuration object that manages viewport settings for different presentation modes. _(beta)_
- [AVPortalViewport](avkit/avportalviewport.md) — A viewport configuration used when displaying content in portals. _(beta)_
- [Third-party casting support](avkit/third-party-casting-support.md) — Provide custom playback controls for third-party casting services and other media sources.

### macOS playback and capture

- [Implementing Trimming in a macOS Player](avkit/implementing-trimming-in-a-macos-player.md) — Provide a QuickTime media-trimming experience in your macOS app.
- [AVPlayerView](avkit/avplayerview.md) — A view that displays content from a player and presents a native user interface to control playback.
- [AVCaptureView](avkit/avcaptureview.md) — A view that displays standard user interface controls for capturing media data.

### Multiplatform playback and capture

- [VideoPlayer](avkit/videoplayer.md) — A view that displays content from a player and a native user interface to control playback.

### Picture in Picture

- [Adopting Picture in Picture Playback in tvOS](avkit/adopting-picture-in-picture-playback-in-tvos.md) — Add advanced multitasking capabilities to your video apps by using Picture in Picture playback in tvOS.
- [Adopting Picture in Picture in a Standard Player](avkit/adopting-picture-in-picture-in-a-standard-player.md) — Add Picture in Picture (PiP) playback to your app using a player view controller.
- [Adopting Picture in Picture in a Custom Player](avkit/adopting-picture-in-picture-in-a-custom-player.md) — Add controls to your custom player user interface to invoke Picture in Picture (PiP) playback.
- [Adopting Picture in Picture for video calls](avkit/adopting-picture-in-picture-for-video-calls.md) — Add multitasking capability to your video-call apps by using Picture in Picture (PiP).
- [Accessing the camera while multitasking on iPad](avkit/accessing-the-camera-while-multitasking-on-ipad.md) — Operate the camera in Split View, Slide Over, Picture in Picture, and Stage Manager modes.
- [AVPictureInPictureController](avkit/avpictureinpicturecontroller.md) — A controller that responds to user-initiated Picture in Picture playback of video in a floating, resizable window.

### Legible media options

- [AVLegibleMediaOptionsMenuController](avkit/avlegiblemediaoptionsmenucontroller.md)
- [AVLegibleMediaOptionsMenuState](avkit/avlegiblemediaoptionsmenustate.md)

### Playback route selection

- [AVRoutePickerView](avkit/avroutepickerview.md) — A view that presents a list of nearby media receivers.

### Metadata

- [AVKit Metadata Identifiers](avkit/avkit-metadata-identifiers.md) — Additional metadata that an asset contains.

### Errors

- [AVKitErrorDomain](avkit/avkiterrordomain.md) — The domain of errors the framework generates.
- [AVKitError](avkit/avkiterror-swift.struct.md) — A structure that represents a framework error.
- [Code](avkit/avkiterror-swift.struct/code.md) — Constants that identify framework error codes.

### Macros

- [Macros](avkit/avkit-macros.md)
