---
title: AVPlayerItem
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem.json'
content_hash: 'sha256:a7518ed5dd1e69f0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerItem

<sub>Class</sub>

An object that models the timing and presentation state of an asset during playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor class AVPlayerItem
```

## Overview

A player item stores a reference to an [AVAsset](avasset.md) object, which represents the media to play. If you require inspecting an asset before you enqueue it for playback, call its [load(_:isolation:)](<avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the values of one or more properties. Alternatively, you can tell the player item to automatically load the required properties by passing them to its [init(asset:automaticallyLoadedAssetKeys:)](<avplayeritem/init(asset_automaticallyloadedassetkeys_)-5czjh.md>) initializer. When the player item is ready to play, the asset properties you request are ready to use.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [AVMetricEventStreamPublisher](avmetriceventstreampublisher.md), [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Observable](../observation/observable.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a player item

- [- initWithURL:](<avplayeritem/init(url_)-1xrtk.md>) — Creates a player item with a specified URL.
- [- initWithAsset:](<avplayeritem/init(asset_)-87rjl.md>) — Creates a player item for a specified asset.
- [init(asset:)](<avplayeritem/init(asset_)-1nme9.md>)
- [init(asset:automaticallyLoadedAssetKeys:)](<avplayeritem/init(asset_automaticallyloadedassetkeys_)-5czjh.md>) — Creates a player item for the asset, and automatically loads values for the specified properties.
- [init(asset:automaticallyLoadedAssetKeys:)](<avplayeritem/init(asset_automaticallyloadedassetkeys_)-85hal.md>)
- [- initWithAsset:automaticallyLoadedAssetKeys:](<avplayeritem/init(asset_automaticallyloadedassetkeys_)-8x4.md>) — Creates a player item with the specified asset and the asset keys to automatically load.

### Accessing tracks

- [tracks](avplayeritem/tracks.md) — An array of player item track objects.

### Accessing metadata

- [externalMetadata](avplayeritem/externalmetadata.md) — An array of additional metadata for the player item to supplement or replace an asset’s embedded metadata.

### Determining readiness

- [status](avplayeritem/status-swift.property.md) — The status of the player item.
- [Status](avplayeritem/status-swift.enum.md) — The statuses for a player item.
- [error](avplayeritem/error.md) — The error that caused the player item to fail.

### Determining playback capabilities

- [canPlayReverse](avplayeritem/canplayreverse.md) — A Boolean value that indicates whether the item can play in reverse.
- [canPlayFastForward](avplayeritem/canplayfastforward.md) — A Boolean value that indicates whether the item can be fast forwarded.
- [canPlayFastReverse](avplayeritem/canplayfastreverse.md) — A Boolean value that indicates whether the item can be quickly reversed.
- [canPlaySlowForward](avplayeritem/canplayslowforward.md) — A Boolean value that indicates whether the item can play slower than normal.
- [canPlaySlowReverse](avplayeritem/canplayslowreverse.md) — A Boolean value that indicates whether the item can play slowly backward.

### Setting playback boundaries

- [forwardPlaybackEndTime](avplayeritem/forwardplaybackendtime.md) — The time at which forward playback ends.
- [reversePlaybackEndTime](avplayeritem/reverseplaybackendtime.md) — The time at which reverse playback ends.

### Stepping through media

- [canStepForward](avplayeritem/canstepforward.md) — A Boolean value that indicates whether the item supports stepping forward.
- [canStepBackward](avplayeritem/canstepbackward.md) — A Boolean value that indicates whether the item supports stepping backward.
- [- stepByCount:](<avplayeritem/step(bycount_).md>) — Moves the player item’s current time forward or backward by a specified number of steps.

### Seeking through media

- [- seekToTime:completionHandler:](<avplayeritem/seek(to_completionhandler_)-91gnw.md>) — Sets the current playback time to the specified time.
- [- seekToTime:toleranceBefore:toleranceAfter:completionHandler:](<avplayeritem/seek(to_tolerancebefore_toleranceafter_completionhandler_).md>) — Sets the current playback time within a specified time bound and invokes the specified block when the seek operation completes or is interrupted.
- [- seekToDate:completionHandler:](<avplayeritem/seek(to_completionhandler_)-1dibq.md>) — Sets the current playback time to the time specified by the date object.
- [- cancelPendingSeeks](<avplayeritem/cancelpendingseeks().md>) — Cancels any pending seek requests and invokes the corresponding completion handlers if present.

### Selecting media options

- [- selectMediaPresentationSetting:forMediaSelectionGroup:](<avplayeritem/select(__for_).md>) — When the associated AVPlayer’s appliesMediaSelectionCriteriaAutomatically property is set to YES, configures the player item to prefer a particular presentation setting, replacing any previous preference for settings of the same media presentation selector.
- [preferredCustomMediaSelectionSchemes](avplayeritem/preferredcustommediaselectionschemes.md) — Indicates the AVCustomMediaSelectionSchemes of AVMediaSelectionGroups of the receiver’s asset with which an associated UI implementation should configure its interface for media selection.
- [- effectiveMediaPresentationSettingsForMediaSelectionGroup:](<avplayeritem/effectivemediapresentationsettings(for_).md>) — Indicates the media presentation settings with media characteristics that are possessed by the currently selected AVMediaSelectionOption in the specified AVMediaSelectionGroup.
- [- selectMediaPresentationLanguage:forMediaSelectionGroup:](<avplayeritem/selectmediapresentationlanguage(__for_).md>) — When the associated AVPlayer’s appliesMediaSelectionCriteriaAutomatically property is set to YES, configures the player item to prefer a particular language, replacing any previous preference for available languages of the specified group’s custom media selection scheme.
- [- selectedMediaPresentationLanguageForMediaSelectionGroup:](<avplayeritem/selectedmediapresentationlanguage(for_).md>) — Returns the selected media presentation language for the specified media selection group, if any language has previously been selected via use of -selectMediaPresentationLanguages:forMediaSelectionGroup:.
- [- selectedMediaPresentationSettingsForMediaSelectionGroup:](<avplayeritem/selectedmediapresentationsettings(for_).md>) — Indicates the media presentation settings that have most recently been selected for each AVMediaPresentationSelector of the AVCustomMediaSelectionScheme of the specified AVMediaSelectionGroup.
- [currentMediaSelection](avplayeritem/currentmediaselection.md) — The current media selections for each of the receiver’s media selection groups.
- [- selectMediaOption:inMediaSelectionGroup:](<avplayeritem/select(__in_).md>) — Selects a media option in a given media selection group and deselects all other options in that group.
- [- selectMediaOptionAutomaticallyInMediaSelectionGroup:](<avplayeritem/selectmediaoptionautomatically(in_).md>) — Selects the media option in the specified media selection group that best matches the receiver’s automatic selection criteria.

### Setting variant behavior

- [variantPreferences](avplayeritem/variantpreferences.md) — The preferences the player item uses when selecting variant playlists.
- [AVVariantPreferences](avvariantpreferences.md) — Defines the preferences the player item uses when selecting variant playlists.
- [startsOnFirstEligibleVariant](avplayeritem/startsonfirsteligiblevariant.md) — A Boolean value that indicates whether playback starts with the first eligible variant that appears in the stream’s main playlist.

### Configuring interstitial events

- [integratedTimeline](avplayeritem/integratedtimeline.md) — An integrated timeline that represents the player item timing including its scheduled interstitial events.
- [automaticallyHandlesInterstitialEvents](avplayeritem/automaticallyhandlesinterstitialevents.md) — A Boolean value that indicates whether the player item automatically plays interstitial events according to server-side directives.
- [translatesPlayerInterstitialEvents](avplayeritem/translatesplayerinterstitialevents.md) — A Boolean value that indicates whether the player translates interstitial events to interstitial time ranges.
- [interstitialTimeRanges](avplayeritem/interstitialtimeranges.md) — An array of time ranges that identify interstitial content.
- [templatePlayerItem](avplayeritem/template.md) — The template player item that initializes this instance.

### Accessing timing information

- [- currentTime](<avplayeritem/currenttime().md>) — Returns the current time of the item.
- [- currentDate](<avplayeritem/currentdate().md>) — Returns the current time of the item as a date.
- [duration](avplayeritem/duration.md) — The duration of the item.
- [timebase](avplayeritem/timebase.md) — The timebase information for the item.

### Determining available time ranges

- [loadedTimeRanges](avplayeritem/loadedtimeranges.md) — An array of time ranges indicating media data that is readily available.
- [seekableTimeRanges](avplayeritem/seekabletimeranges.md) — An array of time ranges within which it is possible to seek.

### Determining buffering status

- [playbackLikelyToKeepUp](avplayeritem/isplaybacklikelytokeepup.md) — A Boolean value that indicates whether the item will likely play through without stalling.
- [playbackBufferFull](avplayeritem/isplaybackbufferfull.md) — A Boolean value that indicates whether the internal media buffer is full and that further I/O is suspended.
- [playbackBufferEmpty](avplayeritem/isplaybackbufferempty.md) — A Boolean value that indicates whether playback has consumed all buffered media and that playback will stall or end.

### Configuring expensive network behavior

- [preferredPeakBitRateForExpensiveNetworks](avplayeritem/preferredpeakbitrateforexpensivenetworks.md) — A limit of network bandwidth consumption by the item when connecting over expensive networks.
- [preferredMaximumResolutionForExpensiveNetworks](avplayeritem/preferredmaximumresolutionforexpensivenetworks.md) — An upper limit on the resolution of video to download when connecting over expensive networks.

### Accessing text style rules

- [textStyleRules](avplayeritem/textstylerules.md) — An array of text style rules that specify the formatting and presentation of Web Video Text Tracks (WebVTT) subtitles.
- [AVTextStyleRule](avtextstylerule.md) — An object that represents the text styling rules to apply to a media item’s textual content.

### Accessing logging information

- [- accessLog](<avplayeritem/accesslog().md>) — Returns an object that represents a snapshot of the network access log. _(deprecated)_
- [AVPlayerItemAccessLog](avplayeritemaccesslog.md) — An object used to retrieve the access log associated with a player item.
- [AVPlayerItemAccessLogEvent](avplayeritemaccesslogevent.md) — A single entry in a player item’s access log.
- [- errorLog](<avplayeritem/errorlog().md>) — Returns an object that represents a snapshot of the error log. _(deprecated)_
- [AVPlayerItemErrorLog](avplayeritemerrorlog.md) — The error log associated with a player item.
- [AVPlayerItemErrorLogEvent](avplayeritemerrorlogevent.md) — A single item in a player item’s error log.

### Observing notifications

- [AVPlayerItemDidPlayToEndTimeNotification](avplayeritem/didplaytoendtimenotification.md) — A notification the system posts when a player item plays to its end time.
- [AVPlayerItemFailedToPlayToEndTimeNotification](avplayeritem/failedtoplaytoendtimenotification.md) — A notification that the system posts when a player item fails to play to its end time.
- [AVPlayerItemTimeJumpedNotification](avplayeritem/timejumpednotification.md) — A notification the system posts when a player item’s time changes discontinuously.
- [AVPlayerItemPlaybackStalledNotification](avplayeritem/playbackstallednotification.md) — A notification the system posts when a player item media doesn’t arrive in time to continue playback.
- [AVPlayerItemMediaSelectionDidChangeNotification](avplayeritem/mediaselectiondidchangenotification.md) — A notification the player item posts when its media selection changes.
- [AVPlayerItemRecommendedTimeOffsetFromLiveDidChangeNotification](avplayeritem/recommendedtimeoffsetfromlivedidchangenotification.md) — A notification the player item posts when its offset from the live time changes.
- [AVPlayerItemNewAccessLogEntryNotification](avplayeritem/newaccesslogentrynotification.md) — A notification the system posts when a player item adds a new entry to its access log.
- [AVPlayerItemNewErrorLogEntryNotification](avplayeritem/newerrorlogentrynotification.md) — A notification the system posts when a player item adds a new entry to its error log.

### Managing time offsets

- [automaticallyPreservesTimeOffsetFromLive](avplayeritem/automaticallypreservestimeoffsetfromlive.md) — A Boolean value that indicates whether the player preserves its time offset from the live time after a buffering operation.
- [recommendedTimeOffsetFromLive](avplayeritem/recommendedtimeoffsetfromlive.md) — A recommended time offset from the live time based on observed network conditions.
- [configuredTimeOffsetFromLive](avplayeritem/configuredtimeoffsetfromlive.md) — A time value that indicates the offset from the live time to start playback, or resume playback after a seek to positive infinity.

### Configuring presentation

- [presentationSize](avplayeritem/presentationsize.md) — The size at which the visual portion of the item is presented by the player.
- [preferredMaximumResolution](avplayeritem/preferredmaximumresolution.md) — The desired maximum resolution of a video that is to be downloaded.
- [videoApertureMode](avplayeritem/videoaperturemode.md) — The video aperture mode to apply during playback.
- [AVVideoApertureMode](avvideoaperturemode.md) — A value that describes how a video is scaled or cropped.

### Accessing Now Playing information

- [nowPlayingInfo](avplayeritem/nowplayinginfo.md) — The current now playing information for the player item.

### Configuring HDR settings

- [appliesPerFrameHDRDisplayMetadata](avplayeritem/appliesperframehdrdisplaymetadata.md) — A Boolean value that indicates whether the player item applies per-frame HDR display metadata during playback.

### Configuring video compositing

- [videoComposition](avplayeritem/videocomposition.md) — The video composition settings to be applied during playback.
- [customVideoCompositor](avplayeritem/customvideocompositor.md) — The custom video compositor.
- [seekingWaitsForVideoCompositionRendering](avplayeritem/seekingwaitsforvideocompositionrendering.md) — A Boolean value that indicates whether the item’s timing follows the displayed video frame when seeking with a video composition.

### Configuring audio

- [audioMix](avplayeritem/audiomix.md) — The audio mix parameters to be applied during playback.
- [audioTimePitchAlgorithm](avplayeritem/audiotimepitchalgorithm.md) — The processing algorithm used to manage audio pitch for scaled audio edits.
- [allowedAudioSpatializationFormats](avplayeritem/allowedaudiospatializationformats.md) — The source audio channel layouts the player item supports for spatialization.
- [AVAudioSpatializationFormats](avaudiospatializationformats.md) — A structure that defines the spatialization formats that a player item supports.
- [audioSpatializationAllowed](avplayeritem/isaudiospatializationallowed.md) — A Boolean value that indicates whether the player item allows spatialized audio playback. _(deprecated)_

### Managing player item outputs

- [outputs](avplayeritem/outputs.md) — An array of outputs associated with the player item.
- [- addOutput:](<avplayeritem/add(__)-16ctk.md>) — Adds the specified player item output object to the receiver.
- [- removeOutput:](<avplayeritem/remove(__)-46b1r.md>) — Removes the specified player item output object from the receiver.

### Managing player item data collectors

- [mediaDataCollectors](avplayeritem/mediadatacollectors.md) — The collection of associated media data collectors.
- [- addMediaDataCollector:](<avplayeritem/add(__)-9l3to.md>) — Adds the specified media data collector to the player item’s collection of media collectors.
- [- removeMediaDataCollector:](<avplayeritem/remove(__)-29iuz.md>) — Removes the specified media data collector from the player item’s collection of media collectors.

### Configuring network behavior

- [preferredPeakBitRate](avplayeritem/preferredpeakbitrate.md) — The desired limit, in bits per second, of network bandwidth consumption for this item.
- [preferredForwardBufferDuration](avplayeritem/preferredforwardbufferduration.md) — The duration the player should buffer media from the network ahead of the playhead to guard against playback disruption.
- [canUseNetworkResourcesForLiveStreamingWhilePaused](avplayeritem/canusenetworkresourcesforlivestreamingwhilepaused.md) — A Boolean value that indicates whether the player item can use network resources to keep the playback state up to date while paused.

### Configuring player items for AVKit

- [navigationMarkerGroups](avplayeritem/navigationmarkergroups.md) — The time marker groups that provide ways to navigate the player item’s content.
- [nextContentProposal](avplayeritem/nextcontentproposal.md) — The item proposed to follow the current content.

### Requesting playback authorization in tvOS

- [- requestPlaybackRestrictionsAuthorization:](<avplayeritem/requestplaybackrestrictionsauthorization(__).md>) — Determines whether this item is subject to parental restrictions, and, if so, prompts the user to enter the restrictions passcode.
- [- cancelPlaybackRestrictionsAuthorizationRequest](<avplayeritem/cancelplaybackrestrictionsauthorizationrequest().md>) — Cancels a pending authorization request and dismisses the passcode entry, if displayed.

### Managing playback authorization in macOS

- [contentAuthorizedForPlayback](avplayeritem/iscontentauthorizedforplayback.md) — A Boolean value that indicates whether the content has been authorized by the user.
- [authorizationRequiredForPlayback](avplayeritem/isauthorizationrequiredforplayback.md) — A Boolean value that indicates whether authorization is required to play the content.
- [applicationAuthorizedForPlayback](avplayeritem/isapplicationauthorizedforplayback.md) — A Boolean value that indicates whether the application can be used to play the content.
- [- requestContentAuthorizationAsynchronouslyWithTimeoutInterval:completionHandler:](<avplayeritem/requestcontentauthorizationasynchronously(withtimeoutinterval_completionhandler_).md>) — Presents the user the opportunity to authorize the content for playback.
- [contentAuthorizationRequestStatus](avplayeritem/contentauthorizationrequeststatus.md) — The status of the most recent content authorization request.
- [AVContentAuthorizationStatus](avcontentauthorizationstatus.md) — A value representing the status of a content authorization request.
- [- cancelContentAuthorizationRequest](<avplayeritem/cancelcontentauthorizationrequest().md>) — Cancels the currently outstanding content authorization request.

### Accessing initialization parameters

- [asset](avplayeritem/asset.md) — The asset provided during initialization.
- [automaticallyLoadedAssetKeys](avplayeritem/automaticallyloadedassetkeys.md) — The array of asset keys to be automatically loaded before the player item is ready to play.

### Copying an player item

- [- copy](<avplayeritem/copy().md>) — Creates a copy of the object.
- [- copyWithZone:](<avplayeritem/copy(with_).md>) — Creates a copy of the object with the specified zone.

### Deprecated

- [Deprecated symbols](avplayeritem-deprecated-symbols.md) — Review unsupported symbols and their replacements.

### Initializers

- [init(URL:)](<avplayeritem/init(url_)-5rssp.md>)
- [init(URL:)](<avplayeritem/init(url_)-91z05.md>)

### Instance Properties

- [interstitialEventIdentifier](avplayeritem/interstitialeventidentifier.md) — The identifier of the AVPlayerInterstitialEvent that created this item, or nil if the item was not created from an interstitial event.

### Instance Methods

- [- fetchAccessLogWithCompletionHandler:](<avplayeritem/fetchaccesslog(completionhandler_).md>) — Asynchronously retrieves the access log without blocking the calling thread. _(beta)_
- [- fetchErrorLogWithCompletionHandler:](<avplayeritem/fetcherrorlog(completionhandler_).md>) — Asynchronously retrieves the error log without blocking the calling thread. _(beta)_
- [- selectableMediaSelectionOptionsInMediaSelectionGroup:](<avplayeritem/selectablemediaselectionoptions(in_).md>) — Returns the media selection options in the specified media selection group that can produce content. _(beta)_

## See Also

### Playback control

- [Observing playback state in SwiftUI](observing-playback-state-in-swiftui.md) — Keep your user interface in sync with state changes from playback objects.
- [Controlling the transport behavior of a player](controlling-the-transport-behavior-of-a-player.md) — Play, pause, and seek through a media presentation.
- [Creating a seamless multiview playback experience](creating-a-seamless-multiview-playback-experience.md) — Build advanced multiview playback experiences with the AVFoundation and AVRouting frameworks.
- [AVPlayer](avplayer.md) — An object that provides the interface to control the player’s transport behavior.
- [AVPlayerItemTrack](avplayeritemtrack.md) — An object that represents the presentation state of an asset track during playback.
- [AVQueuePlayer](avqueueplayer.md) — An object that plays a sequence of player items.
- [AVPlayerLooper](avplayerlooper.md) — An object that loops media content using a queue player.
