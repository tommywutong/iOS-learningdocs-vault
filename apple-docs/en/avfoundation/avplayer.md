---
title: AVPlayer
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer.json'
content_hash: 'sha256:e01d93afb5e38097'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayer

<sub>Class</sub>

An object that provides the interface to control the player’s transport behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor class AVPlayer
```

## Overview

A player is a controller object that manages the playback and timing of a media asset. Use an instance of [AVPlayer](avplayer.md) to play local and remote file-based media, such as QuickTime movies and MP3 audio files, as well as audiovisual media served using HTTP Live Streaming.

Use a player object to play a single media asset. You can reuse the player instance to play additional media assets using its [- replaceCurrentItemWithPlayerItem:](<avplayer/replacecurrentitem(with_).md>) method, but it manages the playback of only a single media asset at a time. The framework also provides a subclass called [AVQueuePlayer](avqueueplayer.md) that you can use to manage the playback of a queue of media assets.

You use an [AVPlayer](avplayer.md) to play media assets, which AVFoundation represents using the [AVAsset](avasset.md) class. [AVAsset](avasset.md) only models the _static_ aspects of the media, such as its duration or creation date, and on its own, isn’t suitable for playback with an [AVPlayer](avplayer.md). To play an asset, you create an instance of its _dynamic_ counterpart found in [AVPlayerItem](avplayeritem.md). This object models the timing and presentation state of an asset played by an instance of [AVPlayer](avplayer.md). See the [AVPlayerItem](avplayeritem.md) reference for more details.

[AVPlayer](avplayer.md) is a dynamic object whose state continuously changes. There are two approaches you can use to observe a player’s state:

- **General State Observations:** You can use key-value observing (KVO) to observe state changes to many of the player’s dynamic properties, such as its [currentItem](avplayer/currentitem.md) or its playback [rate](avplayer/rate.md).
- **Timed State Observations:** KVO works well for general state observations, but isn’t intended for observing continuously changing state like the player’s time. [AVPlayer](avplayer.md) provides two methods to observe time changes:
- [- addPeriodicTimeObserverForInterval:queue:usingBlock:](<avplayer/addperiodictimeobserver(forinterval_queue_using_).md>)
- [- addBoundaryTimeObserverForTimes:queue:usingBlock:](<avplayer/addboundarytimeobserver(fortimes_queue_using_).md>)

These methods let you observe time changes either periodically or by boundary, respectively. As changes occur, invoke the callback block or closure you supply to these methods to give you the opportunity to take some action such as updating the state of your player’s user interface.

[AVPlayer](avplayer.md) and [AVPlayerItem](avplayeritem.md) are nonvisual objects, meaning that on their own they’re unable to present an asset’s video onscreen. There are two primary approaches you use to present your video content onscreen:

- **AVKit:** The best way to present your video content is with the AVKit framework’s [AVPlayerViewController](../avkit/avplayerviewcontroller.md) class in iOS and tvOS, or the [AVPlayerView](../avkit/avplayerview.md) class in macOS. These classes present the video content, along with playback controls and other media features giving you a full-featured playback experience.
- **AVPlayerLayer:** When building a custom interface for your player, use [AVPlayerLayer](avplayerlayer.md). You can set this layer a view’s backing layer or add it directly to the layer hierarchy. Unlike [AVPlayerView](../avkit/avplayerview.md) and [AVPlayerViewController](../avkit/avplayerviewcontroller.md), a player layer doesn’t present any playback controls—it only presents the visual content onscreen. It’s up to you to build the playback transport controls to play, pause, and seek through the media.

Alongside the visual content presented with AVKit or [AVPlayerLayer](avplayerlayer.md), you can also present animated content synchronized with the player’s timing using [AVSynchronizedLayer](avsynchronizedlayer.md). Use a synchronized layer pass along player timing to its layer subtree. You can use [AVSynchronizedLayer](avsynchronizedlayer.md) to build custom effects in Core Animation, such as animated lower thirds or video transitions, and have them play in sync with the timing of the player’s current [AVPlayerItem](avplayeritem.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVQueuePlayer](avqueueplayer.md)

- **Conforms To**: [AVRoutingPlaybackParticipant](../avrouting/avroutingplaybackparticipant.md), [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Observable](../observation/observable.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a player

- [- initWithURL:](<avplayer/init(url_)-87cxx.md>) — Creates a new player to play a single audiovisual resource referenced by a given URL.
- [- initWithPlayerItem:](<avplayer/init(playeritem_).md>) — Creates a new player to play the specified player item.
- [- init](<avplayer/init().md>) — Creates a player object.

### Managing the player item

- [currentItem](avplayer/currentitem.md) — The item for which the player is currently controlling playback.
- [- replaceCurrentItemWithPlayerItem:](<avplayer/replacecurrentitem(with_).md>) — Replaces the current item with a new item.

### Determining player readiness

- [status](avplayer/status-swift.property.md) — A value that indicates the readiness of a player object for playback.
- [Status](avplayer/status-swift.enum.md) — Status values that indicate whether a player can successfully play media.
- [error](avplayer/error.md) — An error that caused a failure.

### Controlling playback

- [defaultRate](avplayer/defaultrate.md) — A default rate at which to begin playback.
- [- play](<avplayer/play().md>) — Begins playback of the current item.
- [- pause](<avplayer/pause().md>) — Pauses playback of the current item.
- [rate](avplayer/rate.md) — The current playback rate.
- [AVPlayerRateDidChangeNotification](avplayer/ratedidchangenotification.md) — A notification that a player posts when its rate changes.
- [AVPlayerRateDidChangeReasonPlayheadReachedLiveEdge](avplayer/ratedidchangereason/playheadreachedliveedge.md) — Indicates that the player automatically switched the playback rate from \> 1.0 back to 1.0 when the playhead reached the live edge during live streaming.
- [AVPlayerRateDidChangeReasonReversePlaybackReachedStartOfSeekableRange](avplayer/ratedidchangereason/reverseplaybackreachedstartofseekablerange.md) — Indicates that the player automatically switched rate to 1.0 when the reverse playback reached start of seekable range. only for live.

### Observing playback time

- [- currentTime](<avplayer/currenttime().md>) — Returns the current time of the current player item.
- [- addPeriodicTimeObserverForInterval:queue:usingBlock:](<avplayer/addperiodictimeobserver(forinterval_queue_using_).md>) — Requests the periodic invocation of a given block during playback to report changing time.
- [- addBoundaryTimeObserverForTimes:queue:usingBlock:](<avplayer/addboundarytimeobserver(fortimes_queue_using_).md>) — Requests the invocation of a block when specified times are traversed during normal playback.
- [- removeTimeObserver:](<avplayer/removetimeobserver(__).md>) — Cancels a previously registered periodic or boundary time observer.

### Seeking through media

- [- seekToTime:](<avplayer/seek(to_)-87h2r.md>) — Requests that the player seek to a specified time.
- [- seekToTime:completionHandler:](<avplayer/seek(to_completionhandler_)-75bls.md>) — Requests that the player seek to a specified time, and to notify you when the seek is complete.
- [- seekToTime:toleranceBefore:toleranceAfter:](<avplayer/seek(to_tolerancebefore_toleranceafter_).md>) — Requests that the player seek to a specified time with the amount of accuracy specified by the time tolerance values.
- [- seekToTime:toleranceBefore:toleranceAfter:completionHandler:](<avplayer/seek(to_tolerancebefore_toleranceafter_completionhandler_).md>) — Requests that the player seek to a specified time with the amount of accuracy specified by the time tolerance values, and to notify you when the seek is complete.
- [- seekToDate:](<avplayer/seek(to_)-9h9qr.md>) — Requests that the player seek to a specified date.
- [- seekToDate:completionHandler:](<avplayer/seek(to_completionhandler_)-wr1l.md>) — Requests that the player seek to a specified date, and to notify you when the seek is complete.

### Configuring waiting behavior

- [automaticallyWaitsToMinimizeStalling](avplayer/automaticallywaitstominimizestalling.md) — A Boolean value that indicates whether the player should automatically delay playback in order to minimize stalling.
- [reasonForWaitingToPlay](avplayer/reasonforwaitingtoplay.md) — The reason the player is currently waiting for playback to begin or resume.
- [WaitingReason](avplayer/waitingreason.md) — The reasons a player is waiting to begin or resume playback.
- [timeControlStatus](avplayer/timecontrolstatus-swift.property.md) — A value that indicates whether playback is in progress, paused indefinitely, or waiting for network conditions to improve.
- [TimeControlStatus](avplayer/timecontrolstatus-swift.enum.md) — Constants that indicate the state of playback control.
- [- playImmediatelyAtRate:](<avplayer/playimmediately(atrate_).md>) — Plays the available media data immediately, at the specified rate.

### Responding when playback ends

- [actionAtItemEnd](avplayer/actionatitemend-swift.property.md) — The action to perform when the current player item has finished playing.
- [ActionAtItemEnd](avplayer/actionatitemend-swift.enum.md) — The actions a player can take when it finishes playing.

### Configuring media selection criteria

- [appliesMediaSelectionCriteriaAutomatically](avplayer/appliesmediaselectioncriteriaautomatically.md) — A Boolean value that indicates whether the receiver should apply the current selection criteria automatically to player items.
- [- mediaSelectionCriteriaForMediaCharacteristic:](<avplayer/mediaselectioncriteria(formediacharacteristic_).md>) — Returns the automatic selection criteria for media items with the specified media characteristic.
- [- setMediaSelectionCriteria:forMediaCharacteristic:](<avplayer/setmediaselectioncriteria(__formediacharacteristic_).md>) — Applies automatic selection criteria for media that has the specified media characteristic.

### Accessing player output

- [videoOutput](avplayer/videooutput.md) — The video output for this player.

### Configuring audio behavior

- [volume](avplayer/volume.md) — The audio playback volume for the player.
- [muted](avplayer/ismuted.md) — A Boolean value that indicates whether the audio output of the player is muted.
- [allowedAudioSpatializationFormats](avplayeritem/allowedaudiospatializationformats.md) — The source audio channel layouts the player item supports for spatialization.
- [audioSpatializationAllowed](avplayeritem/isaudiospatializationallowed.md) — A Boolean value that indicates whether the player item allows spatialized audio playback. _(deprecated)_
- [audioOutputSuppressedDueToNonMixableAudioRoute](avplayer/audiooutputsuppressedduetononmixableaudioroute.md) — Whether the player’s audio output is suppressed due to being on a non-mixable audio route.
- [intendedSpatialAudioExperience](avplayer/intendedspatialaudioexperience-1bd87.md) — The player’s intended Spatial Audio experience.

### Configuring background playback

- [audiovisualBackgroundPlaybackPolicy](avplayer/audiovisualbackgroundplaybackpolicy.md) — A policy that determines how playback of audiovisual media continues when the app transitions to the background.
- [AVPlayerAudiovisualBackgroundPlaybackPolicy](avplayeraudiovisualbackgroundplaybackpolicy.md) — Policies that describe playback behavior when an app transitions to the background while playing video.

### Managing external playback

- [allowsExternalPlayback](avplayer/allowsexternalplayback.md) — A Boolean value that indicates whether the player allows switching to external playback mode.
- [externalPlaybackActive](avplayer/isexternalplaybackactive.md) — A Boolean value that indicates whether the player is currently playing video in external playback mode.
- [usesExternalPlaybackWhileExternalScreenIsActive](avplayer/usesexternalplaybackwhileexternalscreenisactive.md) — A Boolean value that indicates whether the player should automatically switch to external playback mode while the external screen mode is active.
- [externalPlaybackVideoGravity](avplayer/externalplaybackvideogravity.md) — The video gravity of the player for external playback mode only.

### Determining HDR playback eligibility

- [eligibleForHDRPlayback](avplayer/eligibleforhdrplayback.md) — A Boolean value that indicates whether the current device can present content to an HDR display.
- [availableHDRModes](avplayer/availablehdrmodes.md) — The HDR modes that are available for playback. _(deprecated)_
- [HDRMode](avplayer/hdrmode.md) — A bitfield type that specifies an HDR mode. _(deprecated)_
- [AVPlayerEligibleForHDRPlaybackDidChangeNotification](avplayer/eligibleforhdrplaybackdidchangenotification.md) — A notification that’s posted whenever HDR playback eligibility changes.

### Coordinating playback

- [playbackCoordinator](avplayer/playbackcoordinator.md) — The playback coordinator for the player.

### Synchronizing multiple players

- [- setRate:time:atHostTime:](<avplayer/setrate(__time_athosttime_).md>) — Synchronizes the playback rate and time of the current item with an external source.
- [- prerollAtRate:completionHandler:](<avplayer/preroll(atrate_completionhandler_).md>) — Begins loading media data to prime the media pipelines for playback.
- [- cancelPendingPrerolls](<avplayer/cancelpendingprerolls().md>) — Cancels any pending preroll requests and invokes the corresponding completion handlers, if present.
- [sourceClock](avplayer/sourceclock.md) — A clock the player uses for item time bases.
- [masterClock](avplayer/masterclock.md) — The host clock for item time bases. _(deprecated)_

### Preventing sleep and backgrounding

- [preventsDisplaySleepDuringVideoPlayback](avplayer/preventsdisplaysleepduringvideoplayback.md) — A Boolean value that indicates whether video playback prevents display and device sleep.
- [preventsAutomaticBackgroundingDuringVideoPlayback](avplayer/preventsautomaticbackgroundingduringvideoplayback.md) — A Boolean value that indicates whether video playback prevents the system from automatically backgrounding the app.

### Determining content protections

- [outputObscuredDueToInsufficientExternalProtection](avplayer/isoutputobscuredduetoinsufficientexternalprotection.md) — A Boolean value that indicates whether output is being obscured because of insufficient external protection.

### Configuring audio and video devices

- [audioOutputDeviceUniqueID](avplayer/audiooutputdeviceuniqueid.md) — Specifies the unique ID of the Core Audio output device used to play audio.
- [preferredVideoDecoderGPURegistryID](avplayer/preferredvideodecodergpuregistryid.md) — The registry identifier for the GPU used for video decoding.

### Configuring the network resource priority

- [networkResourcePriority](avplayer/networkresourcepriority-swift.property.md) — Indicates the priority of this player for network bandwidth resource distribution.
- [NetworkResourcePriority](avplayer/networkresourcepriority-swift.enum.md) — This defines the network resource priority for a player.

### Configuring observation

- [observationEnabled](avplayer/isobservationenabled.md) — AVPlayer and other AVFoundation types can optionally be observed using Swift Observation.

### Configuring AirPlay behavior

- [allowsAirPlayVideo](avplayer/allowsairplayvideo.md) — A Boolean value that indicates whether the player allows AirPlay video playback. _(deprecated)_
- [airPlayVideoActive](avplayer/isairplayvideoactive.md) — A Boolean value that indicates whether the player is playing video through AirPlay. _(deprecated)_
- [usesAirPlayVideoWhileAirPlayScreenIsActive](avplayer/usesairplayvideowhileairplayscreenisactive.md) — A Boolean value that indicates whether the player automatically switches to AirPlay Video while AirPlay Screen is active. _(deprecated)_

### Displaying closed captions

- [closedCaptionDisplayEnabled](avplayer/isclosedcaptiondisplayenabled.md) — A Boolean value that indicates whether the player uses closed captioning. _(deprecated)_

### Initializers

- [init(URL:)](<avplayer/init(url_)-8aqw0.md>)
- [init(URL:)](<avplayer/init(url_)-9cqj1.md>)

### Instance Properties

- [allowsCaptureOfClearKeyVideo](avplayer/allowscaptureofclearkeyvideo.md) — Indicates whether the video output of ClearKey Encrypted Video can be captured
- [disconnectedFromSystemAudio](avplayer/disconnectedfromsystemaudio.md) — Indicates whether the player is disconnected from system audio. _(beta)_

### Instance Methods

- [setDisconnectedFromSystemAudio(_:completionHandler:)](<avplayer/setdisconnectedfromsystemaudio(__completionhandler_).md>) — Changes whether the player is disconnected from system audio. This method allows you to dynamically change the player’s system audio connection. The operation is asynchronous. Each call to this method will invoke its own completion handler when the operation completes. When changing from `false` to `true`, you should typically call this method first, then deactivate the `AVAudioSession` to allow other audio to resume. _(beta)_

## See Also

### Playback control

- [Observing playback state in SwiftUI](observing-playback-state-in-swiftui.md) — Keep your user interface in sync with state changes from playback objects.
- [Controlling the transport behavior of a player](controlling-the-transport-behavior-of-a-player.md) — Play, pause, and seek through a media presentation.
- [Creating a seamless multiview playback experience](creating-a-seamless-multiview-playback-experience.md) — Build advanced multiview playback experiences with the AVFoundation and AVRouting frameworks.
- [AVPlayerItem](avplayeritem.md) — An object that models the timing and presentation state of an asset during playback.
- [AVPlayerItemTrack](avplayeritemtrack.md) — An object that represents the presentation state of an asset track during playback.
- [AVQueuePlayer](avqueueplayer.md) — An object that plays a sequence of player items.
- [AVPlayerLooper](avplayerlooper.md) — An object that loops media content using a queue player.
