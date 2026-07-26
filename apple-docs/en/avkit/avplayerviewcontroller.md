---
title: AVPlayerViewController
framework: AVKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontroller
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller.json'
content_hash: 'sha256:0dec6b87a89e6d3f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlayerViewController

<sub>Class</sub>

A view controller that displays content from a player and presents a native user interface to control playback.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class AVPlayerViewController
```

## Overview

A player view controller makes it simple to add media playback capabilities to your app that match the styling and features of the native system players. Using this object also means that your app automatically adopts the new features and styling of future operating system releases.

> [!important] Important
> The framework doesn’t support subclassing [AVPlayerViewController](avplayerviewcontroller.md).

### Support AirPlay

AirPlay lets users stream media to Apple TV, HomePod, and AirPlay 2-compatible speakers and smart TVs. A player view controller supports AirPlay automatically, but you need to configure your app to enable it. See [Configuring your app for media playback](../avfoundation/configuring-your-app-for-media-playback.md) for more information about configuring your app for background playback.

### Adopt Picture in Picture playback

[AVPlayerViewController](avplayerviewcontroller.md) provides Picture in Picture (PiP) playback in iOS and tvOS. PiP playback lets users minimize the video player to a small floating window so they can perform other activities in the primary app or in another app.

> [!note] Note
> To enable PiP playback in your macOS app, use [AVPlayerView](avplayerview.md).

### Customize the tvOS playback experience

[AVPlayerViewController](avplayerviewcontroller.md) in tvOS brings advanced Siri Remote control features to your app. This support lets users play and navigate your content, and access supporting features like subtitles and alternate audio tracks. This object also provides support for using Siri Remote voice commands, such as “Skip ahead 15 seconds” and “What did they say?”, to control playback of your content.

AVKit for tvOS extends the features of [AVPlayerViewController](avplayerviewcontroller.md) and [AVPlayerItem](../avfoundation/avplayeritem.md) to provide additional ways to navigate and present content. Features unique to the tvOS player user interface include:

- Navigation Marker Groups. A group of navigation markers that allow a viewer to jump between significant events in the media timeline. The most common type of navigation marker group is a chapter list, but you can also create additional or alternative means of navigation — for example, to allow the user to quickly jump between key moments in a recorded sporting event. The player view controller lets the user choose between multiple marker groups for navigating through the media timeline.

Use the [AVNavigationMarkersGroup](avnavigationmarkersgroup.md) class to create and describe navigation markers, then use the [navigationMarkerGroups](../avfoundation/avplayeritem/navigationmarkergroups.md) property to associate marker groups with the current [AVPlayerItem](../avfoundation/avplayeritem.md) object.

- Interstitial Content. Some content might not relate to the main content that your app presents, or might have different presentation requirements. For example, you might not allow the user to skip over advertisements when scrubbing through the playback timeline, or to skip mandatory legal notices.

Use the [AVInterstitialTimeRange](avinterstitialtimerange.md) class to describe interstitial content, and the [interstitialTimeRanges](../avfoundation/avplayeritem/interstitialtimeranges.md) property to associate those time ranges with the current [AVPlayerItem](../avfoundation/avplayeritem.md) object.

- Content Proposals. When presenting serialized content, like a TV show, you often want to propose additional content for the viewer to watch when the current episode ends. It’s straightforward to add this functionality to your app using content proposals.

Use the [AVContentProposal](avcontentproposal.md) class to describe the proposed content, and set it as the [nextContentProposal](../avfoundation/avplayeritem/nextcontentproposal.md) property of the current [AVPlayerItem](../avfoundation/avplayeritem.md) object. You can implement the methods of the player view controller’s [delegate](avplayerviewcontroller/delegate.md) object to prepare to present a content proposal, and perform actions in response to the viewer accepting, rejecting, or deferring the proposal.

## Relationships

- **Inherits From**: [UIViewController](../uikit/uiviewcontroller.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md), [UIAppearanceContainer](../uikit/uiappearancecontainer.md), [UIContentContainer](../uikit/uicontentcontainer.md), [UIFocusEnvironment](../uikit/uifocusenvironment.md), [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md), [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md), [UIStateRestoring](../uikit/uistaterestoring.md), [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md), [UITraitEnvironment](../uikit/uitraitenvironment.md), [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## Topics

### Configuring presentation

- [showsPlaybackControls](avplayerviewcontroller/showsplaybackcontrols.md) — A Boolean value that indicates whether the player view controller shows playback controls.
- [contentOverlayView](avplayerviewcontroller/contentoverlayview.md) — A view that displays between the video content and the playback controls.
- [videoGravity](avplayerviewcontroller/videogravity.md) — A string that specifies how the video displays within the bounds of the view controller’s view.
- [videoBounds](avplayerviewcontroller/videobounds.md) — The size and position of the video image within the bounds of the view controller’s view.
- [showsTimecodes](avplayerviewcontroller/showstimecodes.md) — A Boolean value that determines whether the player view displays timecodes, if available.
- [appliesPreferredDisplayCriteriaAutomatically](avplayerviewcontroller/appliespreferreddisplaycriteriaautomatically.md) — A Boolean value that indicates whether the view controller automatically sets the screen’s display criteria to match that of the currently playing asset.

### Customizing the tvOS player UI

- [playbackControlsIncludeTransportBar](avplayerviewcontroller/playbackcontrolsincludetransportbar.md) — A Boolean value that indicates whether the player shows the transport bar and related controls.
- [playbackControlsIncludeInfoViews](avplayerviewcontroller/playbackcontrolsincludeinfoviews.md) — A Boolean value that indicates whether the player presents video metadata, navigation markers, and playback settings views when the user requests them.
- [transportBarIncludesTitleView](avplayerviewcontroller/transportbarincludestitleview.md) — A Boolean value that indicates whether the player user interface shows the title view above the scrubber.
- [transportBarCustomMenuItems](avplayerviewcontroller/transportbarcustommenuitems.md) — An array of actions and menus to display with the default player controls.
- [customInfoViewControllers](avplayerviewcontroller/custominfoviewcontrollers.md) — An array of view controllers to display as content tabs in the player user interface.
- [infoViewActions](avplayerviewcontroller/infoviewactions.md) — An array of actions to present in the Info content view.
- [contextualActions](avplayerviewcontroller/contextualactions.md) — An array of action controls to present contextually during playback.
- [customOverlayViewController](avplayerviewcontroller/customoverlayviewcontroller.md) — A view controller that presents custom content over the player view.
- [unobscuredContentGuide](avplayerviewcontroller/unobscuredcontentguide.md) — A layout guide that represents an area that fixed-position playback controls don’t obscure when visible.
- [customInfoViewController](avplayerviewcontroller/custominfoviewcontroller.md) — A view controller that provides client-specific content and controls alongside system-provided information and settings panels. _(deprecated)_

### Configuring the visionOS player UI

- [infoViewActions](avplayerviewcontroller/infoviewactions.md) — An array of actions to present in the Info content view.
- [customInfoViewControllers](avplayerviewcontroller/custominfoviewcontrollers.md) — An array of view controllers to display as content tabs in the player user interface.
- [contextualActions](avplayerviewcontroller/contextualactions.md) — An array of action controls to present contextually during playback.
- [contextualActionsInfoView](avplayerviewcontroller/contextualactionsinfoview.md) — A view the system shows adjacent to the contextual actions that’s suitable for showing related information.
- [contextualActionsPreviewImage](avplayerviewcontroller/contextualactionspreviewimage.md) — An image to show alongside the contextual actions.
- [requiresMonoscopicViewingMode](avplayerviewcontroller/requiresmonoscopicviewingmode.md) — A Boolean value that indicates whether to permit playback of 2D video content only.
- [experienceController](avplayerviewcontroller/experiencecontroller.md) — The experience controller for this view controller.
- [groupExperienceCoordinator](avplayerviewcontroller/groupexperiencecoordinator.md) — The group experience coordinator for this view controller.
- [viewport](avplayerviewcontroller/viewport.md) — A configuration object that manages viewport settings for different presentation modes. _(beta)_
- [AVViewport](avviewport.md) — A configuration object that manages viewport settings for different presentation modes. _(beta)_

### Presenting the visionOS trimming UI

- [canBeginTrimming](avplayerviewcontroller/canbegintrimming.md) — A Boolean value that indicates whether the current media supports trimming.
- [- beginTrimmingWithCompletionHandler:](<avplayerviewcontroller/begintrimming(completionhandler_).md>) — Presents the system trimming interface controls inside the player view.

### Configuring frame analysis

- [allowsVideoFrameAnalysis](avplayerviewcontroller/allowsvideoframeanalysis.md) — A Boolean value that indicates whether to perform video frame analysis.
- [toggleLookupAction](avplayerviewcontroller/togglelookupaction.md) — An action that enables the visual lookup interface.
- [videoFrameAnalysisTypes](avplayerviewcontroller/videoframeanalysistypes.md) — The types of analysis a player view controller performs on a paused video frame.
- [AVVideoFrameAnalysisType](avvideoframeanalysistype.md) — Constants that define the types of analysis a player view controller may perform on a paused video frame.

### Configuring playback speed

- [speeds](avplayerviewcontroller/speeds.md) — A list of user-selectable playback speeds to show in the playback speed control.
- [selectedSpeed](avplayerviewcontroller/selectedspeed.md) — The currently selected playback speed.
- [- selectSpeed:](<avplayerviewcontroller/selectspeed(__).md>) — Selects a specified playback speed.
- [AVPlaybackSpeed](avplaybackspeed.md) — An object that represents a user-selectable playback speed in a playback user interface.

### Configuring Picture in Picture

- [allowsPictureInPicturePlayback](avplayerviewcontroller/allowspictureinpictureplayback.md) — A Boolean value that indicates whether the player allows Picture in Picture playback.
- [canStartPictureInPictureAutomaticallyFromInline](avplayerviewcontroller/canstartpictureinpictureautomaticallyfrominline.md) — A Boolean value that indicates whether Picture in Picture starts automatically when transitioning to the background when the view controller presents its content inline.

### Managing full-screen behavior

- [entersFullScreenWhenPlaybackBegins](avplayerviewcontroller/entersfullscreenwhenplaybackbegins.md) — A Boolean value that determines whether the player automatically displays in full screen when the user taps the play button.
- [exitsFullScreenWhenPlaybackEnds](avplayerviewcontroller/exitsfullscreenwhenplaybackends.md) — A Boolean value that indicates whether the player exits full-screen mode when playback ends.

### Managing subtitles

- [allowedSubtitleOptionLanguages](avplayerviewcontroller/allowedsubtitleoptionlanguages.md) — An array of language codes that restrict the set of subtitle languages available to the user.
- [requiresFullSubtitles](avplayerviewcontroller/requiresfullsubtitles.md) — A Boolean value that indicates whether the user can disable the display of subtitles.
- [mediaCharacteristicsForSupportedCustomMediaSelectionSchemes](avplayerviewcontroller/mediacharacteristicsforsupportedcustommediaselectionschemes.md)

### Preventing navigation

- [requiresLinearPlayback](avplayerviewcontroller/requireslinearplayback.md) — A Boolean value that determines whether the player allows the user to skip media content.

### Configuring skipping behavior

- [skipForwardEnabled](avplayerviewcontroller/isskipforwardenabled.md) — A Boolean value that indicates whether forward-skipping is available.
- [skipBackwardEnabled](avplayerviewcontroller/isskipbackwardenabled.md) — A Boolean value that indicates whether backward-skipping is available.
- [skippingBehavior](avplayerviewcontroller/skippingbehavior.md) — The behavior that skipping gestures perform.
- [AVPlayerViewControllerSkippingBehavior](avplayerviewcontrollerskippingbehavior.md) — Constants that represent the player view controller’s skipping behavior.

### Determining display readiness

- [readyForDisplay](avplayerviewcontroller/isreadyfordisplay.md) — A Boolean value that indicates whether the player item’s first video frame is ready for display.

### Updating Now Playing information

- [updatesNowPlayingInfoCenter](avplayerviewcontroller/updatesnowplayinginfocenter.md) — A Boolean value that indicates whether the view controller updates Now Playing information.

### Proposing additional content

- [contentProposalViewController](avplayerviewcontroller/contentproposalviewcontroller.md) — The view controller responsible for the presentation of content proposals.

### Accessing the player

- [player](avplayerviewcontroller/player.md) — The player object that provides the media content for the view controller to display.

### Accessing the delegate object

- [delegate](avplayerviewcontroller/delegate.md) — The delegate object for the player view controller.

### Configuring pixel buffers

- [pixelBufferAttributes](avplayerviewcontroller/pixelbufferattributes.md) — The pixel buffer attributes of the video frames the view controller presents.

### High dynamic range

- [preferredDisplayDynamicRange](avplayerviewcontroller/preferreddisplaydynamicrange.md) — Describes how High Dynamic Range (HDR) video content renders.
- [AVDisplayDynamicRange](avdisplaydynamicrange.md) — Describes how High Dynamic Range (HDR) video content renders.

## See Also

### iOS playback and capture

- [Playing video content in a standard user interface](playing-video-content-in-a-standard-user-interface.md) — Play media full screen, embedded inline, or in a floating Picture in Picture (PiP) window using a player view controller.
- [AVPlayerViewControllerDelegate](avplayerviewcontrollerdelegate.md) — A protocol that defines the methods to implement to respond to player view controller events.
- [AVCaptureEventInteraction](avcaptureeventinteraction.md) — An object that registers handlers to respond to capture events from system hardware buttons.
- [AVCaptureEvent](avcaptureevent.md) — An object that describes a user interaction with a system hardware button.
- [AVCaptureEventSound](avcaptureeventsound.md) — A sound object for a capture event.
- [AVInputPickerInteraction](avinputpickerinteraction.md) — Use `AVInputPickerInteraction` to present an input picker.
- [Third-party casting support](third-party-casting-support.md) — Provide custom playback controls for third-party casting services and other media sources.
