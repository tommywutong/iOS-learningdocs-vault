---
title: AVPlayerViewControllerDelegate
framework: AVKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontrollerdelegate
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontrollerdelegate.json'
content_hash: 'sha256:3bac6c214515fc23'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlayerViewControllerDelegate

<sub>Protocol</sub>

A protocol that defines the methods to implement to respond to player view controller events.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
protocol AVPlayerViewControllerDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Dismissing the Player View Controller

- [- playerViewControllerShouldDismiss:](<avplayerviewcontrollerdelegate/playerviewcontrollershoulddismiss(__).md>) — Asks the delegate object whether the player view controller dismisses itself upon request.
- [- playerViewControllerWillBeginDismissalTransition:](<avplayerviewcontrollerdelegate/playerviewcontrollerwillbegindismissaltransition(__).md>) — Tells the delegate when the player view controller is about to start its dismissal transition.
- [- playerViewControllerDidEndDismissalTransition:](<avplayerviewcontrollerdelegate/playerviewcontrollerdidenddismissaltransition(__).md>) — Tells the delegate when the player view controller ends its dismissal transition.

### Responding to Picture in Picture Life Cycle Events

- [- playerViewControllerShouldAutomaticallyDismissAtPictureInPictureStart:](<avplayerviewcontrollerdelegate/playerviewcontrollershouldautomaticallydismissatpictureinpicturestart(__).md>) — Asks the delegate whether the player view controller automatically dismisses itself when Picture in Picture starts.
- [- playerViewControllerWillStartPictureInPicture:](<avplayerviewcontrollerdelegate/playerviewcontrollerwillstartpictureinpicture(__).md>) — Tells the delegate when Picture in Picture is about to start.
- [- playerViewControllerDidStartPictureInPicture:](<avplayerviewcontrollerdelegate/playerviewcontrollerdidstartpictureinpicture(__).md>) — Tells the delegate when Picture in Picture starts.
- [- playerViewController:failedToStartPictureInPictureWithError:](<avplayerviewcontrollerdelegate/playerviewcontroller(__failedtostartpictureinpicturewitherror_).md>) — Tells the delegate when Picture in Picture fails to start.
- [- playerViewControllerWillStopPictureInPicture:](<avplayerviewcontrollerdelegate/playerviewcontrollerwillstoppictureinpicture(__).md>) — Tells the delegate when Picture in Picture is about to stop.
- [- playerViewControllerDidStopPictureInPicture:](<avplayerviewcontrollerdelegate/playerviewcontrollerdidstoppictureinpicture(__).md>) — Tells the delegate when Picture in Picture stops.
- [- playerViewController:restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:](<avplayerviewcontrollerdelegate/playerviewcontroller(__restoreuserinterfaceforpictureinpicturestopwithcompletionhandler_).md>) — Tells the delegate when Picture in Picture is about to stop so you can restore your app’s user interface.

### Responding to Navigation Events

- [- playerViewController:timeToSeekAfterUserNavigatedFromTime:toTime:](<avplayerviewcontrollerdelegate/playerviewcontroller(__timetoseekafterusernavigatedfrom_to_).md>) — Tells the delegate when the user skips, scrubs, or otherwise navigates to a new time and wants to resume playback at the target time.
- [- playerViewController:willResumePlaybackAfterUserNavigatedFromTime:toTime:](<avplayerviewcontrollerdelegate/playerviewcontroller(__willresumeplaybackafterusernavigatedfrom_to_).md>) — Tells the delegate when the user navigates to a new time and playback is about to begin.
- [- skipToPreviousItemForPlayerViewController:](<avplayerviewcontrollerdelegate/skiptopreviousitem(for_).md>) — Tells the delegate when the user requests skipping to the previous item in the timeline.
- [- skipToNextItemForPlayerViewController:](<avplayerviewcontrollerdelegate/skiptonextitem(for_).md>) — Tells the delegate when the user requests skipping to the next item in the timeline.

### Responding to Interstitial Content Playback Events

- [- playerViewController:willPresentInterstitialTimeRange:](<avplayerviewcontrollerdelegate/playerviewcontroller(__willpresent_).md>) — Tells the delegate when the player view controller is about to start playing a range of interstitial content.
- [- playerViewController:didPresentInterstitialTimeRange:](<avplayerviewcontrollerdelegate/playerviewcontroller(__didpresent_).md>) — Tells the delegate when the player view controller finishes playing a range of interstitial content.

### Responding to Content Proposals

- [- playerViewController:shouldPresentContentProposal:](<avplayerviewcontrollerdelegate/playerviewcontroller(__shouldpresent_).md>) — Asks the delegate whether the player view controller presents a content proposal.
- [- playerViewController:didAcceptContentProposal:](<avplayerviewcontrollerdelegate/playerviewcontroller(__didaccept_).md>) — Tells the delegate when the user accepts the proposed content.
- [- playerViewController:didRejectContentProposal:](<avplayerviewcontrollerdelegate/playerviewcontroller(__didreject_).md>) — Tells the delegate when the user rejects the proposed content.

### Responding to Media Selection

- [- playerViewController:didSelectMediaSelectionOption:inMediaSelectionGroup:](<avplayerviewcontrollerdelegate/playerviewcontroller(__didselect_in_).md>) — Tells the delegate when the user selects a media option from a media selection group.

### Responding to Transport Bar Changes

- [- playerViewController:willTransitionToVisibilityOfTransportBar:withAnimationCoordinator:](<avplayerviewcontrollerdelegate/playerviewcontroller(__willtransitiontovisibilityoftransportbar_with_).md>) — Tells the delegate when the transport bar’s visibility is about to change.
- [AVPlayerViewControllerAnimationCoordinator](avplayerviewcontrolleranimationcoordinator.md) — A protocol that defines the methods to implement to synchronize animations with playback controls’ visibility animation.

### Responding to Channel Changes

- [- playerViewController:skipToNextChannel:](<avplayerviewcontrollerdelegate/playerviewcontroller(__skiptonextchannel_).md>) — Tells the delegate when the user wants to skip to the next channel.
- [- playerViewController:skipToPreviousChannel:](<avplayerviewcontrollerdelegate/playerviewcontroller(__skiptopreviouschannel_).md>) — Tells the delegate when the user wants to skip to the previous channel.
- [- nextChannelInterstitialViewControllerForPlayerViewController:](<avplayerviewcontrollerdelegate/nextchannelinterstitialviewcontroller(for_).md>) — Asks the delegate for a view controller that describes the layout of the next channel’s interstitial view.
- [- previousChannelInterstitialViewControllerForPlayerViewController:](<avplayerviewcontrollerdelegate/previouschannelinterstitialviewcontroller(for_).md>) — Asks the delegate for a view controller that describes the layout of the previous channel’s interstitial view.

### Responding to Full-Screen Presentations

- [- playerViewController:willBeginFullScreenPresentationWithAnimationCoordinator:](<avplayerviewcontrollerdelegate/playerviewcontroller(__willbeginfullscreenpresentationwithanimationcoordinator_).md>) — Tells the delegate when the player view controller is about to start full-screen display.
- [- playerViewController:willEndFullScreenPresentationWithAnimationCoordinator:](<avplayerviewcontrollerdelegate/playerviewcontroller(__willendfullscreenpresentationwithanimationcoordinator_).md>) — Tells the delegate when the player view controller is about to end full-screen display.
- [- playerViewController:restoreUserInterfaceForFullScreenExitWithCompletionHandler:](<avplayerviewcontrollerdelegate/playerviewcontroller(__restoreuserinterfaceforfullscreenexitwithcompletionhandler_).md>) — Tells the delegate to restore the app’s user interface after returning from a full-screen presentation.

## See Also

### iOS playback and capture

- [Playing video content in a standard user interface](playing-video-content-in-a-standard-user-interface.md) — Play media full screen, embedded inline, or in a floating Picture in Picture (PiP) window using a player view controller.
- [AVPlayerViewController](avplayerviewcontroller.md) — A view controller that displays content from a player and presents a native user interface to control playback.
- [AVCaptureEventInteraction](avcaptureeventinteraction.md) — An object that registers handlers to respond to capture events from system hardware buttons.
- [AVCaptureEvent](avcaptureevent.md) — An object that describes a user interaction with a system hardware button.
- [AVCaptureEventSound](avcaptureeventsound.md) — A sound object for a capture event.
- [AVInputPickerInteraction](avinputpickerinteraction.md) — Use `AVInputPickerInteraction` to present an input picker.
- [Third-party casting support](third-party-casting-support.md) — Provide custom playback controls for third-party casting services and other media sources.
